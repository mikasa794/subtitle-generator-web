import os
import json
import logging
import subprocess
import requests
import math
import shutil
import glob

# Dynamic FFmpeg setup
try:
    import static_ffmpeg
    static_ffmpeg.add_paths()
except ImportError:
    pass

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WhisperService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.temp_dir = os.path.join(self.base_dir, "temp_audio")
        
        # FIX: Robust directory creation (Handle ReparsePoints/Files blocking dir)
        try:
            os.makedirs(self.temp_dir, exist_ok=True)
        except OSError:
            logger.warning(f"Could not create dir {self.temp_dir}, trying to delete and recreate...")
            try:
                if os.path.isdir(self.temp_dir) and not os.path.islink(self.temp_dir):
                    shutil.rmtree(self.temp_dir)
                else:
                    os.remove(self.temp_dir) # Handles files and links
                os.makedirs(self.temp_dir, exist_ok=True)
            except Exception as e:
                logger.error(f"Critical Error: Cannot create temp directory {self.temp_dir}: {e}")
                raise

    def download_audio(self, video_url):
        """Downloads audio from YouTube using yt-dlp."""
        try:
            filename = "temp_audio_course" # Let yt-dlp append extension
            # But we want to construct full path prefix
            output_template = os.path.join(self.temp_dir, filename + ".%(ext)s")
            
            # Clean up old files
            for ext in ['.m4a', '.webm', '.mp3']:
                old_path = os.path.join(self.temp_dir, filename + ext)
                if os.path.exists(old_path):
                    try: os.remove(old_path)
                    except: pass

            logger.info(f"Downloading audio from {video_url}...")
            
            # Try to get format 139 (48kbps AAC) which is ~22MB/hour and doesn't need ffmpeg conversion
            # If not available, fallback to worst audio
            cmd = [
                "python", "-m", "yt_dlp",
                "-f", "139/249/worst[ext=m4a]/worst",
                "--output", output_template,
                "--no-check-certificate", 
                "--no-warnings",
                video_url
            ]
            
            subprocess.run(cmd, check=True)
            
            # Find the result file
            # Since we don't know the extension for sure, we look for it
            final_path = None
            for ext in ['.m4a', '.webm', '.mp4']:
                p = os.path.join(self.temp_dir, filename + ext)
                if os.path.exists(p):
                    final_path = p
                    break
            
            if not final_path:
                 raise Exception("Download finished but file missing.")
                 
            # Check size
            size_mb = os.path.getsize(final_path) / (1024 * 1024)
            logger.info(f"Downloaded file: {final_path} Size: {size_mb:.2f} MB")
            
            # Check for empty file
            if size_mb == 0:
                 raise Exception("Downloaded file is empty (0 bytes).")
                
            return final_path
        except Exception as e:
            logger.error(f"Download failed: {e}")
            return None

    def transcribe(self, audio_path):
        """Transcribes audio using Groq Whisper API, handling large files by splitting using ffmpeg."""
        if not audio_path:
            return None

        file_size_mb = os.path.getsize(audio_path) / (1024 * 1024)
        
        if file_size_mb <= 25:
             logger.info(f"File size {file_size_mb:.2f}MB is within limit. Transcribing directly...")
             return self._transcribe_chunk(audio_path)
        
        logger.info(f"File size {file_size_mb:.2f}MB > 25MB. Splitting into chunks with ffmpeg...")
        
        try:
            # Clean up previous chunks
            for f in glob.glob(os.path.join(self.temp_dir, "temp_chunk_*.m4a")):
                try: os.remove(f)
                except: pass

            timestamp_pattern = os.path.join(self.temp_dir, "temp_chunk_%03d.m4a")
            
            # ffmpeg command to split: 10 mins (600s) segments, copy codec (fast)
            cmd = [
                "ffmpeg", "-i", audio_path,
                "-f", "segment",
                "-segment_time", "600",
                "-c", "copy",
                "-y", # overwrite
                timestamp_pattern
            ]
            
            # Check if webm (needs transcoding if we want m4a, or just copy webm)
            # If source is m4a (from our yt-dlp call), copy works.
            # If source is webm, copy might produce segmented webm.
            if audio_path.endswith('.webm'):
                 cmd[-1] = os.path.join(self.temp_dir, "temp_chunk_%03d.webm")
            
            logger.info(f"Running ffmpeg split: {' '.join(cmd)}")
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Find generated chunks
            chunks = sorted(glob.glob(os.path.join(self.temp_dir, "temp_chunk_*")))
            logger.info(f"Split into {len(chunks)} chunks.")
            
            if not chunks:
                logger.error("FFmpeg split produced no files.")
                return None

            full_transcript = {'text': "", 'segments': []}
            
            for i, chunk_path in enumerate(chunks):
                logger.info(f"Transcribing chunk {i+1}/{len(chunks)}: {os.path.basename(chunk_path)}...")
                chunk_result = self._transcribe_chunk(chunk_path)
                
                if not chunk_result:
                    logger.error(f"Failed to transcribe chunk {i+1}. Aborting and return partial if available.")
                    # Return partial or None? Let's return None for robustness/retry logic outside
                    # But maybe partial is better than nothing?
                    # Let's keep strict.
                    return None
                
                # Merge logic
                full_transcript['text'] += " " + chunk_result.get('text', "")
                
                # Calculate offset based on segment index * 600s
                # Note: 'segment' filter is approximate but reliable enough for subtitles if we trust the order
                time_offset = i * 600.0
                for segment in chunk_result.get('segments', []):
                    segment['start'] += time_offset
                    segment['end'] += time_offset
                    full_transcript['segments'].append(segment)
                
                # Cleanup
                try: os.remove(chunk_path)
                except: pass
            
            return full_transcript
            
        except Exception as e:
            logger.error(f"Splitting/Transcription failed: {e}")
            return None

    def _transcribe_chunk(self, audio_path):
        """Internal method to transcribe a single file chunk with retry logic."""
        url = "https://api.groq.com/openai/v1/audio/transcriptions"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        max_retries = 3
        import time
        
        for attempt in range(max_retries):
            try:
                with open(audio_path, "rb") as file:
                    files = {
                        "file": (os.path.basename(audio_path), file, "audio/m4a"),
                        "model": (None, "whisper-large-v3"),
                        "response_format": (None, "verbose_json"),
                        "language": (None, "en") 
                    }
                    
                    if audio_path.endswith('.webm'):
                        files["file"] = (os.path.basename(audio_path), file, "audio/webm")
                    
                    response = requests.post(url, headers=headers, files=files)
                    
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 429:
                    logger.warning(f"Rate limit hit (429) for chunk. Retrying in 60s (Attempt {attempt+1}/{max_retries})...")
                    time.sleep(60)
                elif response.status_code >= 500:
                    logger.warning(f"Server error {response.status_code}. Retrying in 10s (Attempt {attempt+1}/{max_retries})...")
                    time.sleep(10)
                else:
                    logger.error(f"Whisper API Error {response.status_code}: {response.text}")
                    return None
            except Exception as e:
                logger.error(f"Chunk transcription failed: {e}")
                time.sleep(5)
                
        logger.error("Max retries reached for chunk.")
        return None

    def format_transcript_simple(self, whisper_json):
        """Formats Whisper JSON into simple string or list for Course Player."""
        if not whisper_json or 'segments' not in whisper_json:
            return ""
            
        lines = []
        for seg in whisper_json['segments']:
            start = seg['start']
            text = seg['text'].strip()
            # Format: [00:12] Hello world
            minutes = int(start // 60)
            seconds = int(start % 60)
            timestamp = f"[{minutes:02d}:{seconds:02d}]"
            lines.append(f"{timestamp} {text}")
            
        return "\n".join(lines)
