import json
import os
import sys
import logging
import requests
import time
from source_manager import SourceManager
from feishu_sync import FeishuSync
from services.whisper_service import WhisperService

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def detect_subject(title):
    title_lower = title.lower()
    lang_keywords = [
        'japanese', 'english', 'spanish', 'french', 'language', 
        'katakana', 'hiragana', 'kanji', 'vocabulary', 'grammar', 'pronunciation'
    ]
    tech_keywords = [
        'python', 'react', 'javascript', 'code', 'programming', 'photoshop', 'design', 'ai',
        'typescript', 'node', 'database', 'frontend', 'backend', 'css', 'html'
    ]
    skill_keywords = [
        'guitar', 'music', 'coffee', 'singing', 'drawing', 'art', 'latte', 'vocal'
    ]
    
    if any(k in title_lower for k in lang_keywords):
        return 'LANGUAGE'
    if any(k in title_lower for k in tech_keywords):
        return 'TECH'
    if any(k in title_lower for k in skill_keywords):
        return 'SKILL'
    return 'GENERAL'

def transcribe_with_retry(service, audio_path, max_retries=3):
    for i in range(max_retries):
        res = service.transcribe(audio_path)
        if res: return res
        print(f"   ⚠️ Transcription failed (Attempt {i+1}/{max_retries}). Retrying in 60s...")
        time.sleep(60)
    return None

def get_prompt_for_subject(subject, text):
    base_json_format = """
    RESPONSE FORMAT (JSON ONLY):
    {
        "translation": "Simplified Chinese translation",
        "summary": "Brief analysis",
        "grammar": "Key point (optional)",
        "cultural_note": "Note (optional)",
        "vocab": [
            { 
                "word": "keyword", 
                "meaning": "meaning", 
                "highlight": true 
            }
        ]
    }
    """
    
    if subject == 'LANGUAGE':
        return f"""
        ROLE: Expert Language Teacher.
        TASK: Translate to Chinese and extract Vocabulary/Grammar.
        SENTENCE: "{text}"
        {base_json_format}
        """
    elif subject == 'TECH':
        return f"""
        ROLE: Expert Technical Instructor.
        TASK: Translate to Chinese. Extract Technical Concepts or Libraries as 'vocab'. 
        Use 'grammar' field for Syntax Explanations.
        SENTENCE: "{text}"
        
        RESPONSE FORMAT (JSON ONLY):
        {{
            "translation": "Chinese translation",
            "summary": "Brief stats of what is being done",
            "grammar": "Syntax/Code explanation (optional)",
            "vocab": [
                {{ "word": "Library/Concept", "meaning": "Technical Explanation", "highlight": true }}
            ]
        }}
        """
    elif subject == 'SKILL':
        return f"""
        ROLE: Expert Coach/Instructor.
        TASK: Translate. Extract Techniques, Tools, or Tips.
        SENTENCE: "{text}"
        
        RESPONSE FORMAT (JSON ONLY):
        {{
            "translation": "Chinese translation",
            "summary": "Action/Step summary",
            "cultural_note": "Pro Tip or Common Mistake (optional)",
            "vocab": [
                {{ "word": "Tool/Technique", "meaning": "Usage/Explanation", "highlight": true }}
            ]
        }}
        """
    else: # GENERAL
        return f"""
        ROLE: Translator.
        TASK: Translate and summarize.
        SENTENCE: "{text}"
        {base_json_format}
        """

