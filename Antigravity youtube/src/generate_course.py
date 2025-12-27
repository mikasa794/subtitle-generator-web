import os
import sys
import json
import subprocess
import requests
from source_manager import SourceManager
from feishu_sync import FeishuSync

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

def find_best_video(query):
    print(f"🔍 Searching YouTube: '{query}'...")
    cmd = [
        "python", "-m", "yt_dlp",
        f"ytsearch1:{query}",
        "--print", "id",
        "--print", "title",
        "--print", "duration_string",
        "--print", "thumbnail",
        "--no-warnings"
    ]
    
    
    try:
        # returns bytes
        result = subprocess.run(cmd, capture_output=True) 
        try:
            output = result.stdout.decode('utf-8')
        except UnicodeDecodeError:
             # Fallback for Windows typically
            output = result.stdout.decode('gbk', errors='ignore')

        lines = output.strip().split('\n')
        
        if len(lines) >= 4:
            return {
                "id": lines[0],
                "title": lines[1],
                "duration": lines[2],
                "thumbnail": lines[3],
                "url": f"https://www.youtube.com/watch?v={lines[0]}"
            }
    except Exception as e:
        print(f"Error searching video: {e}")
        return None
    return None

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
        
        # Sync Course
        # Note: feishu_sync.sync_to_bitable returns True/False. 
        # But we need the Record ID to link lessons?
        # Feishu's create_record API returns the record_id. 
        # Our current FeishuSync.sync_to_bitable logic ONLY returns True/False.
        # We need to modifying FeishuSync OR just call API here directly for the Course to get its ID.
        # Let's call API directly here for precision since we need the ID.
        
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
            
            video_info = find_best_video(mod['search_query'])
            
            if video_info:
                # Capture first available thumbnail for course cover
                if not first_thumbnail and video_info.get('thumbnail'):
                    first_thumbnail = video_info['thumbnail']

                lesson_record = {
                    "Title": mod['title'],
                    "Module Title": mod['title'],
                    "Video URL": {"text": "Watch on YouTube", "link": video_info['url']},
                    "Duration": video_info['duration'],
                    "Course ID": [course_record_id]
                }
                
                lesson_record["Course ID"] = course_record_id 
                
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
            # We use a text field 'Cover Image URL' to avoid complex attachment upload flows
            update_fields["Cover Image URL"] = first_thumbnail
            
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
