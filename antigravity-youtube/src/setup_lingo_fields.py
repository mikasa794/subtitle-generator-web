import os
import requests
from source_manager import SourceManager

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

def load_config():
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    return manager.get_api_keys()

def get_tenant_access_token(app_id, app_secret):
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    res = requests.post(url, json={"app_id": app_id, "app_secret": app_secret})
    return res.json().get('tenant_access_token')

def create_field(app_token, table_id, field_name, field_type, token):
    url_create = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
    data = {"field_name": field_name, "type": field_type}
    res = requests.post(url_create, headers={"Authorization": f"Bearer {token}"}, json=data)
    if res.status_code == 200:
        print(f"✅ Created field '{field_name}'")
    else:
        print(f"❌ Failed to create field '{field_name}': {res.text}")

def main():
    config = load_config()
    app_id = config.get('feishu_app_id')
    app_secret = config.get('feishu_app_secret')
    app_token = config.get('bitable_app_token')
    lingo_table_id = config.get('lingo_table_id')

    if not all([app_id, app_secret, app_token, lingo_table_id]):
        print("Missing config.")
        return

    token = get_tenant_access_token(app_id, app_secret)
    print(f"Token: {token[:10]}...")

    # 1. List Fields
    url_list = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/fields"
    res = requests.get(url_list, headers={"Authorization": f"Bearer {token}"})
    if res.status_code != 200:
        print(f"Error listing fields: {res.text}")
        return

    fields = res.json().get('data', {}).get('items', [])
    field_names = [f['field_name'] for f in fields]
    print(f"Existing Fields: {field_names}")

    # Check for Transcript File
    if 'Transcript File' not in field_names:
        print("Creating field 'Transcript File'...")
        create_field(app_token, lingo_table_id, "Transcript File", 17, token)
    else:
        print("Field 'Transcript File' already exists.")

    # Check for Cover Image (Attachment) - Keeping it for internal use or future proxy
    if 'Cover Image' not in field_names:
        print("Creating field 'Cover Image'...")
        create_field(app_token, lingo_table_id, "Cover Image", 17, token)
    else:
        print("Field 'Cover Image' already exists.")

    # Check for Cover Image URL (Text) - For public display
    if 'Cover Image URL' not in field_names:
        print("Creating field 'Cover Image URL'...")
        create_field(app_token, lingo_table_id, "Cover Image URL", 1, token) # Type 1 = Text
    else:
        print("Field 'Cover Image URL' already exists.")
        
    print("✅ Schema Check Complete.")

if __name__ == "__main__":
    main()
