import os
import sys
import json
import logging
import requests
import yt_dlp
from source_manager import SourceManager

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# Force UTF-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def download_audio(video_url, output_path):
    """Downloads audio from YouTube video using yt-dlp."""
    logger.info(f"Downloading audio from {video_url}...")
    
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best', # Try to get m4a directly, or whatever is best
        'outtmpl': output_path + '.%(ext)s', # Keep original extension
        'quiet': True,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        
        # Find the file (we don't know the extension exactly now)
        # Check common extensions
        for ext in ['m4a', 'webm', 'mp3', 'mp4']:
             path = output_path + f".{ext}"
             if os.path.exists(path):
                 return path
        
        return None
        
    except Exception as e:
        logger.error(f"Download failed: {e}")
        return None

def transcribe_with_groq(audio_path, api_key):
    """Transcribes audio using Groq Whisper API."""
    logger.info("Transcribing with Groq Whisper...")
    
    url = "https://api.groq.com/openai/v1/audio/transcriptions"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    # Check file size (Groq limit is 25MB). Friends clip 2min is tiny, so fine.
    
    try:
        with open(audio_path, "rb") as file:
            files = {
                "file": (os.path.basename(audio_path), file, "audio/m4a")
            }
            data = {
                "model": "whisper-large-v3", # or distil-whisper-large-v3-en
                "response_format": "verbose_json", # Request verbose_json to get timestamps (segments)
                "temperature": "0",
                "language": "en"
            }
            
            response = requests.post(url, headers=headers, files=files, data=data)
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Groq API Error: {response.text}")
                return None
                
    except Exception as e:
        logger.error(f"Transcription failed: {e}")
        return None

def main():
    # 1. Load Config
    manager = SourceManager(
        os.path.join(CONFIG_DIR, 'sources.yaml'),
        os.path.join(CONFIG_DIR, 'state.yaml')
    )
    keys = manager.get_api_keys()
    groq_key = keys.get('groq_api_key')
    
    if not groq_key:
        logger.error("Groq API Key not found in config/sources.yaml")
        return

    # 2. Target Video (Friends Clip)
    video_url = "https://www.youtube.com/watch?v=221F55VPp2M"
    temp_audio_base = os.path.join(BASE_DIR, "temp_audio") # base name
    
    # 3. Download
    final_audio_path = download_audio(video_url, temp_audio_base)
    
    if not final_audio_path or not os.path.exists(final_audio_path):
        logger.error("Audio download failed.")
        return
        
    logger.info(f"Audio ready: {final_audio_path}")
    
    # 4. Transcribe
    result = transcribe_with_groq(final_audio_path, groq_key)
    
    if result:
        logger.info("✅ Transcription Success!")
        
        # Save Raw JSON
        with open("whisper_result.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
            
        # Print Preview
        print("\n--- Transcript Preview ---")
        segments = result.get('segments', [])
        for seg in segments[:5]:
            print(f"[{seg['start']:.2f}s - {seg['end']:.2f}s]: {seg['text']}")
            
    else:
        logger.error("Transcription failed.")
        
    # Cleanup
    # if os.path.exists(final_audio_path):
    #     os.remove(final_audio_path)

if __name__ == "__main__":
    main()
