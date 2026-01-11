import os
import requests
import sys
import json
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

def main():
    target_id = "recv6B1UnqPPmK" # The record the user is looking at
    print(f"✨ Updating Record {target_id} with V8 Content...")
    
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    feishu = FeishuSync(keys)
    tenant_token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    lingo_table_id = keys.get('lingo_table_id')

    # Content from V8
    video_url = "https://www.youtube.com/watch?v=221F55VPp2M"
    transcript_structure = [
        {
            "start": 0.5, "end": 5.0,
            "text_source": "Rachel: You know what we shall all do is go to a musical.",
            "text_target": "瑞秋：你知道我们要去做什么吗？我们要去看一场音乐剧。",
            "context": {
                "type": "dialogue",
                "summary": "Rachel 提议大家一起去参加活动。",
                "vocab": [
                     {
                        "word": "Musical",
                        "ipa": "/ˈmjuː.zɪ.kəl/",
                        "pos": "n. (名词)",
                        "meaning": "音乐剧",
                        "definition_en": "A play or film in which singing and dancing play an essential part.",
                        "synonyms": ["Show", "Performance"],
                        "common_phrases": ["Broadway musical (百老汇音乐剧)"],
                        "highlight": True
                    }
                ],
                "grammar": "'What we shall all do is...' - A pseudo-cleft sentence used to emphasize the action."
            }
        },
        {
            "start": 6.0, "end": 10.0,
            "text_source": "[Chandler looks confused/annoyed]",
            "text_target": "[钱德勒看起来很困惑/恼火]",
            "context": {
                "type": "scene_description",
                "summary": "Chandler 对这个提议的典型反应。",
                "vocab": []
            }
        },
        {
            "start": 31.5, "end": 35.0,
            "text_source": "Joey: It's a ladle! You know, for scooping soup or punch.",
            "text_target": "乔伊：这是个汤勺！你知道的，用来舀汤或者果汁潘趣酒。",
             "context": {
                "type": "dialogue",
                "summary": "Joey 解释勺子的用途。",
                "grammar": "For scooping - For + Ving",
                "vocab": [
                    {
                        "word": "Ladle",
                        "ipa": "/ˈleɪ.dəl/",
                         "pos": "n.",
                         "meaning": "汤勺",
                         "highlight": True
                    }
                ]
            }
        }
    ]
    
    transcript_json_str = json.dumps(transcript_structure, ensure_ascii=False, indent=2)
    
    record = {
        "Title": "Friends: The Musical Proposal (V9 Fixed Record)",
        "Transcript": transcript_json_str,
        "AI Notes": "Updated specific record to match V8 content + Fixed Start."
    }

    headers = {"Authorization": f"Bearer {tenant_token}", "Content-Type": "application/json"}
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records/{target_id}"
    
    res = requests.put(
        url,
        headers=headers, 
        json={"fields": record}
    )
    
    if res.status_code == 200:
        print("✅ Record Updated Successfully!")
    else:
        print(f"❌ Update failed: {res.text}")

if __name__ == "__main__":
    main()
