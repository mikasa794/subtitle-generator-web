import yaml
import requests
import json

def load_config():
    with open('config/sources.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def test_create_record():
    config = load_config()
    api_keys = config['api_keys']
    
    app_id = api_keys['feishu_app_id']
    app_secret = api_keys['feishu_app_secret']
    # Hardcode for safety during debug
    base_token = "FCnWb734NawZW6spPVvcMjtonjf"
    table_id = "tblZh4KDjOUZnpod"

    print(f"App ID: {app_id}") 
    print("Getting Tenant Token...")
    # 1. Get Token
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": app_id, "app_secret": app_secret})
    token = resp.json().get("tenant_access_token")
    if not token:
        print("Failed to get token")
        return

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # 2. Try Create Record
    print(f"Creating Record in Table: {table_id} (Base: {base_token})")
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/records"
    
    # Minimal record - JUST TITLE
    record = {
        "Title": "MINIMAL TEST RECORD",
    }
    
    resp = requests.post(url, headers=headers, json={"fields": record})
    
    print(f"HTTP Status: {resp.status_code}")
    print(f"Response Body: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")

if __name__ == "__main__":
    test_create_record()
