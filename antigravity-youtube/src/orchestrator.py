import argparse
import sys
import os
import subprocess
import logging
from fetcher import YouTubeFetcher
from source_manager import SourceManager
from archiver import ContentArchiver
from feishu_sync import FeishuSync
from datetime import datetime

# Config logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')
ARCHIVE_DIR = os.path.join(BASE_DIR, 'archives')

import re
import io

# Force UTF-8 for Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        # For older python versions or weird environments
        pass
# ... (imports)

def parse_ai_output(content):
    """
    Parses the XML-like output from the AI rewriter.
    Returns a dictionary with keys matching Feishu fields.
    """
    data = {}
    
    # Clean content: Remove markdown code blocks if present
    # This handles ```xml ... ``` or just ``` ... ```
    clean_content = re.sub(r'^```\w*\s*', '', content.strip(), flags=re.MULTILINE)
    clean_content = re.sub(r'```$', '', clean_content.strip(), flags=re.MULTILINE)
    
    # Helper to extract content between tags
    def extract(tag):
        pattern = f"<{tag}>(.*?)</{tag}>"
        match = re.search(pattern, clean_content, re.DOTALL)
        return match.group(1).strip() if match else ""

    data['Title'] = extract('title')
    data['Date'] = extract('date')
    data['Author'] = extract('author')
    
    tags_str = extract('tags')
    data['Tags'] = [t.strip() for t in tags_str.split(',') if t.strip()]
    
    data['Golden Quote'] = extract('quote')
    data['Summary'] = extract('summary')
    data['Creation Notes'] = extract('notes')
    
    return data

def process_url(url, manager, fetcher, archiver, feishu, force=False):
    logger.info(f"Processing URL: {url}")
    
    # 1. Fetch Info
    info = fetcher.get_video_info(url)
    if not info:
        logger.error("Failed to get video info.")
        return

    video_id = info['id']
    if manager.is_processed(video_id) and not force:
        logger.info(f"Video {video_id} already processed. Skipping.")
        return

    # 2. Fetch Transcript
    logger.info("Fetching transcript...")
    transcript = fetcher.get_transcript(video_id)
    if not transcript:
        logger.error("No transcript found.")
        return

    # 3. Archive Raw Data (Temp)
    temp_transcript_path = os.path.join(BASE_DIR, 'temp_transcript.txt')
    with open(temp_transcript_path, 'w', encoding='utf-8') as f:
        for item in transcript:
            f.write(item['text'] + " ") 

    # 4. Call AI Rewriter
    logger.info("Calling AI Rewriter (Node.js)...")
    rewritten_content = ""
    try:
        node_script = os.path.join(BASE_DIR, 'src', 'ai_rewriter.js')
        result = subprocess.run(
            ['node', node_script, temp_transcript_path],
            capture_output=True, text=True, encoding='utf-8'
        )
        if result.returncode != 0:
            logger.error(f"AI Rewriter failed: {result.stderr}")
            rewritten_content = "AI Rewrite Failed."
        else:
            rewritten_content = result.stdout
            
    except Exception as e:
        logger.error(f"Error calling Node script: {e}")
        rewritten_content = "AI Rewrite Error."
    
    # Cleanup temp
    if os.path.exists(temp_transcript_path):
        os.remove(temp_transcript_path)

    # 5. Archive Final
    logger.info("Archiving content...")
    folder_path = archiver.save_content({'metadata': info, 'transcript': transcript}, rewritten_content)
    logger.info(f"Saved to {folder_path}")

    # 6. Sync to Feishu
    logger.info("Syncing to Feishu...")
    
    # Parse AI Content
    parsed_data = parse_ai_output(rewritten_content)
    
    # VALIDATION CRITERIA
    # We insist on having at least a Title and a Summary to consider it a valid sync.
    # The 'Title' might fallback to YouTube title, but 'Summary' MUST come from AI.
    if not parsed_data.get('Summary') or len(parsed_data.get('Summary')) < 10:
        logger.error("VALIDATION FAILED: AI did not produce a valid Summary. Skipping Sync.")
        logger.error(f"Raw Output start: {rewritten_content[:200]}...")
        # Optionally mark as 'Error' in state or just leave for retry
        return 

    # Fallback/Merge with metadata
    record = {
        "Title": parsed_data.get('Title') or info['title'],
        "URL": {"text": url, "link": url},
        # Prioritize YouTube Metadata Date (YYYYMMDD) > AI Date > Fallback
        "Date": (lambda: int(datetime.strptime(info['upload_date'], '%Y%m%d').timestamp() * 1000) if info.get('upload_date') else (
            int(datetime.strptime(parsed_data.get('Date'), '%Y-%m-%d').timestamp() * 1000) if parsed_data.get('Date') and re.match(r'\d{4}-\d{2}-\d{2}', parsed_data.get('Date')) else 0
        ))(),
        "Author": parsed_data.get('Author') or info.get('channel', ''),
        "Tags": parsed_data.get('Tags', []), 
        "Golden Quote": parsed_data.get('Golden Quote', ''),
        "Summary": parsed_data.get('Summary', rewritten_content), 
        "Creation Notes": parsed_data.get('Creation Notes', ''),
        "Status": "Done"
    }

    # Prepare Cover
    cover_path = None
    for f in os.listdir(folder_path):
        if f.startswith('cover.'):
            cover_path = os.path.join(folder_path, f)
            break
    
    if cover_path:
        token = feishu.upload_image(cover_path)
        if token:
            record["Cover"] = [{"file_token": token}]

    if feishu.sync_to_bitable(record):
        logger.info("Feishu Sync Success")
    else:
        logger.warning("Feishu Sync Failed (Check configuration)")

    # 7. Update State
    manager.mark_processed(video_id)
    logger.info("Done.")

