from youtube_transcript_api import YouTubeTranscriptApi
import sys
import json

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

def fetch_raw_transcript():
    video_id = "221F55VPp2M"
    try:
        print(f"Fetching lists for {video_id}...")
        # Try modern API
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Try to find English
        transcript = transcript_list.find_transcript(['en'])
        data = transcript.fetch()
        
        # Save
        with open("debug_transcript_raw.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            
        print("✅ Transcript fetched successfully (First 5 lines):")
        for line in data[:5]:
            print(f"- {line['start']:.1f}s: {line['text']}")
            
        print("\nSearching Content:")
        found_ladle = any("ladle" in line['text'].lower() for line in data)
        found_musical = any("musical" in line['text'].lower() for line in data)
        print(f"- Contains 'Ladle': {found_ladle}")
        print(f"- Contains 'Musical': {found_musical}")

        # If found Musical, print context
        if found_musical:
            print("\nContext for 'Musical':")
            for line in data:
                if "musical" in line['text'].lower():
                    print(f"- {line['start']:.1f}s: {line['text']}")

    except Exception as e:
        print(f"❌ Error fetching: {e}")

if __name__ == "__main__":
    fetch_raw_transcript()
