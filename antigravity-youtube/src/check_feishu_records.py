import os
import requests
import sys
import json
from source_manager import SourceManager
from feishu_sync import FeishuSync

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8 for Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def main():
    print("🔍 Checking Feishu Lingo Records...")
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    feishu = FeishuSync(keys)
    tenant_token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    lingo_table_id = keys.get('lingo_table_id')

    if not app_token or not lingo_table_id:
        print("Error: Config missing app_token or lingo_table_id")
        return

    headers = {"Authorization": f"Bearer {tenant_token}"}
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records"
    
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(f"Error fetching records: {res.text}")
        return

    data = res.json()
    items = data.get('data', {}).get('items', [])
    print(f"Found {len(items)} records:")
    for item in items:
        fields = item.get('fields', {})
        print(f"- {fields.get('Title', 'Untitled')} (ID: {item['record_id']})")

if __name__ == "__main__":
    main()
