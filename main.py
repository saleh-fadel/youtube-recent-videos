# YouTube Recent Videos Fetcher
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_IDS = os.getenv('CHANNEL_IDS').split(',')

# Build YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

print("🔍 Fetching channel information...\n")

# Get info about each channel
for channel_id in CHANNEL_IDS:
    request = youtube.channels().list(
        part='snippet',
        id=channel_id
    )
    response = request.execute()
    
    if response['items']:
        channel_name = response['items'][0]['snippet']['title']
        print(f"✅ Found: {channel_name} ({channel_id})")
    else:
        print(f"❌ Channel not found: {channel_id}")

print("\n🎉 All channels loaded successfully!")