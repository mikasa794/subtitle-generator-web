import os
import requests
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
    table_id = keys.get('courses_table_id')
    
    # Authenticate
    res = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={
            "app_id": keys['feishu_app_id'],
            "app_secret": keys['feishu_app_secret']
        }
    )
    token = res.json()['tenant_access_token']
    
    print(f"Adding 'Cover Image URL' to Table: {table_id}")
    
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    # 1 is Text field type
    payload = {
        "field_name": "Cover Image URL",
        "type": 1 
    }
    
    resp = requests.post(url, headers=headers, json=payload)
    print(resp.json())

if __name__ == "__main__":
    main()
