import argparse
import os
import yaml
import csv
import subprocess
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CONFIG_Path = os.path.join(os.path.dirname(__file__), '../config/sources.yaml')

def load_config():
    if not os.path.exists(CONFIG_Path):
        return {'channels': []}
    with open(CONFIG_Path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {'channels': []}

def save_config(config):
    with open(CONFIG_Path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)

def import_from_csv(csv_path):
    new_channels = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Takeout format usually: "Channel Id","Channel Url","Channel Title"
                url = row.get('Channel Url')
                name = row.get('Channel Title')
                if url and name:
                    new_channels.append({'name': name, 'url': url, 'enable': True})
    except Exception as e:
        logger.error(f"CSV Parse Error: {e}")
    return new_channels

def import_from_cookies(browser='chrome'):
    logger.info(f"Attempting to fetch subscriptions using {browser} cookies via yt-dlp...")
    logger.info("NOTE: Please ensure your browser is CLOSED before running this, or it may fail (database lock).")
    
    # We use yt-dlp to dump the subscription feed
    # https://www.youtube.com/feed/channels
    # https://www.youtube.com/feed/channels
    # Use python -m yt_dlp to ensure we find it if installed via pip
    cmd = [
        'python', '-m', 'yt_dlp',
        '--cookies-from-browser', browser,
        '--flat-playlist',
        '--dump-json',
        'https://www.youtube.com/feed/channels'
    ]
    
    new_channels = []
    try:
        # This might return lines of JSON objects
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode != 0:
            logger.error(f"yt-dlp failed: {result.stderr}")
            return []

        for line in result.stdout.strip().split('\n'):
            if not line: continue
            try:
                data = json.loads(line)
                # yt-dlp dump of a channel entry in the feed
                url = data.get('url') or data.get('original_url')
                title = data.get('title') or data.get('channel')
                if url and title:
                    new_channels.append({'name': title, 'url': url, 'enable': True})
            except:
                pass
                
    except Exception as e:
        logger.error(f"Cookie Import Error: {e}")
        
    return new_channels

def merge_channels(existing, new_items):
    # Create simple map to avoid dupes
    existing_map = {c['url']: c for c in existing}
    added_count = 0
    
    for item in new_items:
        if item['url'] not in existing_map:
            existing.append(item)
            existing_map[item['url']] = item
            added_count += 1
            
    return existing, added_count

def main():
    parser = argparse.ArgumentParser(description="Import YouTube Subscriptions")
    parser.add_argument('--csv', help="Path to Google Takeout subscriptions.csv")
    parser.add_argument('--browser', default='chrome', help="Browser to extract cookies from (chrome, firefox, edge)")
    parser.add_argument('--use-cookies', action='store_true', help="Try to import directly using browser cookies")
    parser.add_argument('--cookies-file', help="Path to Netscape formatted cookies.txt file")
    
    args = parser.parse_args()
    
    config = load_config()
    current_channels = config.get('channels', [])
    if current_channels is None: current_channels = []
    
    imported_channels = []
    
    if args.csv:
        imported_channels = import_from_csv(args.csv)
    elif args.cookies_file:
        # Use cookies.txt
        logger.info(f"Using cookies file: {args.cookies_file}")
        cmd = [
            'python', '-m', 'yt_dlp',
            '--cookies', args.cookies_file,
            '--flat-playlist',
            '--dump-json',
            'https://www.youtube.com/feed/channels'
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
            if result.returncode != 0:
                logger.error(f"yt-dlp failed: {result.stderr}")
            else:
                for line in result.stdout.strip().split('\n'):
                    if not line: continue
                    try:
                        data = json.loads(line)
                        url = data.get('url') or data.get('original_url')
                        title = data.get('title') or data.get('channel')
                        if url and title:
                            imported_channels.append({'name': title, 'url': url, 'enable': True})
                    except:
                        pass
        except Exception as e:
            logger.error(f"Cookies File Import Error: {e}")

    elif args.use_cookies:
        imported_channels = import_from_cookies(args.browser)
    else:
        print("Please specify --use-cookies, --cookies-file <path>, or --csv <path>")
        return

    print(f"Found {len(imported_channels)} channels to import.")
    
    if imported_channels:
        current_channels, added = merge_channels(current_channels, imported_channels)
        config['channels'] = current_channels
        save_config(config)
        print(f"Successfully added {added} new channels to sources.yaml")
    else:
        print("No channels found.")

if __name__ == "__main__":
    main()