def main():
    parser = argparse.ArgumentParser(description="Daily Content Curation Workflow")
    parser.add_argument('--url', help="Process a single URL")
    parser.add_argument('--batch', action='store_true', help="Scan subscribed channels")
    parser.add_argument('--force', action='store_true', help="Process even if already done")
    parser.add_argument('--auto-approve', action='store_true', help="Automatically process all found videos without asking")
    parser.add_argument('--daemon', action='store_true', help="Run in background mode (checks every 4 hours)")
    args = parser.parse_args()

    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    fetcher = YouTubeFetcher()
    archiver = ContentArchiver(ARCHIVE_DIR)
    feishu = FeishuSync(manager.get_api_keys())

    if args.daemon:
        import time
        logger.info("🕵️‍♂️ DETECTIVE MODE ENABLED: Watching for new content every 4 hours...")
        while True:
            try:
                logger.info("\n⏰ Wake up! Checking for updates...")
                run_batch(manager, fetcher, archiver, feishu, force=args.force)
                logger.info("💤 Nothing new / Done. Sleeping for 4 hours.")
                time.sleep(4 * 3600) 
            except KeyboardInterrupt:
                logger.info("Stopping Daemon.")
                break
            except Exception as e:
                logger.error(f"Daemon crashed: {e}. Retrying in 1 hour.")
                time.sleep(3600)

    elif args.url:
        process_url(args.url, manager, fetcher, archiver, feishu, args.force)
    elif args.batch:
        run_batch(manager, fetcher, archiver, feishu, force=args.force)
    else:
        parser.print_help()

def run_batch(manager, fetcher, archiver, feishu, force=False):
    logger.info("Starting Batch Scan...")
    channels = manager.get_channels()
    candidates = []
    
    # 1. Scan Channels
    for ch in channels:
        logger.info(f"Scanning channel: {ch['name']}...")
        videos = fetcher.get_channel_latest_videos(ch['url'], limit=5) 
        for v in videos:
            if not manager.is_processed(v['id']):
                candidates.append(v)
    
    if not candidates:
        logger.info("No new videos found.")
        return

    # 2. Auto-Process All
    print(f"\nFound {len(candidates)} new videos:")
    for idx, v in enumerate(candidates):
        print(f"[{idx}] {v.get('title')} ({v.get('url')})")
    
    logger.info(f"Automatically processing...")
    
    # 3. Process
    for v in candidates:
        process_url(v['url'], manager, fetcher, archiver, feishu, force=force)

if __name__ == "__main__":
    main()
