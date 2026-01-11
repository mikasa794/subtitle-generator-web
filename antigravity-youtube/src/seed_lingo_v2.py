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
    print("✨ Seeding LingoTube V2 Demo (Dual Subs + AI Notes)...")
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
    
    # Structured Transcript (JSON)
    # Simulating what the AI Pipeline would output
    transcript_structure = [
        {
            "start": 0, "end": 5,
            "text_source": "[Scene: Monica and Rachel's apartment. Everyone is sitting around.]",
            "text_target": "[场景：莫妮卡和瑞秋的公寓。大家都坐在周围。]",
            "notes": "Scene Setting (场景描述)"
        },
        {
            "start": 6, "end": 9,
            "text_source": "Rachel: (opening a present) Ooooh! I love it!",
            "text_target": "瑞秋：（拆开礼物）噢！我太喜欢了！",
            "notes": ""
        },
        {
            "start": 9, "end": 14,
            "text_source": "It's a... fancy... metal... thing!",
            "text_target": "这是个... 花哨的... 金属... 东西！",
            "notes": "Rachel 显然没认出这是什么，她在努力编造。"
        },
        {
            "start": 15, "end": 18,
            "text_source": "Joey: It's a ladle! You know, for scooping soup or punch.",
            "text_target": "乔伊：这是个汤勺（Ladle）！你知道的，用来舀汤或者果汁潘趣酒。",
            "notes": "**Ladle**: (n) 长柄大汤勺。\n**Scoop**: (v) 舀取。"
        },
        {
            "start": 19, "end": 22,
            "text_source": "Rachel: Oh, Joey, that is so sweet!",
            "text_target": "瑞秋：噢，乔伊，你太贴心了！",
            "notes": "**Sweet**: 在这里形容人很体贴、很暖心。"
        },
        {
            "start": 23, "end": 28,
            "text_source": "Joey: Yeah, well, I figured you invite people over a lot, you serve soup, you need a ladle.",
            "text_target": "乔伊：是啊，我想着你经常请人来做客，你会招待汤，所以你需要个汤勺。",
            "notes": "**I figured**: 口语常用，“我寻思着”、“我推测”。"
        },
        {
            "start": 29, "end": 33,
            "text_source": "Chandler: (sarcastic) You know what? I think I'll get you a ladle for your birthday.",
            "text_target": "钱德勒：（讽刺地）你知道吗？我觉得你过生日我也送你个汤勺好了。",
            "notes": "Chandler 经典的讽刺 (Sarcasm)。暗示这个礼物很糟糕。"
        }
    ]
    
    # Dump to JSON string
    transcript_json_str = json.dumps(transcript_structure, ensure_ascii=False, indent=2)
    
    record = {
        "Title": "Friends: Joey's Bad Birthday Gift (Dual-Sub V2)",
        "Series": "Friends",
        "Target Language": "English",
        "Video URL": {"text": "Watch", "link": video_url},
        "Transcript": transcript_json_str,
        "Difficulty": "Beginner",
        "Status": "Done",
        "AI Notes": "本片段包含大量生活口语。重点词汇：Ladle (汤勺), Figured (认为/推测)."
    }

    headers = {"Authorization": f"Bearer {tenant_token}", "Content-Type": "application/json"}
    res = requests.post(
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records", 
        headers=headers, 
        json={"fields": record}
    )
    
    if res.status_code == 200:
        print("✅ V2 Demo Clip Seeded Successfully!")
        print("   This record contains structured JSON in the Transcript field.")
    else:
        print(f"❌ Seed failed: {res.text}")

if __name__ == "__main__":
    main()
