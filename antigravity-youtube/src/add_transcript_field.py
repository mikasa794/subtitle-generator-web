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

def add_transcript_field():
    print("Initializing...")
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    feishu = FeishuSync(keys)
    tenant_token = feishu.get_tenant_access_token()
    
    app_token = keys.get('bitable_app_token')
    lessons_table_id = keys.get('lessons_table_id')
    
    if not app_token or not lessons_table_id:
        print("Error: Config missing app_token or lessons_table_id")
        return

    print(f"Adding 'Transcript' field to table {lessons_table_id}...")
    
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lessons_table_id}/fields"
    headers = {"Authorization": f"Bearer {tenant_token}", "Content-Type": "application/json"}
    
    # Type 1 = Text (Multi-line)
    data = {
        "field_name": "Transcript",
        "type": 1 
    }
    
    res = requests.post(url, headers=headers, json=data)
    if res.status_code == 200:
        print("✅ Success! Field 'Transcript' added.")
    else:
        err = res.json()
        if "already exists" in str(err) or "重复" in str(err):
            print("✅ Field 'Transcript' already exists.")
        else:
            print(f"❌ Failed: {res.text}")

if __name__ == "__main__":
    add_transcript_field()
