from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json
from django.utils.safestring import mark_safe

DEVELOPER_KEY = "AIzaSyCbhETq3jLFBsnsp9f5OnIVCKpmzx8pxE8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query,maxResults):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=query,
    part="id,snippet",
    maxResults=maxResults,
    type='video',
    order='rating'
  ).execute()

  videos = []
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      video_details = {}
      video_details['id'] = search_result['id']['videoId']
      video_details['image_url'] = search_result['snippet']['thumbnails']['high']['url']
      video_details['title'] = search_result['snippet']['title']
      video_details['description'] = search_result['snippet']['description']
      video_details['publisher'] = search_result['snippet']['channelTitle']
      video_details['date_published'] = search_result['snippet']['publishedAt']
      videos.append(video_details)

  return videos