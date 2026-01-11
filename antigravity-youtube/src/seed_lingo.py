import os
import requests
import sys
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
    print("Seed Demo LingoClip... (Emoji removed for safety)")
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

    # Demo Content: Friends - Ross's Sandwich (My Sandwich!)
    # Video: https://www.youtube.com/watch?v=KeepItSimple (Using a placeholder or a real valid ID if known. 
    # Let's use a generic 'Friends Funny' ID or the one from search logs: 221F55VPp2M (Joey's gift))
    video_id = "221F55VPp2M" 
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    transcript = """[Scene: Monica and Rachel's, everyone is there.]
Rachel: (opening a present) Ooooh! I love it! It's a... fancy... metal... thing!
Joey: It's a ladle! You know, for scooping soup or punch.
Rachel: Oh, Joey, that is so sweet!
Joey: Yeah, well, I figured you invite people over a lot, you serve soup, you need a ladle.
Chandler: (sarcastic) You know what? I think I'll get you a ladle for your birthday.
Joey: I have a ladle. I have two ladles.
Ross: You have two ladles?
Joey: Yeah, one for soup and one for... you know, other scoopable things.
Monica: (laughing) Joey, you don't even cook!
Joey: I cook! I make... cereal. And toast.
Phoebe: You know, in my next life, I want to come back as a ladle.
Detailed Scene Breakdown:
1. Rachel receives a gift which turns out to be a ladle.
2. Joey explains the practical use of the ladle.
3. Chandler makes a sarcastic comment.
4. The group discusses Joey's cooking habits.
"""
    
    record = {
        "Title": "Friends: Joey's Bad Birthday Gift (Demo)",
        "Series": "Friends",
        "Target Language": "English",
        "Video URL": {"text": "Watch", "link": video_url},
        "Transcript": transcript,
        "Difficulty": "Beginner",
        "Status": "Done",
        "AI Notes": "Ladle: A large long-handled spoon with a cup-shaped bowl, used for serving soup.\nScoop: To pick up something with a scoop or spoon."
    }

    headers = {"Authorization": f"Bearer {tenant_token}", "Content-Type": "application/json"}
    res = requests.post(
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records", 
        headers=headers, 
        json={"fields": record}
    )
    
    if res.status_code == 200:
        print("✅ Demo Clip Seeded!")
    else:
        print(f"❌ Seed failed: {res.text}")

if __name__ == "__main__":
    main()
