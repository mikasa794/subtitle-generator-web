import json
import os
import sys
import logging
import requests
from source_manager import SourceManager
from feishu_sync import FeishuSync

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

def analyze_segment_with_groq(text, api_key):
    """
    Uses Groq (Llama3-70b) to translate and extract context.
    Returns a dict with text_target, context (vocab, grammar, summary).
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""
    ROLE: Expert English-to-Chinese Translator & Teacher.
    TASK: Translate the sentence to Natural Simplified Chinese and extract learning points.
    
    SENTENCE: "{text}"
    
    RESPONSE FORMAT (JSON ONLY):
    {{
        "translation": "Put the Simplified Chinese translation here. MUST NOT BE EMPTY.",
        "summary": "Brief context/tone in Chinese",
        "grammar": "One grammar point (optional)",
        "cultural_note": "Explain cultural background (e.g. Holidays, Famous People) if any (optional)",
        "vocab": [
            {{ 
                "word": "keyword", 
                "ipa": "/ipa/", 
                "meaning": "Chinese meaning", 
                "definition_en": "Simple English definition",
                "synonyms": ["synonym1", "synonym2"],
                "common_phrases": ["phrase 1", "phrase 2"],
                "highlight": true 
            }}
        ]
    }}
    
    IMPORTANT: 
    - "translation" field is MANDATORY. 
    - If "Hanukkah" or similar cultural terms appear, YOU MUST provide a "cultural_note".
    - "definition_en", "synonyms", "common_phrases" are highly desired for the dictionary feature.
    - If unsure, provide a literal translation.
    - Output valid JSON only.
    """
    
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
                # print(f"DEBUG LLM: {res_json}") # Optional verbose
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
        else:
             print(f"Fallback Error Status: {response.status_code}, Body: {response.text}")
    except Exception as e:
        print(f"Fallback Exception: {e}")
    return "(Translation Failed)"

def main():
    # 1. Load Config
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    groq_key = keys.get('groq_api_key')
    
    if not groq_key:
        logger.error("Groq Key missing.")
        return

    # 2. Load Whisper Result
    whisper_file = "whisper_result.json"
    if not os.path.exists(whisper_file):
        logger.error("whisper_result.json not found. Run fetch_audio_whisper.py first.")
        return
        
    with open(whisper_file, "r", encoding="utf-8") as f:
        whisper_data = json.load(f)
        
    segments = whisper_data.get('segments', [])
    logger.info(f"Loaded {len(segments)} segments.")
    
    final_output = []
    
    # Process each segment (LIMIT to first 10 for speed demo, or all?)
    # For Phase 3 demo, let's do first 8 segments to cover the intro fully.
    # Or maybe user wants the WHOLE video? It's 2 mins.
    # Llama3-70b is fast. Let's do a batch of 15 segments.
    
    logger.info("Enriching segments with Llama3 (this may take 30s)...")
    
    for i, seg in enumerate(segments[:50]): 
        print(f"Propcessing [{i+1}/{min(50, len(segments))}]: {seg['text']}")
        
        analysis = analyze_segment_with_groq(seg['text'], groq_key)
        
        # Validation & Fallback
        translation = ""
        context_data = {"type": "dialogue"}
        
        if analysis and analysis.get("translation"):
             translation = analysis.get("translation")
             context_data = {
                "type": "dialogue",
                "summary": analysis.get("summary", ""),
                "grammar": analysis.get("grammar"),
                "cultural_note": analysis.get("cultural_note"),
                "vocab": analysis.get("vocab", [])
             }
        else:
             # Trigger Fallback
             print(f" -> JSON Failed/Empty. Triggering Fallback Translation...")
             translation = simple_translate_fallback(seg['text'], groq_key)
        
        item = {
            "start": seg['start'],
            "end": seg['end'],
            "text_source": seg['text'].strip(),
            "text_target": translation,
            "context": context_data
        }
        final_output.append(item)

    # 3. Update Feishu Record (Target ID: recv6B1UnqPPmK)
    target_id = "recv6B1UnqPPmK"
    
    transcript_json_str = json.dumps(final_output, ensure_ascii=False, indent=2)
    
    logger.info(f"Uploading enriched transcript to {target_id}...")
    
    feishu = FeishuSync(keys)
    tenant_token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    lingo_table_id = keys.get('lingo_table_id')
    
    url_feishu = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records/{target_id}"
    
    headers = {"Authorization": f"Bearer {tenant_token}", "Content-Type": "application/json"}
    
    res = requests.put(
        url_feishu,
        headers=headers, 
        json={"fields": {
            "Title": "Friends: S4E06 (Whisper+Llama3 Auto-Gen)",
            "Transcript": transcript_json_str,
            "AI Notes": "Generated via Groq Pipeline (Whisper V3 -> Llama3)"
        }}
    )
    
    if res.status_code == 200:
        logger.info("✅ Success! Record updated.")
    else:
        logger.error(f"Feishu Update Failed: {res.text}")

if __name__ == "__main__":
    main()
