import os
import requests
import sys
import yaml
from source_manager import SourceManager

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

def main():
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    app_token = keys.get('bitable_app_token')
    
    # Needs a Token - reuse feishu_sync or just get it manual?
    # Simple manual fetch for debug
    from feishu_sync import FeishuSync
    feishu = FeishuSync(keys)
    token = feishu.get_tenant_access_token()
    
    # Get Vocab Table ID from sources or hardcode
    table_id = 'tblMYEUusOpQ9HIN' # V2 Table
    print(f"Inspecting Table ID: {table_id}")
    
    # Get Schema
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
    headers = {"Authorization": f"Bearer {token}"}
    
    res = requests.get(url, headers=headers)
    fields = res.json().get('data', {}).get('items', [])
    
    print(f"\n--- Schema Dump for {table_id} ---")
    for f in fields:
        print(f"[{f['field_name']}] Type: {f['type']} | Prop: {f.get('property')}")

    # TEST SAVE - using exact structure as TS
    print("\nAttempting Python Save (Mimicking TS)...")
    import time
    test_fields = {
        "Word": "TS_Mimic",
        "Meaning": "Test",
        "Context Sentence": "Test",
        "Video Title": "Test",
        "Video URL": { "link": "https://example.com", "text": "View Video" },
        "Timestamp": 123,
        "Saved Date": int(time.time() * 1000)
        # Review Count OMITTED
    }
    print("\nAttempting Test Save...")
    save_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records"
    import time
    test_fields = {
        "Word": "DebugWord_EmptyURL",
        "Meaning": "DebugMeaning",
        "Context Sentence": "DebugContext",
        "Video Title": "DebugTitle",
        "Video URL": { "link": "", "text": "View Video" },
        "Timestamp": 123,
        "Saved Date": int(time.time() * 1000)
    }
    
    res = requests.post(save_url, headers=headers, json={"fields": test_fields})
    if res.status_code == 200:
        print("✅ Test Save Success!")
    else:
        print(f"❌ Test Save Failed: {res.text}")

if __name__ == "__main__":
    main()
