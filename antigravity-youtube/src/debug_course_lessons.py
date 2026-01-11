import os
import requests
import json
import sys
from source_manager import SourceManager
from feishu_sync import FeishuSync

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def main():
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    feishu = FeishuSync(keys)
    token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    lessons_table_id = keys.get('lessons_table_id')
    courses_table_id = keys.get('courses_table_id')

    target_course_id = "recv6BljxupuWb" # From screenshot (Corrected case)
    
    print(f"🔍 Inspecting Lessons for Course: {target_course_id}")
    
    # 1. Fetch ALL lessons (limited to 20 for debug) to see structure
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lessons_table_id}/records?page_size=20"
    headers = {"Authorization": f"Bearer {token}"}
    
    res = requests.get(url, headers=headers)
    
    if res.status_code != 200:
        print(f"Error fetching lessons: {res.text}")
        return
        
    data = res.json()
    items = data.get('data', {}).get('items', [])
    
    print(f"Found {len(items)} lessons (first page). checking fields...")
    
    found_count = 0
    for item in items:
        f = item['fields']
        course_link = f.get('Course ID')
        title = f.get('Title')
        
        # Check if it matches
        # Link fields usually come as ["recXXXX", "recYYYY"]
        is_match = False
        if isinstance(course_link, list) and target_course_id in course_link:
            is_match = True
        elif course_link == target_course_id:
            is_match = True
            
        video_url = f.get('Video URL', {})
        link_url = video_url.get('link') if isinstance(video_url, dict) else video_url
        
        print(f" - Lesson: {title}")
        print(f"   Video URL: {link_url}")
        print(f"   Course ID Field (Raw): {course_link} (Type: {type(course_link)})")
        
        if is_match:
            print("   ✅ MATCHES TARGET!")
            found_count += 1
            
    print(f"\nTotal matches found manually: {found_count}")
    
    # 2. Test the specific filter used in frontend
    print("\n--------------------------------")
    print("Testing Frontend Filter Query...")
    # Frontend uses: filter: CurrentValue.[Course ID]="{courseId}"
    
    filter_str = f'CurrentValue.[Course ID]="{target_course_id}"'
    params = {"filter": filter_str}
    
    res_filter = requests.get(url, headers=headers, params=params)
    data_filter = res_filter.json()
    filter_items = data_filter.get('data', {}).get('items', [])
    
    print(f"Filter: '{filter_str}'")
    print(f"Returned Count: {len(filter_items)}")
    
    if len(filter_items) == 0 and found_count > 0:
        print("❌ Filter FAILED but data exists! The filter syntax is wrong for Link fields.")
    elif len(filter_items) > 0:
        print("✅ Filter works.")

if __name__ == "__main__":
    main()
