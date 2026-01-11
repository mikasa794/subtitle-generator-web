import youtube_transcript_api
print("Version:", getattr(youtube_transcript_api, '__version__', 'unknown'))
print("Attributes:", dir(youtube_transcript_api))
try:
    from youtube_transcript_api import YouTubeTranscriptApi
    print("Class Attributes:", dir(YouTubeTranscriptApi))
except ImportError:
    print("Could not import class")
