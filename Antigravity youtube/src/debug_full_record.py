import yaml
import requests
import json
import os
import re
from datetime import datetime

def load_config():
    with open('config/sources.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def test_full_record():
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

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Simulate Parsed Data
    title = "DEBUG FULL RECORD TEST"
    # Date logic from orchestrator
    date_str = "2023-10-22"
    date_val = int(datetime.strptime(date_str, '%Y-%m-%d').timestamp() * 1000)
    
    tags = ["TagA", "TagB"] # Test if these auto-create
    
    record = {
        "Title": title,
        "Date": date_val,
        "Author": "DebugBot",
        "Tags": tags,
        "Summary": "Testing if tags break the record."
    }

    print(f"Creating Record in Table: {table_id}")
    print(f"Payload: {json.dumps(record, ensure_ascii=False)}")
    
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/records"
    
    resp = requests.post(url, headers=headers, json={"fields": record})
    
    print(f"HTTP Status: {resp.status_code}")
    print(f"Response Body: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")

if __name__ == "__main__":
    test_full_record()
