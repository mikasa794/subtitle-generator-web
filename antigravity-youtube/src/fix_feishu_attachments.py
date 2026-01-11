import os
import sys
import requests
import json
from source_manager import SourceManager

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

def get_keys():
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    return manager.get_api_keys()

def get_tenant_access_token(app_id, app_secret):
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    payload = {"app_id": app_id, "app_secret": app_secret}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("tenant_access_token")

def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_feishu_attachments.py <record_id>")
        sys.exit(1)

    record_id = sys.argv[1]
    keys = get_keys()
    app_id = keys['feishu_app_id']
    app_secret = keys['feishu_app_secret']
    app_token = keys['bitable_app_token']
    table_id = keys['lingo_table_id']

    token = get_tenant_access_token(app_id, app_secret)
    
    # 1. Fetch Record
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}"
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(url, headers=headers)
    
    if res.status_code != 200:
        print(f"Error fetching record: {res.text}")
        sys.exit(1)
        
    data = res.json().get('data', {}).get('record', {})
    fields = data.get('fields', {})
    
    # 2. Check Transcript File
    files = fields.get('Transcript File', [])
    print(f"Current Files detected: {len(files)}")
    
    for f in files:
        print(f" - {f.get('name')} (Size: {f.get('size')}, Token: {f.get('file_token')})")
        
    if len(files) <= 1:
        print("✅ No duplicates found. Exiting.")
        return

    # 3. Find Largest
    files.sort(key=lambda x: x.get('size', 0), reverse=True)
    best_file = files[0]
    print(f"\n🏆 Keeping Largest: {best_file.get('name')} ({best_file.get('size')})")
    
    # 4. Update Record
    # We must write back the file_token as a list of objects
    payload = {
        "fields": {
            "Transcript File": [{"file_token": best_file.get('file_token')}]
        }
    }
    
    update_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}"
    update_res = requests.put(update_url, headers=headers, json=payload) # PUT usually replaces fields
    
    if update_res.status_code == 200:
        print("✅ Successfully updated record to keep only the largest file.")
    else:
        print(f"❌ Update failed: {update_res.text}")

if __name__ == "__main__":
    main()
