import argparse
import os
import sys
from source_manager import SourceManager
from services.pipeline import LingoPipeline

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

def main():
    parser = argparse.ArgumentParser(description="LingoTube Magic Import")
    parser.add_argument('url', help="YouTube Video URL")
    parser.add_argument('--mode', type=str, default='import', choices=['import', 'playlist'], help="Mode: import or playlist")
    parser.add_argument('--lang', type=str, default='English', help="Target Language (English, Japanese)")
    args = parser.parse_args()

    # Load Config
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()

    # Run Pipeline
    pipeline = LingoPipeline(CONFIG_DIR, keys)
    
    if args.mode == 'playlist':
        from services.fetcher import YouTubeFetcher
        import json
        # Use existing fetcher
        info = pipeline.fetcher.get_playlist_info(args.url)
        if info:
            print(json.dumps(info, ensure_ascii=False))
        else:
            print(json.dumps({"error": "Failed to fetch playlist"}))
            sys.exit(1)
    else:
        pipeline.process(args.url, target_lang=args.lang)

if __name__ == "__main__":
    main()
