import yaml
import requests
import json
import logging

def load_config():
    with open('config/sources.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def list_tables():
    config = load_config()
    api_keys = config['api_keys']
    
    app_id = api_keys['feishu_app_id']
    app_secret = api_keys['feishu_app_secret']
    base_token = api_keys['bitable_app_token']

    print(f"App ID: {app_id}")
    print(f"Base Token: {base_token}")

    # 1. Get Tenant Token
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": app_id, "app_secret": app_secret})
    token = resp.json().get("tenant_access_token")
    
    if not token:
        print("Failed to get Tenant Token")
        return

    headers = {"Authorization": f"Bearer {token}"}

    # 2. List Fields
    table_id = "tblZh4KDjOUZnpod"
    print(f"Listing Fields for Table: {table_id} (Base: {base_token})")
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/fields"
    
    resp = requests.get(url, headers=headers)
    
    print(f"Status: {resp.status_code}")
    if resp.status_code == 200:
        data = resp.json()
        items = data.get('data', {}).get('items', [])
        if items:
            print(f"\n[SUCCESS] FOUND {len(items)} FIELDS:")
            for f in items:
                print(f"- Name: {f['field_name']} | Type: {f['type']}")
        else:
            print("\n[WARN] No fields found.")
    else:
        print(f"Error: {resp.text}")

if __name__ == "__main__":
    list_tables()
