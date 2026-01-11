import yt_dlp
import json

def fetch_subs():
    url = "https://www.youtube.com/watch?v=221F55VPp2M"
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'outtmpl': 'debug_subs_friends',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print("Done fetching subs.")

if __name__ == "__main__":
    fetch_subs()
