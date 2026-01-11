from youtube_transcript_api import YouTubeTranscriptApi
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def fetch():
    video_id = "221F55VPp2M"
    try:
        # Based on inspection, 'list' seems to be the method name for list_transcripts
        print(f"Trying YouTubeTranscriptApi.list({video_id})...")
        listing = YouTubeTranscriptApi.list_transcripts(video_id) 
        # Wait, the library usually exposes list_transcripts. 
        # If 'list' is in dir(), maybe it IS list_transcripts.
        # But let's try calling it.
        
        t = listing.find_transcript(['en'])
        data = t.fetch()
        
        print("Success!")
        for line in data[:5]:
             print(f"- {line['start']}: {line['text']}")
             
        with open("final_transcript.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
            
    except AttributeError:
        # Fallback if list_transcripts is not found but 'list' is
        try:
             print("Fallback: calling YouTubeTranscriptApi.list...")
             # This assumes an older or modified version
             data = YouTubeTranscriptApi.get_transcript(video_id)
             print("Success (get_transcript)!")
             for line in data[:5]:
                 print(f"- {line['start']}: {line['text']}")
        except Exception as e:
            print(f"Fallback Error: {e}")
            
    except Exception as e:
        print(f"Primary Error: {e}")

if __name__ == "__main__":
    fetch()