def analyze_segment_with_groq(text, api_key, subject='GENERAL'):
    """
    Uses Groq (Llama3-70b) to translate and extract context based on subject.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = get_prompt_for_subject(subject, text)
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "response_format": {"type": "json_object"} 
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            try:
                res_json = json.loads(content)
                return res_json
            except json.JSONDecodeError:
                logger.error(f"JSON Parse Error. Raw: {content}")
                return None
        else:
            logger.error(f"Groq LLM Error: {response.text}")
            return None
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        return None

def simple_translate_fallback(text, api_key):
    """Fallback: Just get the translation if JSON fails."""
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"Translate to Simplified Chinese: {text}"}],
        "temperature": 0.3
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
    except Exception:
        pass
    return "(Translation Failed)"

def process_lesson(lesson, keys, manager, whisper_service):
    lesson_id = lesson['record_id']
    title = lesson['fields'].get('Title', 'Untitled')
    course_id_raw = lesson['fields'].get('Course ID') 
    # Note: We don't have Course Title easily here without extra fetch, 
    # but Lesson Title usually contains context (e.g. "Python: ...") or we can infer from Lesson title too.
    # Ideally should fetch Course Record. For now, let's guess from Lesson Title + generic fallback.
    
    subject = detect_subject(title)
    
    # Handle Video URL which might be a dict (link object) or string
    video_url_field = lesson['fields'].get('Video URL', '')
    video_url = video_url_field.get('link') if isinstance(video_url_field, dict) else video_url_field
    
    current_transcript = lesson['fields'].get('Transcript', '')

    print(f"🎬 Processing Lesson: {title} ({lesson_id})")
    print(f"   Subject Detected: {subject}")
    print(f"   URL: {video_url}")

    if not video_url:
        print("   ⚠️ No Video URL. Skipping.")
        return

    # Check if already has JSON transcript (starts with [ { )
def translate_batch_with_groq(texts, api_key, subject='GENERAL'):
    """
    Translates a batch of texts to Chinese using Groq.
    Returns a list of translated strings corresponding to the input.
    """
    if not texts: return []

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Prepare the prompt
    input_text = json.dumps(texts, ensure_ascii=False)
    
    prompt = f"""
    ROLE: Professional Translator ({subject} field).
    TASK: Translate the following list of sentences into Simplified Chinese.
    input: {input_text}
    
    REQUIREMENTS:
    - Return ONLY a raw JSON list of strings.
    - Maintain the exact same order.
    - Maintain the exact same length (one translation per input).
    - If a sentence is just noise/music, return an empty string.
    """

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "response_format": {"type": "json_object"} 
    }
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                content = response.json()['choices'][0]['message']['content']
                try:
                    # Llama sometimes wraps list in a key like {"translations": [...]} or just returns the list if told nicely
                    # But json_object mode requires valid JSON.
                    # Let's try to parse.
                    res_json = json.loads(content)
                    
                    # Heuristic to find the list
                    if isinstance(res_json, list):
                        return res_json
                    elif isinstance(res_json, dict):
                        # valid keys might be 'translations', 'result', etc.
                        # Look for the first list value
                        for k, v in res_json.items():
                            if isinstance(v, list):
                                return v
                                
                    logger.warning(f"Could not find list in JSON: {content[:100]}...")
                    return [""] * len(texts) # Fallback
                    
                except json.JSONDecodeError:
                    logger.error(f"JSON Parse Error. Raw: {content}")
            elif response.status_code == 429:
                logger.warning(f"Rate limit (429) batch. Sleep 10s...")
                time.sleep(10)
            else:
                 logger.error(f"Groq Error {response.status_code}: {response.text}")
        except Exception as e:
            logger.error(f"Batch translate failed: {e}")
            
        time.sleep(2)
            
    return [""] * len(texts) # Fallback empty strings

def process_lesson(lesson, keys, manager, whisper_service):
    lesson_id = lesson['record_id']
    fields = lesson['fields']
    # DEBUG: Print fields to see why Youtube Link is missing
    print(json.dumps(fields, ensure_ascii=False, indent=2)) 
    
    title = fields.get('Title', 'Unknown')
    # Try alternate parsing for Link field
    link_obj = fields.get('Video URL') or fields.get('Youtube Link')
    if isinstance(link_obj, dict):
        video_url = link_obj.get('link') or link_obj.get('text', '')
    elif isinstance(link_obj, str):
        video_url = link_obj
    else:
        video_url = ''
    
    subject = detect_subject(title)
    current_transcript = fields.get('Transcript', '')

    print(f"🎬 Processing Lesson: {title} ({lesson_id})")
    print(f"   Subject Detected: {subject}")
    print(f"   URL: {video_url}")
    
    if not video_url:
        print("   ❌ No Video URL. Skipping.")
        return

    # Check if we should skip (already processed?) 
    # Logic: If transcript is valid JSON and long enough, maybe skip?
    # For now, FORCE UPDATE if running manually
    if current_transcript and current_transcript.strip().startswith('[') and len(current_transcript) > 100:
        print("   ✅ Already has structured transcript. Skipping (force by removing this check if needed).")
        # return # UNCOMMENT TO SKIP ALREADY DONE

    print("   ⬇️ Downloading Audio...")
    audio_path = whisper_service.download_audio(video_url)
    if not audio_path:
        print("   ❌ Download failed.")
        return

    print("   🎙️ Transcribing with Whisper...")
    whisper_json = transcribe_with_retry(whisper_service, audio_path)
    if not whisper_json:
        print("   ❌ Transcription failed after retries.")
        return

    segments = whisper_json.get('segments', [])
    print(f"   ✨ Got {len(segments)} segments. Enriching with AI ({subject})...")

    final_output = []
    groq_key = keys.get('groq_api_key')
    
    # Process in Batches
    BATCH_SIZE = 20
    total_segments = len(segments)
    
    for i in range(0, total_segments, BATCH_SIZE):
        batch = segments[i:i+BATCH_SIZE]
        print(f"     Processing Batch {i//BATCH_SIZE + 1}/{(total_segments//BATCH_SIZE)+1} (Segs {i}-{i+len(batch)})...")
        
        texts_source = [seg['text'].strip() for seg in batch]
        
        # Translate Batch
        translations = translate_batch_with_groq(texts_source, groq_key, subject)
        
        # Ensure alignment
        if len(translations) != len(batch):
            logger.warning(f"Mismatch: Sent {len(batch)}, Got {len(translations)}. Padding/Truncating.")
            if len(translations) < len(batch):
                translations += [""] * (len(batch) - len(translations))
            else:
                translations = translations[:len(batch)]
                
        # Merge
        for idx, seg in enumerate(batch):
            item = {
                "start": seg['start'],
                "end": seg['end'],
                "text_source": seg['text'].strip(),
                "text_target": translations[idx],
                "context": {"type": subject.lower()} # Minimal context for now to save tokens
            }
            final_output.append(item)
            
        time.sleep(1) # Polite delay betwen batches

    # Save back to Feishu
    transcript_json_str = json.dumps(final_output, ensure_ascii=False, indent=2)
    
    print(f"   💾 Saving to Feishu...")
    # Using raw requests here because FeishuSync might not have specific update method for arbitrary tables readily exposed without mods
    # But FeishuSync has `sync_to_bitable` which creates new records. We need UPDATE.
    # Let's use direct requests for UPDATE.
    
    feishu = FeishuSync(keys)
    token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    lessons_table_id = keys.get('lessons_table_id')
    
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lessons_table_id}/records/{lesson_id}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    res = requests.put(url, headers=headers, json={"fields": {"Transcript": transcript_json_str}})
    
    if res.status_code == 200:
        print("   ✅ Success! Lesson updated.")
    else:
        print(f"   ❌ Feishu Update Failed: {res.text}")

def main():
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    whisper_service = WhisperService(keys.get('groq_api_key'))
    
    feishu = FeishuSync(keys)
    token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    lessons_table_id = keys.get('lessons_table_id')

    # Fetch Lessons to process
    # Limit to 1 for testing if user requested, but let's query a few
    print("🔍 Fetching potential lessons...")
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lessons_table_id}/records?page_size=50"
    headers = {"Authorization": f"Bearer {token}"}
    
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print("Failed to list lessons")
        return

    items = res.json().get('data', {}).get('items', [])
    print(f"Found {len(items)} lessons.")

    # Sort or Filter? 
    # Let's just find the first one that has a Video URL but NO structured transcript
    
    processed_count = 0
    for item in items:
        # Check if we should process this one
        transcript = item['fields'].get('Transcript', '')
        if transcript.startswith('['): 
            continue # Already done
            
        video_url = item['fields'].get('Video URL')
        if not video_url:
            continue
            
        # Found a candidate!
        process_lesson(item, keys, manager, whisper_service)
        processed_count += 1
        
        # STOP after 1 checking removed.
        # if processed_count >= 1:
        #    print("🛑 Stopping after 1 lesson for verification.")
        #    break

if __name__ == "__main__":
    main()
