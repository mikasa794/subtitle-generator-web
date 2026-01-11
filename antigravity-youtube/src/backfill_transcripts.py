import os
import sys
import requests
import json
from source_manager import SourceManager
from feishu_sync import FeishuSync
from fetcher import YouTubeFetcher

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8 for Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def format_transcript(transcript_list):
    if not transcript_list:
        return ""
    lines = []
    for item in transcript_list:
        t = item.get('text', '').strip()
        if t:
            lines.append(t)
    return "\n".join(lines)

def get_youtube_id(url):
    import re
    # Match standard id
    match = re.search(r'(?:v=|\/)([\w-]{11})(?:\?|&|\/|$)', url)
    return match.group(1) if match else None

def main():
    print("🚀 Starting Transcript Backfill...")
    
    # 1. Init
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    feishu = FeishuSync(keys)
    fetcher = YouTubeFetcher()
    
    app_token = keys.get('bitable_app_token')
    lessons_table_id = keys.get('lessons_table_id')
    tenant_token = feishu.get_tenant_access_token()

    if not app_token or not lessons_table_id:
        print("Error: Config missing app_token or lessons_table_id")
        return

    # 2. Fetch All Lessons
    print("Fetching lessons from Feishu...")
    headers = {"Authorization": f"Bearer {tenant_token}"}
    
    all_lessons = []
    page_token = None
    while True:
        params = {"page_size": 100}
        if page_token: params["page_token"] = page_token
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lessons_table_id}/records"
        res = requests.get(url, headers=headers, params=params)
        
        if res.status_code != 200:
            print(f"Error listing lessons: {res.text}")
            break
            
        data = res.json().get('data', {})
        all_lessons.extend(data.get('items', []))
        
        if not data.get('has_more'):
            break
        page_token = data.get('page_token')

    print(f"Found {len(all_lessons)} lessons. Scanning for missing transcripts...")
    
    # 3. Process
    updated_count = 0
    for lesson in all_lessons:
        fields = lesson['fields']
        record_id = lesson['record_id']
        title = fields.get('Title', 'Untitled')
        
        # Check if transcript already exists
        if fields.get('Transcript') and len(fields.get('Transcript')) > 10:
            continue
            
        video_url_obj = fields.get('Video URL')
        if not video_url_obj or not video_url_obj.get('link'):
            continue
            
        video_url = video_url_obj.get('link')
        video_id = get_youtube_id(video_url)
        
        if not video_id:
            continue
            
        print(f"[{updated_count+1}] Backfilling: {title} ({video_id})...")
        
        # Fetch
        transcript_raw = fetcher.get_transcript(video_id)
        if not transcript_raw:
            print("   ⚠️ No transcript available.")
            continue
            
        text = format_transcript(transcript_raw)
        
        # Update Feishu
        update_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lessons_table_id}/records/{record_id}"
        payload = {
            "fields": {
                "Transcript": text
            }
        }
        u_res = requests.put(update_url, headers=headers, json=payload)
        
        if u_res.status_code == 200:
            print("   ✅ Saved!")
            updated_count += 1
        else:
            print(f"   ❌ Update failed: {u_res.text}")

    print(f"\nDone! Backfilled {updated_count} lessons.")

if __name__ == "__main__":
    main()
