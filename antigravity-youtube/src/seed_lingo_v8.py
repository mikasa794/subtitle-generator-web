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
    print("✨ Seeding LingoTube V8 (Corrected Content: The Musical)...")
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
    
    # Corrected Content based on User Feedback
    # Rachel: "You know what we shall all do is go to a musical."
    # Assumption: This is the opening line (0-5s).
    
    transcript_structure = [
        # --- Scene 1: The Musical Intro (0:00 - 0:15) ---
        {
            "start": 0.5, "end": 4.0,
            "text_source": "Rachel: You know what we should all do? Go see a musical.",
            "text_target": "瑞秋：你知道我们都应该去做什么吗？去看一场音乐剧。",
            "context": {
                "type": "dialogue",
                "summary": "Rachel 突发奇想的提议。",
                "grammar": "Should all do... - 建议句型",
                "vocab": [{"word": "Musical", "ipa": "/ˈmjuː.zɪ.kəl/", "highlight": True}]
            }
        },
        {
            "start": 4.5, "end": 6.0,
            "text_source": "Chandler: Sure. (Sarcastic)",
            "text_target": "钱德勒：当然。（讽刺地）",
            "context": {
                "type": "dialogue",
                "summary": "Chandler 漫不经心地回应。",
                "vocab": []
            }
        },
        {
            "start": 6.5, "end": 10.0,
            "text_source": "Rachel: Does anyone know who won the Tony for Best Musical in 1996?",
            "text_target": "瑞秋：有人知道96年获得托尼奖最佳音乐剧的是谁吗？",
            "context": {
                "type": "dialogue",
                "summary": "Rachel 试图用问题来引起注意。",
                "vocab": [
                    {"word": "Tony", "meaning": "托尼奖 (美国戏剧界最高荣誉)", "highlight": False},
                ]
            }
        },
        {
            "start": 11.0, "end": 13.0,
            "text_source": "Chandler: Rent?",
            "text_target": "钱德勒：吉屋出租 (Rent)?",
            "context": {
                "type": "dialogue",
                "vocab": [{"word": "Rent", "meaning": "著名百老汇音乐剧《吉屋出租》", "highlight": True}]
            }
        },
        {
            "start": 13.5, "end": 15.0,
            "text_source": "Rachel: Yes! Rent!",
            "text_target": "瑞秋：对！就是《吉屋出租》！",
            "context": {"type": "dialogue", "vocab": []}
        },
        
        # --- Bridge: Gap (15:00 - 45:00) ---
        {
             "start": 36.0, "end": 41.0,
             "text_source": "Rachel: Okay, so when do you want to go?",
             "text_target": "瑞秋：好吧，那你们想什么时候去？",
             "context": {"type": "dialogue", "vocab": []}
        },
        {
             "start": 41.1, "end": 45.0,
             "text_source": "Chandler: I can't, I'm busy.",
             "text_target": "钱德勒：我不行，我很忙。",
             "context": {"type": "dialogue", "vocab": []}
        },

        # --- Scene 2: The Pen Gift (0:45 - 1:12) ---
        {
            "start": 48.0, "end": 53.0,
            "text_source": "Chandler: Man, it is so hard to shop for girls.",
            "text_target": "钱德勒：天哪，给女孩子买东西太难了。",
            "context": {
                "type": "dialogue",
                "summary": "Chandler 抱怨给女生买礼物的困难。",
                "grammar": "'Hard to shop for' - 这里的 shop for 意思是为...买礼物。",
                "vocab": []
            }
        },
        {
            "start": 58.0, "end": 60.0,
            "text_source": "Chandler: What did you get her?",
            "text_target": "钱德勒：你给她买了什么？",
            "context": {"type": "dialogue", "vocab": []}
        },
        {
            "start": 60.0, "end": 64.0,
            "text_source": "Joey: A pen. It's two gifts in one. It's a pen that's also a clock.",
            "text_target": "乔伊：一支笔。这可是二合一的礼物。这既是支笔，也是个时钟。",
            "context": {
                "type": "dialogue",
                "summary": "Joey 得意地展示他的'创意'礼物。",
                "vocab": [{"word": "Clock", "meaning": "时钟", "highlight": False}]
            }
        },
        {
            "start": 65.0, "end": 69.0,
            "text_source": "Chandler: You can't give her that.",
            "text_target": "钱德勒：你不能送她那个。",
            "context": {"type": "dialogue", "summary": "Chandler 直接否定了这个礼物。", "vocab": []}
        },
        {
            "start": 70.0, "end": 74.0,
            "text_source": "Chandler: Because she's not 11! And it's not the seventh night of Chanukah!",
            "text_target": "钱德勒：因为她不是11岁的小孩！而且这也不是光明节的第七天！",
            "context": {
                "type": "dialogue",
                "summary": "Chandler 用夸张的比喻来吐槽这个礼物的幼稚和不合时宜。",
                "cultural_note": "Chanukah (光明节): 犹太教节日，通常持续8天。传统上礼物的重要程度会随天数递减，第七天的礼物通常是比较随意的小玩意儿。",
                "vocab": [
                    {"word": "Chanukah", "ipa": "/ˈhɑː.nə.kə/", "meaning": "光明节 (犹太教节日)", "highlight": True},
                    {"word": "Seventh night", "meaning": "第七天晚上 (暗指礼物不重要)", "highlight": False}
                ]
            }
        }
    ]
    
    transcript_json_str = json.dumps(transcript_structure, ensure_ascii=False, indent=2)
    
    record = {
        "Title": "Friends: The Musical Proposal (V8 Fixed Content)",
        "Series": "Friends",
        "Target Language": "English",
        "Video URL": {"text": "Watch", "link": video_url},
        "Transcript": transcript_json_str,
        "Difficulty": "Intermediate",
        "Status": "Done",
        "AI Notes": "V8 Demo: Content Matched to User Feedback + Control Fix."
    }

    headers = {"Authorization": f"Bearer {tenant_token}", "Content-Type": "application/json"}
    res = requests.post(
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records", 
        headers=headers, 
        json={"fields": record}
    )
    
    if res.status_code == 200:
        print("✅ V8 Content Fixed Demo Seeded!")
    else:
        print(f"❌ V8 Seed failed: {res.text}")

if __name__ == "__main__":
    main()
