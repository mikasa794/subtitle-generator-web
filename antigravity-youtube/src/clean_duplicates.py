import os
import requests
import json
from dotenv import load_dotenv

# Load env
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

# Hardcoded from feishu.ts
APP_ID = 'cli_a9c6a1bb56f89cd4'
APP_SECRET = 'Ox6v51RIbon1bbxaHmvUGhqRNnW3CiUs'
APP_TOKEN = 'FCnWb734NawZW6spPVvcMjtonjf'
LINGO_TABLE_ID = 'tblTEYjEp8ZtDwZZ'

class FeishuCleaner:
    def __init__(self):
        self.client = None 
        self.token = self._get_token()
        
    def _get_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        body = {
            "app_id": APP_ID,
            "app_secret": APP_SECRET
        }
        res = requests.post(url, json=body)
        return res.json().get('tenant_access_token')

    def clean_duplicates(self):
        print("🧹 Scanning for duplicates...")
        # 1. Fetch All
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{LINGO_TABLE_ID}/records"
        params = {"page_size": 100} # Assume < 100 for now
        res = requests.get(url, headers={"Authorization": f"Bearer {self.token}"}, params=params)
        data = res.json()
        if data.get('code') != 0:
            print(f"❌ API Error: {data}")
            return
            
        items = data['data']['items']
        
        # 2. Group by Title
        grouped = {}
        for item in items:
            title = item['fields'].get('Title', 'Untitled')
            if title not in grouped: grouped[title] = []
            grouped[title].append(item)
            
        # 3. Process
        for title, records in grouped.items():
            if len(records) > 1:
                print(f"\nFound {len(records)} versions of: {title}")
                # Sort by creation? Record ID is roughly chronological. 
                # Let's assume last in list is latest (Feishu default) or just keep the one with 'Cover Image URL' if others don't?
                # Actually, let's keep the one that has the RICH data we verified.
                # ID: recv7eBbgk4A5ze (The one we just made).
                
                # Simple Logic: Keep the LAST one created (assuming Feishu returns chrono).
                # To be consistant with debug script, last is latest.
                latest = records[-1]
                to_delete = records[:-1]
                
                print(f"   keeping: {latest['record_id']}")
                
                for r in to_delete:
                    print(f"   ❌ Deleting: {r['record_id']}")
                    self._delete_record(r['record_id'])
            else:
                print(f"✅ Unique: {title}")

    def _delete_record(self, rid):
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{LINGO_TABLE_ID}/records/{rid}"
        res = requests.delete(url, headers={"Authorization": f"Bearer {self.token}"})
        if res.status_code == 200:
            print("      Deleted.")
        else:
            print(f"      Failed: {res.text}")

if __name__ == "__main__":
    cleaner = FeishuCleaner()
    cleaner.clean_duplicates()
