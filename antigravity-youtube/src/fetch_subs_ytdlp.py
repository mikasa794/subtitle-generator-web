import yt_dlp
import json
import sys
import os

# Force UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def fetch_subs():
    url = "https://www.youtube.com/watch?v=221F55VPp2M"
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'outtmpl': 'temp_subs',
        'quiet': False
    }

    try:
        print(f"Fetching subs for {url}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print("Download complete.")
            
        # Check for file
        # yt-dlp usually names it temp_subs.en.vtt
        expected_file = "temp_subs.en.vtt"
        if os.path.exists(expected_file):
             print(f"✅ Found {expected_file}")
             with open(expected_file, 'r', encoding='utf-8') as f:
                 lines = f.readlines()
                 print("First 20 lines of subtitle file:")
                 for line in lines[:20]:
                     print(line.strip())
        else:
            print("❌ Subtitle file not found. Check if video has English subs.")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    fetch_subs()
