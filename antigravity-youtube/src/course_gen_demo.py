import os
import sys
import json
import subprocess
import shutil

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    
    # Clean output (remove markdown fences if any)
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
    
    # Use yt-dlp to search and get metadata
    # ytsearch1 means "search and take top 1"
    cmd = [
        "python", "-m", "yt_dlp",
        f"ytsearch1:{query}",
        "--print", "id",
        "--print", "title",
        "--print", "duration_string",
        "--no-warnings"
    ]
    
    # On Windows, we need to be careful with utf-8
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        lines = result.stdout.strip().split('\n')
        
        if len(lines) >= 3:
            return {
                "id": lines[0],
                "title": lines[1],
                "duration": lines[2],
                "url": f"https://www.youtube.com/watch?v={lines[0]}"
            }
    except FileNotFoundError:
        print("Error: yt-dlp not found in PATH.")
        return None
        
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/course_gen_demo.py \"<topic>\"")
        return

    topic = sys.argv[1]
    
    try:
        # 1. Generate Syllabus
        course_data = generate_syllabus(topic)
        
        print("\n" + "="*50)
        print(f"🎓 COURSE: {course_data.get('course_title', topic)}")
        print(f"📝 {course_data.get('description', '')}")
        print("="*50 + "\n")
        
        # 2. Find Videos
        modules = course_data.get('modules', [])
        for mod in modules:
            print(f"Subject: {mod['title']}")
            
            video_info = find_best_video(mod['search_query'])
            
            if video_info:
                print(f"   📺 FOUND: {video_info['title']}")
                print(f"   ⏱️ Duration: {video_info['duration']}")
                print(f"   🔗 Link: {video_info['url']}")
            else:
                print("   ❌ No confirmed video found.")
            print("-" * 30)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
