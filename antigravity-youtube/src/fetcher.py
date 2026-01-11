import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class YouTubeFetcher:
    def __init__(self):
        self.ydl_opts = {
            'quiet': True,
            'extract_flat': True, # Don't download yet, just get info
            'force_generic_extractor': False,
        }

    def get_playlist_info(self, url):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Check if it's a playlist
                if info.get('_type') == 'playlist' or 'entries' in info:
                    logger.info(f"Found Playlist: {info.get('title')}")
                    videos = []
                    for entry in info.get('entries', []):
                        if entry: # entry might be None if deleted
                            videos.append({
                                'title': entry.get('title'),
                                'id': entry.get('id'),
                                'url': entry.get('url') or f"https://www.youtube.com/watch?v={entry.get('id')}",
                                'duration': entry.get('duration')
                            })
                    return {
                        'type': 'playlist',
                        'title': info.get('title'),
                        'id': info.get('id'),
                        'videos': videos
                    }
                else:
                    # Single video
                    return {
                        'type': 'video', 
                        'video': self.get_video_info(url) # Reuse logic, but careful about recursion if get_video_info calls this? No.
                    }
        except Exception as e:
            logger.error(f"Error fetching playlist for {url}: {e}")
            return None

    def get_video_info(self, url):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title'),
                    'upload_date': info.get('upload_date'), # YYYYMMDD
                    'thumbnail': info.get('thumbnail'),
                    'description': info.get('description'),
                    'channel': info.get('channel'),
                    'duration': info.get('duration'),
                    'url': url,
                    'id': info.get('id')
                }
        except Exception as e:
            logger.error(f"Error fetching metadata for {url}: {e}")
            return None

    def get_transcript(self, video_id):
        try:
            # Instantiate the API
            api = YouTubeTranscriptApi()
            
            # List transcripts
            transcript_list = api.list(video_id)
            
            # Try to fetch Chinese manually created, then Chinese generated, then English
            transcript_obj = None
            try:
                transcript_obj = transcript_list.find_transcript(['zh-Hans', 'zh-Hant', 'zh'])
            except NoTranscriptFound:
                try:
                    transcript_obj = transcript_list.find_generated_transcript(['zh-Hans', 'zh-Hant', 'zh'])
                except NoTranscriptFound:
                    try:
                        transcript_obj = transcript_list.find_transcript(['en'])
                    except NoTranscriptFound:
                         return None

            fetched = transcript_obj.fetch()
            
            # Convert FetchedTranscript/Snippets to list of dicts
            # Expecting fetched to be FetchedTranscript object with .snippets
            # or maybe it's iterable?
            # Based on debug output: FetchedTranscript(snippets=[...])
            if hasattr(fetched, 'snippets'):
                return [{'text': s.text, 'start': s.start, 'duration': s.duration} for s in fetched.snippets]
            
            # Fallback if it is a list (standard version)
            return fetched

        except Exception as e:
            logger.error(f"Error fetching transcript for {video_id}: {e}")
            return None

    def fetch(self, url):
        info = self.get_video_info(url)
        if not info:
            return None
        
        transcript = self.get_transcript(info['id'])
        if not transcript:
            logger.warning(f"No transcript found for {url}")
            
        return {
            'metadata': info,
            'transcript': transcript
        }

    def get_channel_latest_videos(self, channel_url, limit=5):
        try:
            # Append /videos to ensure we fetch the videos tab, avoiding mix of Shorts/Live/Tabs
            target_url = channel_url.rstrip('/') + '/videos'
            
            opts = self.ydl_opts.copy()
            opts['extract_flat'] = True
            opts['playlistend'] = limit
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                result = ydl.extract_info(target_url, download=False)
                if 'entries' in result:
                    # sometimes entries can be playlists (tabs), filter for videos
                    videos = []
                    for entry in result['entries']:
                        # Ensure it has a video title and id, and ignores playlists
                        if entry.get('_type') == 'playlist': continue
                        if entry.get('ie_key') == 'YoutubeTab': continue 
                        videos.append(entry)
                    return videos
                return []
        except Exception as e:
            logger.error(f"Error fetching channel videos: {e}")
            return []
