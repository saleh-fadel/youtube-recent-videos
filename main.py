# YouTube Recent Videos Fetcher
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env
load_dotenv()

# Get API key
API_KEY = os.getenv('YOUTUBE_API_KEY')

# Build YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Test: Get your channel's info (just to verify connection works)
request = youtube.channels().list(
    part='snippet',
    mine=True
)

print("🔍 Testing YouTube API connection...")
print(f"✅ API Key loaded: {API_KEY[:10]}..." if API_KEY else "❌ No API key found!")
print("✅ YouTube API client created successfully!")# YouTube Recent Videos Fetcher
