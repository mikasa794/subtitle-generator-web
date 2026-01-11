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
    print("✨ Seeding LingoTube V3 Demo (Deep Context + Overlay Subs)...")
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
    
    # Enhanced V3 Schema
    # Each item represents a subtitle line, but with a rich 'context' object
    transcript_structure = [
        {
            "start": 0, "end": 5.5,
            "text_source": "[Scene: Monica and Rachel's apartment. Everyone is sitting around.]",
            "text_target": "[场景：莫妮卡和瑞秋的公寓。大家都坐在周围。]",
            "context": {
                "type": "scene_setting",
                "summary": "这是情景喜剧的标准开场描述。",
                "vocab": []
            }
        },
        {
            "start": 6, "end": 8.5,
            "text_source": "Rachel: Ooooh! I love it!",
            "text_target": "瑞秋：噢！我太喜欢了！",
            "context": {
                "type": "dialogue",
                "summary": "Rachel 表现出夸张的惊喜（通常暗示她在掩饰）。",
                "grammar": "感叹句的使用。",
                "vocab": []
            }
        },
        {
            "start": 9, "end": 14,
            "text_source": "It's a... fancy... metal... thing!",
            "text_target": "这是个... 花哨的... 金属... 东西！",
            "context": {
                "type": "dialogue",
                "summary": "Rachel 根本不知道这是什么，只好描述外观。",
                "vocab": [
                    {"word": "Fancy", "meaning": "花哨的/高级的", "example": "It's a fancy restaurant."},
                    {"word": "thing", "meaning": "东西（当叫不出名字时常用）"}
                ]
            }
        },
        {
            "start": 15, "end": 18,
            "text_source": "Joey: It's a ladle! You know, for scooping soup or punch.",
            "text_target": "乔伊：这是个汤勺！你知道的，用来舀汤或者果汁潘趣酒。",
            "context": {
                "type": "dialogue",
                "summary": "Joey 解释礼物的用途，这对他来说是很实用的礼物。",
                "vocab": [
                    {"word": "Ladle", "meaning": "长柄大汤勺", "highlight": True},
                    {"word": "Scoop", "meaning": "舀取 (动作)"},
                    {"word": "Punch", "meaning": "潘趣酒 (派对常见饮料)"}
                ],
                "grammar": "'For scooping' - For + V-ing 表用途。"
            }
        },
        {
            "start": 23, "end": 28,
            "text_source": "Joey: I figured you invite people over a lot, you serve soup, you need a ladle.",
            "text_target": "乔伊：我寻思你经常请人来做客，你会招待汤，所以你需要个汤勺。",
            "context": {
                "type": "dialogue",
                "summary": "Joey 展示了他单纯直线的逻辑。",
                "vocab": [
                    {"word": "I figured", "meaning": "我寻思/我认为 (口语高频)", "highlight": True},
                    {"word": "Invite over", "meaning": "邀请某人来家里"}
                ],
                "cultural_note": "在西方文化中，送这种纯实用性的厨房用具给年轻女性过生日通常被认为是'直男'行为，不够浪漫或贴心。"
            }
        },
        {
            "start": 29, "end": 33,
            "text_source": "Chandler: You know what? I think I'll get you a ladle for your birthday.",
            "text_target": "钱德勒：你知道吗？我觉得你过生日我也送你个汤勺好了。",
            "context": {
                "type": "dialogue",
                "summary": "Chandler 的经典讽刺。",
                "grammar": "Sarcasm (讽刺修辞). 他显然不是真的要送，而是讽刺这是个烂礼物。",
                "vocab": [
                    {"word": "You know what?", "meaning": "你猜怎么着？(引起注意)"}
                ]
            }
        }
    ]
    
    transcript_json_str = json.dumps(transcript_structure, ensure_ascii=False, indent=2)
    
    record = {
        "Title": "Friends: The Ladle Incident (V3 Deep Context)",
        "Series": "Friends",
        "Target Language": "English",
        "Video URL": {"text": "Watch", "link": video_url},
        "Transcript": transcript_json_str,
        "Difficulty": "Intermediate",
        "Status": "Done",
        "AI Notes": "V3 Demo: Deep Context Mode Enabled."
    }

    headers = {"Authorization": f"Bearer {tenant_token}", "Content-Type": "application/json"}
    res = requests.post(
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records", 
        headers=headers, 
        json={"fields": record}
    )
    
    if res.status_code == 200:
        print("✅ V3 Deep Context Demo Seeded!")
    else:
        print(f"❌ V3 Seed failed: {res.text}")

if __name__ == "__main__":
    main()
