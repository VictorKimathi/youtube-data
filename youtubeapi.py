import requests
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Constants
API_KEY = os.getenv('YOUTUBE_API_KEY')  # Fetch the API key from environment variables
VIDEO_ID = 'Wbm8twqnb4s'

# Fetch the video title using YouTube Data API
def get_video_title(video_id, api_key):
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}'
    response = requests.get(url).json()
    return response['items'][0]['snippet']['title']

# Fetch the transcript
transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)

# Get the video title
title = get_video_title(VIDEO_ID, API_KEY)

# Save the title and transcript to a text file
with open('transcript.txt', 'w', encoding='utf-8') as f:
    f.write(f"Title: {title}\n\n")
    for entry in transcript:
        f.write(f"{entry['text']} ")

print("Transcript saved to transcript.txt")
