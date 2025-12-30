# YouTube Recent Videos Fetcher
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_IDS = os.getenv('CHANNEL_IDS').split(',')

# Build YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Calculate time 12 hours ago (YouTube API uses RFC 3339 format)
twelve_hours_ago = (datetime.utcnow() - timedelta(hours=12)).strftime('%Y-%m-%dT%H:%M:%SZ')

print(f"🔍 Searching for videos uploaded after: {twelve_hours_ago}\n")

recent_videos = []

# Fetch recent videos from each channel
for channel_id in CHANNEL_IDS:
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        publishedAfter=twelve_hours_ago,
        order='date',
        type='video',
        maxResults=5
    )
    response = request.execute()
    
    # Add videos to our list
    for item in response.get('items', []):
        video_info = {
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'video_id': item['id']['videoId'],
            'published': item['snippet']['publishedAt']
        }
        recent_videos.append(video_info)

# Display results
if recent_videos:
    print(f"✅ Found {len(recent_videos)} recent video(s):\n")
    for video in recent_videos:
        print(f"📺 {video['title']}")
        print(f"   Channel: {video['channel']}")
        print(f"   Link: https://youtube.com/watch?v={video['video_id']}")
        print(f"   Published: {video['published']}\n")
else:
    print("❌ No videos found in the last 12 hours from your channels.")