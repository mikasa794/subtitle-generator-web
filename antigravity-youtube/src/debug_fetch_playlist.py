from fetcher import YouTubeFetcher
import json
import sys

def test_playlist(url):
    fetcher = YouTubeFetcher()
    print(f"Fetching playlist info for: {url}")
    info = fetcher.get_playlist_info(url)
    
    if info:
        print(json.dumps(info, indent=2, ensure_ascii=False))
    else:
        print("Failed to fetch info.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python debug_fetch_playlist.py <url>")
    else:
        test_playlist(sys.argv[1])
