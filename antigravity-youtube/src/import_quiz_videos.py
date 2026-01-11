import os
import sys

# Ensure src is in path
sys.path.append(os.path.join(os.path.dirname(__file__)))

from fetcher import YouTubeFetcher
from orchestrator import process_url, SourceManager
from archiver import ContentArchiver
from feishu_sync import FeishuSync
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO)

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_dir = os.path.join(base_dir, 'config')
    archive_dir = os.path.join(base_dir, 'archives')
    
    # Init Services
    manager = SourceManager(
        os.path.join(config_dir, 'sources.yaml'),
        os.path.join(config_dir, 'state.yaml')
    )
    fetcher = YouTubeFetcher()
    archiver = ContentArchiver(archive_dir)
    feishu = FeishuSync(manager.get_api_keys())
    
    # The 5 Videos from the Quiz
    quiz_videos = [
        "https://www.youtube.com/watch?v=zQUO39j_c_k", # Joey Food
        "https://www.youtube.com/watch?v=L_PWbnHABsM", # Pivot
        "https://www.youtube.com/watch?v=UPW3iSLPrPg", # Unagi
        "https://www.youtube.com/watch?v=lkbr5qnYSUU", # Split Bill
        "https://www.youtube.com/watch?v=JYqAWNVHBwo"  # My Eyes
    ]
    
    print(f"Starting Import of {len(quiz_videos)} Quiz Videos...")
    
    for i, url in enumerate(quiz_videos):
        print(f"\n--- Importing [{i+1}/{len(quiz_videos)}]: {url} ---")
        try:
            # force=True to ensure we process it even if state says checked
            process_url(url, manager, fetcher, archiver, feishu, force=True)
        except Exception as e:
            print(f"Error processing {url}: {e}")

if __name__ == "__main__":
    main()
