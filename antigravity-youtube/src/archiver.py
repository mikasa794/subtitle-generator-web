import os
import requests
import logging

logger = logging.getLogger(__name__)

class ContentArchiver:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def sanitize_filename(self, name):
        return "".join([c for c in name if c.isalpha() or c.isdigit() or c==' ' or c in '-_']).rstrip()

    def save_content(self, video_data, rewritten_content):
        """
        video_data: dict from fetcher (metadata, transcript)
        rewritten_content: str, AI output
        """
        metadata = video_data['metadata']
        transcript = video_data['transcript']
        
        # Create folder name: YYYYMMDD - Title
        folder_name = f"{metadata.get('upload_date', '00000000')} - {self.sanitize_filename(metadata['title'])}"
        folder_path = os.path.join(self.base_dir, folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        # Save Metadata
        with open(os.path.join(folder_path, 'metadata.md'), 'w', encoding='utf-8') as f:
            # Simple metadata dump, can be improved to be pretty
            f.write(f"# {metadata['title']}\n\n")
            f.write(f"**Channel**: {metadata['channel']}\n")
            f.write(f"**Date**: {metadata['upload_date']}\n")
            f.write(f"**URL**: {metadata['url']}\n")
            f.write(f"**ID**: {metadata['id']}\n")
        
        # Save Transcript
        with open(os.path.join(folder_path, 'transcript.md'), 'w', encoding='utf-8') as f:
            for item in transcript:
                # Format: [00:00:00] Text
                start = int(item['start'])
                m, s = divmod(start, 60)
                h, m = divmod(m, 60)
                timestamp = f"[{h:02d}:{m:02d}:{s:02d}]"
                f.write(f"{timestamp} {item['text']}\n")

        # Save Rewritten Content
        with open(os.path.join(folder_path, 'rewritten.md'), 'w', encoding='utf-8') as f:
            f.write(rewritten_content)

        # Download Cover
        cover_url = metadata.get('thumbnail')
        if cover_url:
            try:
                ext = 'jpg'
                if '.webp' in cover_url: ext = 'webp'
                response = requests.get(cover_url)
                if response.status_code == 200:
                    with open(os.path.join(folder_path, f'cover.{ext}'), 'wb') as f:
                        f.write(response.content)
            except Exception as e:
                logger.error(f"Failed to download cover: {e}")
                
        return folder_path
