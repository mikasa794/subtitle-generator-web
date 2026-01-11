import os
import sys
import json
import subprocess
import requests
from source_manager import SourceManager
from feishu_sync import FeishuSync
from fetcher import YouTubeFetcher
# Import helper functions from generate_course would be better, but for speed let's copy minor logic
# actually let's import the generate_syllabus from generate_course if possible, or duplicate safely.
# Importing implies running top-level code if not careful. generate_course has if __name__ == "__main__".

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def generate_syllabus(topic):
    print(f"🧠 AI Planning Curriculum for: '{topic}'...")
    node_script = os.path.join(BASE_DIR, 'src', 'ai_course_planner.js')
    result = subprocess.run(['node', node_script, topic], capture_output=True, text=True, encoding='utf-8')
    if result.returncode != 0:
        raise Exception(f"AI Planner Failed: {result.stderr}")
    raw_json = result.stdout.strip()
    if raw_json.startswith('```json'): raw_json = raw_json[7:]
    if raw_json.endswith('```'): raw_json = raw_json[:-3]
    return json.loads(raw_json)

def format_transcript(transcript_list):
    if not transcript_list: return ""
    lines = [item.get('text', '').strip() for item in transcript_list]
    return "\n".join(filter(None, lines))

def main():
    target_course_id = "recv6BljxupuWb" # Corrected ID (lowercase j)
    
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    feishu = FeishuSync(keys)
    fetcher = YouTubeFetcher()
    
    app_token = keys.get('bitable_app_token')
    courses_table_id = keys.get('courses_table_id')
    lessons_table_id = keys.get('lessons_table_id')
    token = feishu.get_tenant_access_token()
    
    # 1. Get Course Details
    print(f"🔍 Fetching Course Details: {target_course_id}...")
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{courses_table_id}/records/{target_course_id}"
    res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    if res.status_code != 200:
        print(f"❌ Failed to get course: {res.text}")
        return
        
    course_data = res.json().get('data', {}).get('record', {}).get('fields', {})
    print(f"DEBUG RAW FIELDS: {json.dumps(course_data, ensure_ascii=False)}")
    course_title = course_data.get('Title')
    print(f"✅ Found Course: {course_title}")
    
    if not course_title:
        print("❌ Course has no title. Cannot regenerate.")
        return

    # 2. Regenerate Syllabus
    print("🔄 Regenerating Syllabus...")
    # Use title as topic
    syllabus = generate_syllabus(course_title)
    modules = syllabus.get('modules', [])
    print(f"📋 Generated {len(modules)} modules.")
    
    # 3. Create Lessons
    first_thumbnail = None
    
    for i, mod in enumerate(modules):
        print(f"\nProcessing Module {i+1}: {mod['title']}")
        search_query = mod['search_query']
        print(f"   Searching: {search_query}...")
        
        video_id = None
        try:
             # Try ytsearch1
             cmd = ["python", "-m", "yt_dlp", f"ytsearch1:{search_query}", "--print", "id", "--no-warnings"]
             s_res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
             video_id = s_res.stdout.strip()
        except Exception as e:
             print(f"   Search error: {e}")

        if video_id:
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            info = fetcher.get_video_info(video_url)
            
            if not info:
                print("   Failed to get video info.")
                continue
                
            if not first_thumbnail and info.get('thumbnail'):
                first_thumbnail = info['thumbnail']
                
            print("   Fetching transcript...")
            t_raw = fetcher.get_transcript(video_id)
            t_text = format_transcript(t_raw) or "(No transcript)"
            
            lesson_record = {
                "Title": mod['title'],
                "Module Title": mod['title'],
                "Video URL": {"text": "Watch", "link": video_url},
                "Duration": str(info.get('duration')),
                "Course ID": target_course_id, # Linking back to the existing course!
                "Transcript": t_text[:5000] # truncate if too long? simple string is fine
            }
            
            # Save
            res_l = requests.post(
                f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lessons_table_id}/records", 
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                json={"fields": lesson_record}
            )
            if res_l.status_code == 200:
                print(f"   ✅ Saved Lesson: {mod['title']}")
            else:
                print(f"   ❌ Save failed: {res_l.text}")
        else:
            print("   ❌ No video found.")

    print("\n✅ Regeneration Complete!")

if __name__ == "__main__":
    main()
