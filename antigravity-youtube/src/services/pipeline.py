import os
import json
import logging
import subprocess
import glob
from fetcher import YouTubeFetcher
from services.whisper_service import WhisperService
from feishu_sync import FeishuSync

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LingoPipeline:
    def __init__(self, config_dir, keys):
        self.config_dir = config_dir
        self.keys = keys
        self.fetcher = YouTubeFetcher()
        self.whisper = WhisperService(keys.get('groq_api_key'))
        self.feishu = FeishuSync(keys)
        
        self.app_token = keys.get('bitable_app_token')
        self.lingo_table_id = keys.get('lingo_table_id')

    def process(self, video_url, target_lang='English'):
        logger.info(f"🚀 Starting Magic Import for: {video_url} (Target: {target_lang})")
        
        # 1. Fetch Metadata (Official API / yt-dlp safe mode)
        # Assuming fetcher uses yt-dlp 'extract_flat' which is safe-ish.
        # Ideally, we should add API check here if we implemented it, but for now stick to fetcher's logic.
        info = self.fetcher.get_video_info(video_url)
        if not info:
            logger.error("❌ Failed to fetch video info.")
            return False
            
        title = info.get('title')
        video_id = info.get('id')
        logger.info(f"Video Found: {title} ({video_id})")

        # 2. Ingest Strategy (Hybrid)
        final_transcript_text = None
        source_type = "Unknown"

        # Check for Official English Subs
        logger.info("strategies: Checking for official captions...")
        subs_data = self.fetcher.get_transcript(video_id) # This tries manual en/zh
        
        if subs_data and len(subs_data) > 0:
            logger.info("✅ Official/Manual subtitles found!")
            source_type = "Official (Manual)"
            # Convert fetcher's list output to full text block for context analysis
            # Actually, we need segment-level data for the analysis loop.
            # fetcher returns [{'text':..., 'start':..., 'duration':...}]
            segments = subs_data
        else:
            logger.info("⚠️ No official subtitles. Falling back to Whisper AI...")
            source_type = "AI Generated (Whisper)"
            
            # Download Audio
            audio_path = self.whisper.download_audio(video_url)
            if not audio_path:
                logger.error("❌ Audio download failed.")
                return False
                
            # Transcribe
            whisper_result = self.whisper.transcribe(audio_path)
            if not whisper_result:
                logger.error("❌ Whisper transcription failed.")
                return False
                
            segments = whisper_result.get('segments', [])

            # Cleanup
            try:
                os.remove(audio_path)
            except: pass

        if not segments:
            logger.error("❌ No segments available from either source.")
            return False

        logger.info(f"Got {len(segments)} segments. Starting AI Enrichment...")
        
        # 3. AI Enrichment (Smart Context)
        # We reuse the logic from process_whisper_lingo but integrated here.
        # We need to import analyze_segment_with_groq or reimplement it. 
        # For cleanness, let's keep the logic inline or import if refactored.
        # I'll implement a helper method in this class for now to keep it self-contained.
        
        enriched_data = self._enrich_content(segments, target_lang)
        
        # 4. Save to Feishu
        return self._save_to_feishu(info, enriched_data, source_type)

    def _enrich_content(self, segments):
        from services.whisper_service import requests # Re-import inside if needed or rely on top
        import requests 

        # Limit for demo speed, or full? Let's do partial batch if too long, but product should be full.
    def _enrich_content(self, segments, target_lang='English'):
        import time
        from math import ceil
        
        final_output = []
        api_key = self.keys.get('groq_api_key')
        batch_size = 5 # Reduced from 10 to avoid Context Limit / Truncation with Rich Prompt
        total_batches = ceil(len(segments) / batch_size)
        
        logger.info(f"🚀 Starting Batch Enrichment: {len(segments)} segments in {total_batches} batches.")
        
        for b_idx in range(total_batches):
            start_idx = b_idx * batch_size
            end_idx = min((b_idx + 1) * batch_size, len(segments))
            batch = segments[start_idx:end_idx]
            
            logger.info(f"   Processing Batch [{b_idx+1}/{total_batches}] (segs {start_idx}-{end_idx})...")
            
            batch_texts = [s.get('text', '').strip() for s in batch]
            if not any(batch_texts): # Skip empty batches
                continue
                
            # Call AI with list
            results = self._call_llama_batch(batch_texts, api_key, target_lang)
            
            # Map back
            for i, seg in enumerate(batch):
                text = batch_texts[i]
                analysis = results[i] if i < len(results) else {}
                
                item = {
                    "start": seg['start'],
                    "end": seg['start'] + seg.get('duration', 0) if 'duration' in seg else seg['end'],
                    "text_source": text,
                    "text_target": analysis.get("translation", "(Transcribing...)"),
                    "context": {
                        "type": "dialogue",
                        "summary": analysis.get("summary", ""),
                        "grammar": analysis.get("grammar"),
                        "cultural_note": analysis.get("cultural_note"),
                        "vocab": analysis.get("vocab", [])
                    }
                }
                # JP Support
                if "text_source_ruby" in analysis:
                    item["text_source_ruby"] = analysis["text_source_ruby"]
                
                final_output.append(item)
            
            time.sleep(2.0) # Sleep between batches
            
        return final_output

    def _call_llama_batch(self, texts, api_key, target_lang='English'):
        import requests
        import time
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        
        formatted_inputs = "\n".join([f"{i+1}. {t}" for i, t in enumerate(texts)])
        
        # Dynamic Instructions
        extra_instr = ""
        extra_json = ""
        
        if target_lang.lower() == 'japanese':
            extra_instr = """
            - SOURCE TEXT IS JAPANESE.
            - GENERATE 'text_source_ruby': The source text with HTML ruby tags for Furigana using <ruby>Kanji<rt>Kana</rt></ruby>. 
              Example: "私(わたし)は" -> "<ruby>私<rt>わたし</rt></ruby>は" (Keep particles outside if no kanji).
              Note: Do not add ruby to kana-only words.
            - VOCAB: Include 'kana' reading in the vocab object.
            """
            extra_json = """"text_source_ruby": "<ruby>...</ruby>", """
        
        prompt = f"""
        ROLE: Expert Translator & Language Teacher.
        TASK: Translate the following {len(texts)} lines ({target_lang}) to Simplified Chinese. Extract keys.
        {extra_instr}
        INPUTS:
        {formatted_inputs}
        
        FORMAT (JSON LIST OF OBJECTS ONLY):
        [
            {{
                {extra_json}
                "translation": "Chinese1",
                "summary": "Context1",
                "grammar": "Point1",
                "cultural_note": "Note1",
                "vocab": [
                    {{ 
                        "word": "english_word", 
                        "meaning": "chinese_meaning", 
                        "ipa": "/.../", 
                        "highlight": true,
                        "definition_en": "English definition",
                        "synonyms": ["syn1", "syn2"],
                        "common_phrases": ["phrase 1", "phrase 2"]
                    }}
                ]
            }},
            ...
        ]
                "vocab": [
                    {{ 
                        "word": "english_word", 
                        "meaning": "CHINESE_MEANING_HERE", 
                        "ipa": "/ipa/", 
                        "highlight": true,
                        "definition_en": "English definition",
                        "synonyms": ["syn1"],
                        "common_phrases": ["phrase 1"]
                    }}
                ]
            }},
            ...
        ]
        IMPORTANT: 
        1. 'vocab' MUST be a list of OBJECTS.
        2. EXTRACT VOCABULARY ONLY FROM THE SPECIFIC LINE OF TEXT. DO NOT INCLUDE WORDS FROM PREVIOUS LINES.
        3. If no difficult words, return empty list [].
        4. DO NOT return empty strings for 'meaning' or 'word'.
        5. 'highlight': true only for the focus word.
        6. {target_lang} specific notes apply.
        """
        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
            "response_format": {"type": "json_object"}
        }


        
        retries = 3
        for attempt in range(retries):
            try:
                res = requests.post(url, headers=headers, json=data)
                if res.status_code == 200:
                    content = res.json()['choices'][0]['message']['content']
                    parsed = json.loads(content)
                    
                    # Handle if API returns {"items": [...]} or just [...] depending on json_object constraint
                    # Llama often wraps list in a key if forced to object.
                    if isinstance(parsed, dict):
                        # Try finding the list
                        for k, v in parsed.items():
                            if isinstance(v, list):
                                return v
                                
                        # Fallback: maybe it returned { "1": {...}, "2": {...} }?
                        # Or maybe it failed to follow instruction?
                        pass
                        
                    if isinstance(parsed, list):
                        return parsed
                        
                elif res.status_code == 429:
                    logger.warning(f"⚠️ Rate limit hit (Batch). Sleeping... (Attempt {attempt+1})")
                    time.sleep(5 * (attempt + 1))
                else:
                    logger.error(f"❌ AI Batch Error {res.status_code}: {res.text}")
                    break
            except Exception as e:
                logger.error(f"❌ AI Batch Failed: {e}")
                time.sleep(1)
        
        # Fallback list of empty dicts
        return [{} for _ in texts]

    def _call_llama_analyzer(self, text, api_key):
        import requests
        import time
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        
        prompt = f"""
        ROLE: Expert Translator.
        TASK: Translate "{text}" to Simplified Chinese. Extract vocab/grammar.
        FORMAT (JSON):
        {{
            "translation": "Chinese here",
            "summary": "Context tone",
            "grammar": "Point or null",
            "cultural_note": "Note or null",
            "vocab": [{{ "word": "english_word", "meaning": "chinese_meaning", "ipa": "", "highlight": true }}]
        }}
        """
        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
            "response_format": {"type": "json_object"}
        }
        
        retries = 3
        for attempt in range(retries):
            try:
                res = requests.post(url, headers=headers, json=data)
                if res.status_code == 200:
                    content = res.json()['choices'][0]['message']['content']
                    return json.loads(content)
                elif res.status_code == 429:
                    logger.warning(f"⚠️ Rate limit hit. Sleeping... (Attempt {attempt+1}/{retries})")
                    time.sleep(5 * (attempt + 1)) # Backoff
                else:
                    logger.error(f"❌ AI Error {res.status_code}: {res.text}")
                    break # Don't retry client errors
            except Exception as e:
                logger.error(f"❌ AI Request Failed: {e}")
                time.sleep(1)
        
        return {"translation": "(Translation Unavailable)"} # Fallback message

    def _upload_cover(self, url):
        import requests
        import os
        try:
            # Download
            res = requests.get(url)
            if res.status_code != 200: return None
            
            temp_path = os.path.join(self.config_dir, 'temp_cover.jpg')
            with open(temp_path, 'wb') as f:
                f.write(res.content)
                
            # Upload as File (for Attachment field)
            token = self.feishu.upload_file(temp_path)
            
            try: os.remove(temp_path)
            except: pass
            
            return token
        except Exception as e:
            logger.error(f"Cover upload failed: {e}")
            return None

    def _save_to_feishu(self, info, transcript_data, source_type):
        import requests
        
        # Cover Image Handling
        cover_token = self._upload_cover(info.get('thumbnail'))
        cover_payload = [{"file_token": cover_token}] if cover_token else []
        
        # File Attachment Strategy (Unlimited Size)
        # 1. Save to temp file
        temp_file = os.path.join(self.config_dir, 'temp_transcript.json')
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(transcript_data, f, ensure_ascii=False, indent=2) # Restore indent
            
        # 2. Upload file
        file_token = self.feishu.upload_file(temp_file)
        if not file_token:
            logger.error("❌ Failed to upload transcript file.")
            return False
            
        logger.info(f"✅ Transcript uploaded. Token: {file_token}")
        
        # 3. Construct Record
        record = {
            "Title": info['title'],
            "Series": "Imported", 
            "Target Language": "English",
            "Video URL": {"text": "Watch", "link": info['url']},
            "Cover Image": cover_payload, # Use new field (Attachment, keep for internal)
            "Cover Image URL": info.get('thumbnail', ''), # Text URL (Public Display)
            "Transcript File": [{"file_token": file_token}], # The dedicated attachment field
            "Transcript": "", 
            "Difficulty": "Auto",
            "Status": "Done",
            "AI Notes": f"Source: {source_type}. Full Transcript in 'Transcript File' attachment."
        }
        
        # Cleanup
        try: os.remove(temp_file)
        except: pass
        
        headers = {"Authorization": f"Bearer {self.feishu.get_tenant_access_token()}", "Content-Type": "application/json"}
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.lingo_table_id}/records"
        
        res = requests.post(url, headers=headers, json={"fields": record})
        if res.status_code == 200:
            res_data = res.json()
            if res_data.get('code') == 0:
                record_id = res_data.get('data', {}).get('record', {}).get('record_id')
                logger.info(f"✅ Successfully saved to Feishu! Record ID: {record_id}")
                return True
            else:
                logger.error(f"❌ Feishu Save Failed: {res_data}")
                return False
        else:
            logger.error(f"❌ HTTP Error saving to Feishu: {res.status_code} {res.text}")
            return False

