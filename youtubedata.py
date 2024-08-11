from youtube_transcript_api import YouTubeTranscriptApi

# Extract the video ID from the URL
VIDEO_ID = 'Wbm8twqnb4s'

# Fetch the transcript
transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)

# Save the transcript to a text file
with open('transcript.txt', 'w', encoding='utf-8') as f:
    for entry in transcript:
        f.write(f"{entry['start']} - {entry['duration']}: {entry['text']}\n")

print("Transcript saved to transcript.txt")
