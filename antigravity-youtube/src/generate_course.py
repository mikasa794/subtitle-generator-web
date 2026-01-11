import os
import sys
import json
import subprocess
import requests
from source_manager import SourceManager
from feishu_sync import FeishuSync
from fetcher import YouTubeFetcher
from services.whisper_service import WhisperService

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8 for Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def generate_syllabus(topic):
    print(f"🧠 AI Planning Curriculum for: '{topic}'...")
    node_script = os.path.join(BASE_DIR, 'src', 'ai_course_planner.js')
    
    result = subprocess.run(
        ['node', node_script, topic],
        capture_output=True, text=True, encoding='utf-8'
    )
    
    if result.returncode != 0:
        raise Exception(f"AI Planner Failed: {result.stderr}")
    
    raw_json = result.stdout.strip()
    if raw_json.startswith('```json'):
        raw_json = raw_json[7:]
    if raw_json.endswith('```'):
        raw_json = raw_json[:-3]
        
    try:
        return json.loads(raw_json)
    except json.JSONDecodeError:
        print("Failed to parse JSON. Raw output:")
        print(raw_json)
        raise

def format_transcript(transcript_list):
    """
    Formats list of {'text', 'start', ...} into a readable string.
    """
    if not transcript_list:
        return ""
    
    lines = []
    for item in transcript_list:
        t = item.get('text', '').strip()
        if t:
            # Optional: Add timestamps? [00:12] Text
            # For comprehensive reading, simple text is better, but videos need ref.
            # Let's add simple timestamps every ~30 seconds or so? 
            # For MVP simplicity: just text.
            lines.append(t)
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/generate_course.py \"<topic>\"")
        return

    topic = sys.argv[1]
    
    # Debug: Log topic to file
    with open(os.path.join(BASE_DIR, 'src', 'last_run.txt'), 'w', encoding='utf-8') as f:
        f.write(f"Received Topic: {topic}")
    
    # 1. Init
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    feishu = FeishuSync(keys)
    fetcher = YouTubeFetcher() # Init fetcher (Still used for info)
    
    groq_key = keys.get('groq_api_key')
    if not groq_key:
        print("Error: Groq API Key missing.")
        return
        
    whisper_service = WhisperService(groq_key)
    
    courses_table_id = keys.get('courses_table_id')
    lessons_table_id = keys.get('lessons_table_id')
    
    if not courses_table_id or not lessons_table_id:
        print("Error: Table IDs not found in config. Run setup_course_tables.py first.")
        return

    try:
        # 2. Generate Syllabus
        course_data = generate_syllabus(topic)
        title = course_data.get('course_title', topic)
        desc = course_data.get('description', '')
        
        print(f"\nCreating Course: {title}")
        
        # 3. Create Course Record
        course_record = {
            "Title": title,
            "Description": desc,
            "Status": "Generating"
        }
        
        token = feishu.get_tenant_access_token()
        app_token = keys.get('bitable_app_token')
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{courses_table_id}/records"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        
        res = requests.post(url, headers=headers, json={"fields": course_record})
        if res.status_code != 200:
            print(f"Failed to create course: {res.text}")
            return
            
        course_record_id = res.json().get('data', {}).get('record', {}).get('record_id')
        print(f"✅ Course Created. Record ID: {course_record_id}")
        
        # 4. Find Videos & Create Lessons
        modules = course_data.get('modules', [])
        first_thumbnail = None

        for i, mod in enumerate(modules):
            print(f"\nProcessing Module {i+1}: {mod['title']}")
            
            # Use fetcher to search (via yt-dlp wrapped logic or just call directly)
            # fetcher currently doesn't expose 'search' directly, it has get_video_info(url)
            # We still need find_best_video logic. Let's reimplement it using subprocess for search
            # because yt-dlp search is efficient.
            
            search_query = mod['search_query']
            print(f"   Searching: {search_query}...")
            
            # Simple yt-dlp search
            try:
                # ytsearch1 prints id
                cmd = ["python", "-m", "yt_dlp", f"ytsearch1:{search_query}", "--print", "id", "--no-warnings"]
                s_res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
                video_id = s_res.stdout.strip()
            except Exception as e:
                print(f"   Search error: {e}")
                video_id = None

            if video_id:
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                
                # Get Info & Transcript
                # We use fetcher.get_video_info to get clean details (title, duration, thumbnail)
                # And get_transcript for text
                
                info = fetcher.get_video_info(video_url)
                if not info:
                     # Fallback if fetcher fails?
                     print("   Failed to get video details.")
                     continue

                if not first_thumbnail and info.get('thumbnail'):
                    first_thumbnail = info['thumbnail']

                # Use Whisper Service for Transcript
                print("   Transcribing with Whisper AI (Standard Pipeline)...")
                try:
                     audio_path = whisper_service.download_audio(video_url)
                     if audio_path:
                         transcript_json = whisper_service.transcribe(audio_path)
                         transcript_text = whisper_service.format_transcript_simple(transcript_json)
                     else:
                         transcript_text = "(Audio Download Failed)"
                except Exception as e:
                     print(f"   Whisper Pipeline failed. Falling back to simple text. Error: {e}")
                     transcript_text = "(Transcript Unavailable - Error)"

                lesson_record = {
                    "Title": mod['title'], 
                    "Module Title": mod['title'],
                    "Video URL": {"text": "Watch on YouTube", "link": video_url},
                    "Duration": str(info.get('duration')),
                    "Course ID": course_record_id, # FIX: Send as String, not List ['id']
                    "Transcript": transcript_text
                }
                
                # Sync Lesson
                res_l = requests.post(
                    f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lessons_table_id}/records", 
                    headers=headers, 
                    json={"fields": lesson_record}
                )
                res_json = res_l.json()
                if res_l.status_code == 200 and res_json.get('code') == 0:
                   print(f"   ✅ Lesson saved: {mod['title']}")
                else:
                   print(f"   ❌ Lesson save failed: {res_json}")

            else:
                print("   ❌ No video found.")

        # 5. Update Course Status & Cover
        print("\nUpdating Course Status...")
        update_fields = {"Status": "Done"}
        if first_thumbnail:
            update_fields["Cover Image URL"] = first_thumbnail
            # Try upload as attachment too if needed? No, URL field is simpler for now.
            
        requests.put(
            f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{courses_table_id}/records/{course_record_id}",
            headers=headers,
            json={"fields": update_fields}
        )
        print("Done! 🚀")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
