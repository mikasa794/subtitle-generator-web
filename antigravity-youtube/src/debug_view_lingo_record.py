import os
import requests
import json
import sys
from source_manager import SourceManager
from feishu_sync import FeishuSync

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')
sys.stdout.reconfigure(encoding='utf-8')

def main():
    target_id = "recv7iS6yqKJb3"
    print(f"🔍 Inspecting Record: {target_id}")

    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    feishu = FeishuSync(keys)
    token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    lingo_table_id = keys.get('lingo_table_id')

    # 1. Fetch Latest Record
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records?sort=[\"Created Time DESC\"]&pageSize=1"
    res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    if res.status_code != 200:
        print(f"❌ API Error: {res.text}")
        return

    items = res.json().get('data', {}).get('items', [])
    if not items:
        print("❌ No records found")
        return
        
    record = items[0]
    target_id = record['record_id']
    print(f"🔍 Inspecting Latest Record: {target_id} ({record['fields'].get('Title', 'Untitled')})")
    if not record:
        print("❌ Record not found")
        return

    fields = record['fields']
    
    # 2. Get Attachment
    transcript_file = fields.get('Transcript File')
    if not transcript_file:
         print("❌ No Transcript File attachment found.")
         # Fallback to text for debugging
         print(f"Fields: {fields.keys()}")
         return

    file_url = transcript_file[0]['url']
    print(f"⬇️ Downloading JSON from: {file_url[:60]}...")
    
    # 3. Download JSON
    f_res = requests.get(file_url, headers={"Authorization": f"Bearer {token}"})
    if f_res.status_code != 200:
        f_res = requests.get(file_url) # Try no-auth
    
    if f_res.status_code != 200:
        print(f"❌ Download failed: {f_res.status_code}")
        return

    try:
        content = f_res.json()
    except:
        print("❌ Invalid JSON content")
        return

    print(f"✅ JSON Parsed. Total Segments: {len(content)}")

    # 4. Search for window
    print("\n--- Searching for 'しん' or 'Shin' ---")
    for i, item in enumerate(content):
        txt = item.get('text_source', '')
        if 'しん' in txt or 'Shin' in txt or 'の' in txt: # Generic Japanese particle to match all
            print(f"\n📍 Match at Index [{i}]")
            
            # Print Window
            start = max(0, i - 1)
            end = min(len(content), i + 2)
            for k in range(start, end):
                seg = content[k]
                vocabs = seg.get('context', {}).get('vocab', [])
                v_words = [v.get('word') for v in vocabs]
                print(f"[{k}] {seg.get('text_source')}")
                print(f"     Ruby: {seg.get('text_source_ruby', '(No Ruby)')}")
                print(f"     Vocab: {v_words}")
                
if __name__ == "__main__":
    main()
