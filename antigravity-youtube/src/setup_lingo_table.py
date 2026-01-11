import os
import requests
import sys
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
    data = {"table": {"name": table_name}}
    
    response = requests.post(url, headers=headers, json=data)
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
        type_code = 1 # Default Text
        if field_type == 'text': type_code = 1
        elif field_type == 'number': type_code = 3
        elif field_type == 'url': type_code = 15 
        elif field_type == 'image': type_code = 11
        elif field_type == 'multi_line': type_code = 1  # Still text but implies usage
        
        data = {
            "field_name": field_name,
            "type": type_code
        }
        res = requests.post(url, headers=headers, json=data)
        if res.status_code == 200:
            print(f"  + Added field: {field_name}")
        else:
            err = res.json()
            if "already exists" in str(err) or "重复" in str(err):
                print(f"  = Field {field_name} exists.")
            else:
                print(f"  ! Failed field {field_name}: {err.get('msg')}")

def main():
    print("🚀 Setting up LingoTube Schema...")
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    feishu = FeishuSync(keys)
    tenant_token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    
    if not app_token:
        print("Error: No bitable_app_token found.")
        return

    # Create LingoClips Table
    table_id = create_table(tenant_token, app_token, "LingoClips")
    
    if table_id:
        add_fields(tenant_token, app_token, table_id, {
            "Title": "text",
            "Series": "text",          # Friends, Conan
            "Target Language": "text", # English, Japanese
            "Video URL": "url",
            "Transcript": "text",      # 1 is multi-line capable usually
            "Difficulty": "text",      # Beginner, etc.
            "Status": "text",
            "AI Notes": "text",        # JSON or text blob for grammar points
            "Cover": "image"
        })
        print(f"\n✅ LingoClips Table Ready! ID: {table_id}")
        print("⚠️  Please add this ID to 'sources.yaml' as 'lingo_table_id' manually or via code.")
        
        # Determine if we should update config automaticallly? For safety, let's just print it.
        # But for agent convenience, we might want to know it.

if __name__ == "__main__":
    main()
