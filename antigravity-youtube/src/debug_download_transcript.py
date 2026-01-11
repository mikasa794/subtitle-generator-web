import os
import requests
import json
from source_manager import SourceManager

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

def main():
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    app_token = keys.get('bitable_app_token')
    lingo_table_id = keys.get('lingo_table_id')
    
    # Get Tenant Token
    url_token = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    res = requests.post(url_token, json={"app_id": keys['feishu_app_id'], "app_secret": keys['feishu_app_secret']})
    token = res.json().get('tenant_access_token')
    
    # 1. Get Record to find File Token
    record_id = "recv79l79tksGz"
    url_rec = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records/{record_id}"
    res = requests.get(url_rec, headers={"Authorization": f"Bearer {token}"})
    if res.status_code != 200:
        print(f"Failed to get record: {res.text}")
        return
        
    fields = res.json().get('data', {}).get('record', {}).get('fields', {})
    tf = fields.get('Transcript File')
    if not tf:
        print("No Transcript File found.")
        return
        
    file_token = tf[0]['file_token']
    print(f"Found File Token: {file_token}")
    
    # 2. Get Download URL (using Drive API 'batch_get_tmp_download_url' is for files in folders, 
    # but for Bitable attachments we usually simply use the 'url' provided in the field if available,
    # OR we use the Drive API if we only have token?
    # Bitable attachment objects usually contain 'url'. Let's check 'tf' content again.
    print(f"Attachment Object: {tf[0]}")
    # Usually it has 'url', 'tmp_url' etc.
    
    download_url = tf[0].get('url')
    if not download_url:
        print("No URL in attachment object. Trying Drive API...")
        # Fallback to Drive API? 
        pass
        
    # 3. Download Content
    print(f"Downloading from: {download_url}...")
    res_dl = requests.get(download_url, headers={"Authorization": f"Bearer {token}"})
    if res_dl.status_code != 200:
        print(f"Failed to download: {res_dl.status_code}")
        return
        
    data = res_dl.json()
    print(f"Total Segments: {len(data)}")
    
    # Inspect specific segments
    indices = [0, 1, 10, 50, 100, -1]
    for i in indices:
        if i < len(data):
            seg = data[i]
            print(f"\n--- Segment {i} ---")
            print(f"Source: {seg.get('text_source')}")
            print(f"Target: {seg.get('text_target')}")
            print(f"Context Keys: {seg.get('context', {}).keys()}")
            
if __name__ == "__main__":
    main()
