import requests
import json
import os
import sys
from source_manager import SourceManager

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

def main():
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    api_key = keys.get('groq_api_key')
    
    url = "https://api.groq.com/openai/v1/models"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        models = res.json()['data']
        print("Available Models:")
        for m in models:
            print(f"- {m['id']}")
    else:
        print(f"Error: {res.text}")

if __name__ == "__main__":
    main()
