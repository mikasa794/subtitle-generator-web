import os
import requests
import json
import sys
from source_manager import SourceManager
from feishu_sync import FeishuSync

# Force UTF-8 for Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

def list_tables(token, app_token):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables"
    headers = {"Authorization": f"Bearer {token}"}
    all_tables = {}
    
    page_token = ""
    while True:
        params = {"page_size": 100, "page_token": page_token}
        res = requests.get(url, headers=headers, params=params)
        if res.status_code != 200:
            print(f"Failed to list tables: {res.text}")
            break
            
        data = res.json().get('data', {})
        for t in data.get('items', []):
            all_tables[t['name']] = t['table_id']
            
        if not data.get('has_more'):
            break
        page_token = data.get('page_token')
        
    return all_tables

def create_table(token, app_token, table_name):
    # Check if exists first
    existing_tables = list_tables(token, app_token)
    if table_name in existing_tables:
        print(f"Table '{table_name}' already exists. ID: {existing_tables[table_name]}")
        return existing_tables[table_name]

    print(f"Creating table: {table_name}...")
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {
        "table": {
            "name": table_name
        }
    }
    response = requests.post(url, headers=headers, json=data)
    # print(f"DEBUG: {response.json()}")
    if response.status_code != 200:
        print(f"Failed to create table {table_name}: {response.text}")
        return None
    
    return response.json().get('data', {}).get('table_id')

def add_fields(token, app_token, table_id, fields):
    print(f"Adding fields to table {table_id}...")
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    for field_name, field_type in fields.items():
        # Feishu Field Types: 1=Text, 3=Number, 15=Url, 11=Attachment, 17=Lookup?
        # Simplified mapping:
        type_code = 1 # Default Text
        if field_type == 'text': type_code = 1
        elif field_type == 'number': type_code = 3
        elif field_type == 'url': type_code = 15 # Hyperlink
        elif field_type == 'image': type_code = 11 # Attachment
        
        data = {
            "field_name": field_name,
            "type": type_code
        }
        res = requests.post(url, headers=headers, json=data)
        if res.status_code == 200:
            print(f"  + Added field: {field_name}")
        else:
            print(f"  ! Failed field {field_name}: {res.json().get('msg')}")

def main():
    # 1. Init Config
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    # 2. Get Token
    feishu = FeishuSync(keys)
    tenant_token = feishu.get_tenant_access_token()
    if not tenant_token:
        print("Failed to get tenant token. Check API keys.")
        return
        
    app_token = keys.get('bitable_app_token')
    if not app_token:
        print("No bitable_app_token found in config.")
        return

    print(f"Connected to Base: {app_token}")

    # 3. Create 'Courses' Table
    courses_id = create_table(tenant_token, app_token, "Courses")
    if courses_id:
        add_fields(tenant_token, app_token, courses_id, {
            "Description": "text",
            "Cover": "image",
            "Status": "text"
        })
        print(f"✅ Created 'Courses' Table ID: {courses_id}")

    # 4. Create 'Lessons' Table
    lessons_id = create_table(tenant_token, app_token, "Lessons")
    if lessons_id:
        add_fields(tenant_token, app_token, lessons_id, {
            "Video URL": "url",
            "Duration": "text",
            "Course ID": "text", # Simple text link for now
            "Module Title": "text"
        })
        print(f"✅ Created 'Lessons' Table ID: {lessons_id}")

    print("\nIMPORTANT: Please add these Table IDs to your configuration if you want to use them automatically.")

if __name__ == "__main__":
    main()
