import os
import requests
import json
import sys
from source_manager import SourceManager
from feishu_sync import FeishuSync

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def main():
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    feishu = FeishuSync(keys)
    token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    courses_table_id = keys.get('courses_table_id')

    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{courses_table_id}/records"
    res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    
    if res.status_code != 200:
        print(f"Error: {res.text}")
        return

    items = res.json().get('data', {}).get('items', [])
    print(f"Found {len(items)} courses:")
    
    for item in items:
        rid = item.get('record_id')
        title = item['fields'].get('Title', 'Untitled')
        print(f"- [{rid}] {title}")
        print(f"  Fields keys: {list(item['fields'].keys())}")

if __name__ == "__main__":
    main()
