import yaml
import requests
import json

def load_config():
    with open('config/sources.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def list_records():
    config = load_config()
    api_keys = config['api_keys']
    
    app_id = api_keys['feishu_app_id']
    app_secret = api_keys['feishu_app_secret']
    
    # Hardcode verified values
    base_token = "FCnWb734NawZW6spPVvcMjtonjf"
    table_id = "tblZh4KDjOUZnpod"

    print("Getting Tenant Token...")
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": app_id, "app_secret": app_secret})
    token = resp.json().get("tenant_access_token")
    if not token:
        print("Failed to get token")
        return

    headers = {"Authorization": f"Bearer {token}"}

    print(f"Listing Records from Table: {table_id}")
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/records"
    
    resp = requests.get(url, headers=headers)
    print(f"Status: {resp.status_code}")
    
    if resp.status_code == 200:
        data = resp.json()
        items = data.get('data', {}).get('items', [])
        print(f"Found {len(items)} records.")
        for item in items:
            fields = item['fields']
            print(f"- ID: {item['record_id']} | Title: {fields.get('Title')} | Date: {fields.get('Date')}")
    else:
        print(f"Error: {resp.text}")

if __name__ == "__main__":
    list_records()
