import os
import sys
import json
import requests
from source_manager import SourceManager

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8 for Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def inspect_table(token, app_token, table_id, table_name):
    print(f"\n--- Inspecting Table: {table_name} ({table_id}) ---")
    headers = {"Authorization": f"Bearer {token}"}
    
    # 1. List Fields
    url_fields = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
    res = requests.get(url_fields, headers=headers)
    if res.status_code == 200:
        fields = res.json().get('data', {}).get('items', [])
        print("Fields:")
        for f in fields:
            print(f"  - [{f['field_name']}] (Type: {f['type']})")
    else:
        print(f"Failed to list fields: {res.text}")

    # 2. List Records
    url_records = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records"
    res = requests.get(url_records, headers=headers)
    if res.status_code == 200:
        data = res.json().get('data', {})
        total = data.get('total', 0)
        items = data.get('items', [])
        print(f"Total Records: {total}")
        for i, item in enumerate(items[:3]):
            print(f"  Record {i+1}: {json.dumps(item['fields'], ensure_ascii=False)}")
    else:
        print(f"Failed to list records: {res.text}")

def main():
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    # Simple Token Fetch (Copy-paste logic to avoid dep loop if any, or import class)
    # Importing class is better
    from feishu_sync import FeishuSync
    feishu = FeishuSync(keys)
    token = feishu.get_tenant_access_token()
    
    app_token = keys.get('bitable_app_token')
    courses_id = keys.get('courses_table_id')
    lessons_id = keys.get('lessons_table_id')
    
    if courses_id: inspect_table(token, app_token, courses_id, "Courses")
    if lessons_id: inspect_table(token, app_token, lessons_id, "Lessons")

if __name__ == "__main__":
    main()
