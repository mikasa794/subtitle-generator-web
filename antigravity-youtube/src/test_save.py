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
    user_token = keys.get('feishu_user_access_token') # Using user token or tenant? Setup used tenant.
    
    # Get Tenant Token
    url_token = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    res = requests.post(url_token, json={"app_id": keys['feishu_app_id'], "app_secret": keys['feishu_app_secret']})
    token = res.json().get('tenant_access_token')
    print(f"Token: {token[:10]}...")
    
    # Test Data
    # Use the token we saw earlier: AtfPbkjsAoQazLxT5JUc6AcMnWe
    file_token = "AtfPbkjsAoQazLxT5JUc6AcMnWe" 
    
    record = {
        "Title": "Debug Full Payload Test",
        "Series": "Imported",
        "Target Language": "English",
        "Video URL": {"text": "Watch", "link": "https://example.com"},
        "Cover Image URL": "", # Test empty
        "Transcript File": [{"file_token": file_token}],
        "Transcript": "",
        "Difficulty": "Auto",
        "Status": "Done",
        "AI Notes": "Test Notes"
    }
    
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    print("Sending request...")
    res = requests.post(url, headers=headers, json={"fields": record})
    print(f"Status: {res.status_code}")
    print(f"Response: {res.text}")

if __name__ == "__main__":
    main()
