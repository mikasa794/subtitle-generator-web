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
    
    # Friends "The Ones That Make You Laugh" Playlist
    playlist_url = "https://www.youtube.com/playlist?list=PLvHE0mJ2lGe-cCRKDwG3ClBmOix69L8Pj"
    
    print("Fetching playlist info...")
    playlist_info = fetcher.get_playlist_info(playlist_url)
    
    if not playlist_info or 'videos' not in playlist_info:
        print("Failed to fetch playlist.")
        return

    videos = playlist_info['videos']
    print(f"Found {len(videos)} videos. Processing Top 5...")
    
    count = 0
    for v in videos:
        if count >= 5:
            break
            
        print(f"\n--- Importing [{count+1}/5]: {v['title']} ---")
        try:
            # force=True to ensure we process it even if state says checked
            process_url(v['url'], manager, fetcher, archiver, feishu, force=True)
            count += 1
        except Exception as e:
            print(f"Error processing {v['title']}: {e}")

if __name__ == "__main__":
    main()
