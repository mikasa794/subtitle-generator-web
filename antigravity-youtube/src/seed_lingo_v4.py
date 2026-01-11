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
    print("✨ Seeding LingoTube V4 Demo (Dictionary Quality Vocab)...")
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    feishu = FeishuSync(keys)
    tenant_token = feishu.get_tenant_access_token()
    app_token = keys.get('bitable_app_token')
    lingo_table_id = keys.get('lingo_table_id')

    if not app_token or not lingo_table_id:
        print("Error: Config missing app_token or lingo_table_id")
        return

    # Video: Friends - Joey's Bad Birthday Gift (221F55VPp2M)
    video_url = "https://www.youtube.com/watch?v=221F55VPp2M"
    
    # Enhanced V4 Schema with Dictionary Details
    transcript_structure = [
        {
            "start": 0, "end": 5.5,
            "text_source": "[Scene: Monica and Rachel's apartment. Everyone is sitting around.]",
            "text_target": "[场景：莫妮卡和瑞秋的公寓。大家围坐在一起。]",
            "context": {
                "type": "scene_setting",
                "summary": "标准的情景剧开场。",
                "vocab": []
            }
        },
        {
            "start": 15, "end": 18,
            "text_source": "Joey: It's a ladle! You know, for scooping soup or punch.",
            "text_target": "乔伊：这是个汤勺！你知道的，用来舀汤或者果汁潘趣酒。",
            "context": {
                "type": "dialogue",
                "summary": "Joey 认真地解释这个礼物的实用性。",
                "grammar": "'For scooping' - For + V-ing (动名词) 表示物品的功能或用途。",
                "vocab": [
                    {
                        "word": "Ladle",
                        "ipa": "/ˈleɪ.dəl/",
                        "pos": "n. (名词)",
                        "meaning": "长柄大汤勺",
                        "definition_en": "A large long-handled spoon with a cup-shaped bowl, used for serving soup, stew, or punch.",
                        "synonyms": ["Spoon", "Dipper"],
                        "common_phrases": ["Soup ladle (汤勺)", "Ladle out (舀出)"],
                        "highlight": True
                    },
                    {
                        "word": "Scoop",
                        "ipa": "/skuːp/",
                        "pos": "v. (动词)",
                        "meaning": "舀取；挖出",
                        "definition_en": "To pick up or move something with a scoop or a spoon.",
                        "synonyms": ["Dig", "Shovel"],
                        "common_phrases": ["Scoop up (抱起/铲起)", "The inside scoop (内幕消息)"],
                        "highlight": False
                    }
                ]
            }
        },
        {
            "start": 23, "end": 28,
            "text_source": "Joey: I figured you invite people over a lot, you serve soup, you need a ladle.",
            "text_target": "乔伊：我寻思你经常请人来做客，你会招待汤，所以你需要个汤勺。",
            "context": {
                "type": "dialogue",
                "summary": "Joey 展示了他单纯直线的逻辑思维。",
                "vocab": [
                    {
                        "word": "Figure",
                        "ipa": "/ˈfɪɡ.jər/",
                        "pos": "v. (动词)",
                        "meaning": "认为；推测 (口)",
                        "definition_en": "To expect, believe, or think that something will happen.",
                        "synonyms": ["Think", "Reckon", "Assume"],
                        "common_phrases": ["Go figure (你瞧瞧/真怪了)", "Figure out (弄明白)"],
                        "highlight": True
                    },
                     {
                        "word": "Invite over",
                        "ipa": "/ɪnˈvaɪt ˈəʊ.vər/",
                        "pos": "phrasal verb (短语动词)",
                        "meaning": "邀请(某人)来家里",
                        "definition_en": "To ask someone to come to your home.",
                        "synonyms": ["Have over", "Ask round"],
                        "common_phrases": [],
                        "highlight": False
                    }
                ],
                "cultural_note": "送礼文化：在西方，送这种纯实用性的厨房用具给年轻异性朋友（尤其是生日）通常被认为是'直男'行为 (clueless guy move)，显得不够用心或浪漫。"
            }
        }
    ]
    
    transcript_json_str = json.dumps(transcript_structure, ensure_ascii=False, indent=2)
    
    record = {
        "Title": "Friends: The Ladle Incident (V4 Dictionary Mode)",
        "Series": "Friends",
        "Target Language": "English",
        "Video URL": {"text": "Watch", "link": video_url},
        "Transcript": transcript_json_str,
        "Difficulty": "Intermediate",
        "Status": "Done",
        "AI Notes": "V4 Demo: Dictionary-Level Vocab Data."
    }

    headers = {"Authorization": f"Bearer {tenant_token}", "Content-Type": "application/json"}
    res = requests.post(
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records", 
        headers=headers, 
        json={"fields": record}
    )
    
    if res.status_code == 200:
        print("✅ V4 Dictionary Mode Demo Seeded!")
    else:
        print(f"❌ V4 Seed failed: {res.text}")

if __name__ == "__main__":
    main()
