import os
import sys
import json
import subprocess
import requests
import argparse
from source_manager import SourceManager
from feishu_sync import FeishuSync
from fetcher import YouTubeFetcher

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8 for Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def format_transcript(transcript_list):
    if not transcript_list:
        return ""
    lines = []
    for item in transcript_list:
        t = item.get('text', '').strip()
        if t:
            lines.append(t)
    return "\n".join(lines)

def search_clips(query, limit=5):
    print(f"🔍 Searching YouTube for: '{query}'...")
    try:
        # ytsearch{limit}
        cmd = [
            "python", "-m", "yt_dlp", 
            f"ytsearch{limit}:{query}", 
            "--print", "%(id)s", 
            "--print", "%(title)s",
            "--no-warnings"
        ]
        # res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        # Windows encoding fix: capture bytes and decode manually
        res = subprocess.run(cmd, capture_output=True)
        try:
            raw_out = res.stdout.decode('utf-8')
        except UnicodeDecodeError:
            raw_out = res.stdout.decode('gbk', errors='ignore')
            
        lines = raw_out.strip().split('\n')
        
        # Output is alternating ID, Title
        videos = []
        for i in range(0, len(lines)-1, 2):
            if i+1 < len(lines):
                videos.append({'id': lines[i].strip(), 'title': lines[i+1].strip()})
        return videos
    except Exception as e:
        print(f"Search error: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="LingoTube Clip Generator")
    parser.add_argument('series', help="Name of the series (e.g. Friends)")
    parser.add_argument('lang', help="Target Language (English, Japanese)")
    args = parser.parse_args()

    # 1. Init
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    
    feishu = FeishuSync(keys)
    fetcher = YouTubeFetcher()
    
    app_token = keys.get('bitable_app_token')
    lingo_table_id = keys.get('lingo_table_id')
    tenant_token = feishu.get_tenant_access_token()

    if not app_token or not lingo_table_id:
        print("Error: Config missing app_token or lingo_table_id")
        return

    # 2. Search
    # "Friends clips english subtitles" -> "Learn English with Friends clips"
    # This yields better educational content with reliable subs.
    search_query = f"Learn {args.lang} with {args.series} clips subtitles"
    if args.lang.lower() == 'japanese':
        search_query = f"Learn Japanese with {args.series} clips subtitles"

    candidates = search_clips(search_query, limit=10)
    print(f"Found {len(candidates)} candidates. Checking for transcripts...")

    success_count = 0
    headers = {"Authorization": f"Bearer {tenant_token}", "Content-Type": "application/json"}

    # from youtube_transcript_api import YouTubeTranscriptApi
    # We need to import it here or at top. It is available since fetcher uses it.
    from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

    for vid in candidates:
        video_id = vid['id']
        title = vid['title']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        
        print(f"\nProcessing: {title} ({video_id})")
        
        # Custom Transcript Logic for LingoTube
        transcript_text = ""
        try:
            # Fix: Instantiate APi as seen in fetcher.py
            api = YouTubeTranscriptApi()
            transcript_list = api.list_transcripts(video_id)
            
            # Wait, fetcher.py used api.list(video_id). Let's try to be safe and try both or check dir?
            # actually, if 'list_transcripts' failed on class, maybe it works on instance?
            # BUT fetcher.py uses `.list`. Let's assume `.list` is the method name in this version.
            # AND fetcher.py calls `.find_transcript` on the result.
            
            transcript_list_obj = api.list_transcripts(video_id) 
            
            # ...
            # Actually, let's just use what fetcher.py uses: `api.list(video_id)`
            # But wait, if api.list returns something that has .find_transcript, then it is a TranscriptList.
            
        except AttributeError:
             # Fallback if .list_transcripts doesn't exist on instance either
             try:
                 api = YouTubeTranscriptApi()
                 transcript_list_obj = api.list(video_id)
             except Exception:
                 print(f"   ❌ Transcript API method missing.")
                 continue
        except Exception as e:
            # If list_transcripts failed for other reason (e.g. video unavailable)
            print(f"   ❌ Transcript list error: {e}")
            continue

        try:
            # Priority: Manual Target -> Auto Target -> Manual English -> Auto English
            # args.lang is "English" or "Japanese"
            lang_code = 'en'
            if 'japan' in args.lang.lower(): lang_code = 'ja'
            elif 'chin' in args.lang.lower(): lang_code = 'zh'
            
            t_obj = None
            
            # Try to find target lang
            try:
                t_obj = transcript_list_obj.find_transcript([lang_code])
            except NoTranscriptFound:
                try:
                    t_obj = transcript_list_obj.find_generated_transcript([lang_code])
                except NoTranscriptFound:
                    pass
            
            if t_obj:
                fetched = t_obj.fetch()
                transcript_text = format_transcript(fetched)
                print(f"   ✅ Transcript acquired ({t_obj.language})!")
            else:
                 print(f"   ❌ No {args.lang} transcript found.")
                 continue

        except Exception as e:
            print(f"   ❌ Transcript processing error: {e}")
            # FALLBACK: Use yt-dlp CLI directly to download subs
            print("   ⚠️ Trying yt-dlp fallback...")
            try:
                # Defines output template to temp file
                temp_output = f"temp_{video_id}"
                # Download en or zh subs
                cmd = [
                    "python", "-m", "yt_dlp",
                    video_url,
                    "--skip-download",
                    "--write-auto-sub", 
                    "--write-sub",
                    "--sub-lang", "en,zh,ja",
                    "--output", temp_output,
                    "--no-warnings"
                ]
                subprocess.run(cmd, check=True)
                
                # Check for files
                import glob
                files = glob.glob(f"{temp_output}.*.vtt")
                if not files:
                    # try srt? yt-dlp default is vtt usually for auto
                    files = glob.glob(f"{temp_output}.*.srt")
                
                if files:
                    # Pick the best one (prefer non-auto if poss, but filename doesn't always tell explicit)
                    # Just pick first
                    fn = files[0]
                    print(f"   ✅ Downloaded sub file: {fn}")
                    
                    with open(fn, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Simple VTT cleaner
                    lines = content.split('\n')
                    clean_lines = []
                    seen = set()
                    for line in lines:
                        if '-->' in line: continue
                        if line.strip() == '': continue
                        if line.strip().isdigit(): continue # srt index
                        if line.startswith('WEBVTT'): continue
                        if line.startswith('Kind:'): continue
                        if line.startswith('Language:'): continue
                        
                        l = line.strip()
                        # Dedupe adjacent roughly
                        if l in seen: continue
                        clean_lines.append(l)
                        seen.add(l)
                    
                    transcript_text = "\n".join(clean_lines)
                    print("   ✅ Extracted text from VTT/SRT!")
                    
                    # Cleanup
                    for f in files:
                        try: os.remove(f)
                        except: pass
                else:
                    print("   ❌ yt-dlp failed to download any subs.")
                    continue

            except Exception as e2:
                print(f"   ❌ yt-dlp fallback error: {e2}")
                continue
        
        # Get extra info (thumbnail) via simple yt-dlp call
        info = fetcher.get_video_info(video_url)
        cover_url = info.get('thumbnail') if info else None
        
        # Save to Feishu
        record = {
            "Title": title,
            "Series": args.series,
            "Target Language": args.lang,
            "Video URL": {"text": "Watch", "link": video_url},
            "Transcript": transcript_text, 
            "Difficulty": "Intermediate",
            "Status": "Done",
        }
        
        # Try upload cover
        if cover_url:
             # Download first? feishu_sync.upload_image takes path.
             # Too complex for quick script. Let's skip cover upload for now unless we add code.
             pass

        res = requests.post(
            f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{lingo_table_id}/records", 
            headers=headers, 
            json={"fields": record}
        )
        
        if res.status_code == 200:
            print("   ✅ Saved to Feishu LingoClips!")
            success_count += 1
        else:
            print(f"   ❌ Save failed: {res.text}")
            
    print(f"\nDone! Generated {success_count} LingoClips.")

if __name__ == "__main__":
    main()
