import requests
import logging

# User Token provided by you
USER_TOKEN = "u-cUZ5wnM.x6fGVKu1cOnG_7l462HAk4ihooEaYBqa2L0n"

def find_my_bases():
    print("Searching for your Bitable files...")
    
    token_to_check = "FCnWb734NawZW6spPVvcMjtonjf"
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{token_to_check}/tables"
    headers = {"Authorization": f"Bearer {token}"} # Use Tenant Token from earlier in the script!
    
    # Wait, the script at step 252+ was using "test_connection" with tenant token logic.
    # But I rewrote it in Step 327+ to be "find_my_bases" using USER_TOKEN.
    # I should use "debug_feishu.py" (which uses tenant token) not "find_token.py".
    
    # checking debug_feishu.py content...
    # Step 258 output shows it has "test_connection".
    # But I want to be sure it has the correct logic.
    # Let's just rewrite debug_feishu.py cleanly to list tables using config.
    pass
    
    try:
        print(f"Probing Token: {token_to_check} ...")
        resp = requests.get(url, headers=headers)
        print(f"Status: {resp.status_code}")
        print(f"Response: {resp.text}")
        
        data = resp.json()
        if data.get('code') == 0:
            print(">>> SUCCESS! The token is VALID and accessible by YOU. <<<")
            print(f"Name: {data.get('data', {}).get('app', {}).get('name')}")
        else:
            print(">>> ERROR: Token not accessible or invalid. <<<")
            
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    find_my_bases()
