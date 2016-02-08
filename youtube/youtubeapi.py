from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCbhETq3jLFBsnsp9f5OnIVCKpmzx8pxE8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  print '\n\n\n',options.q,'\n\n'
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []

  # print search_response.get('items',[]),'Search Response'

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      video_details = {}
      video_details['id'] = search_result['id']['videoId']
      video_details['title'] = search_result['snippet']['title']
      video_details['description'] = search_result['snippet']['description']
      video_details['publisher'] = search_result['snippet']['channelTitle']
      video_details['date_published'] = search_result['snippet']['publishedAt']
      videos.append(video_details)

  print videos
  # print "Videos:\n", "\n".join(videos), "\n"
  # print "Channels:\n", "\n".join(channels), "\n"
  # print "Playlists:\n", "\n".join(playlists), "\n"


if __name__ == "__main__":
  searchQuery = raw_input('Give the Query: ')
  argparser.add_argument("--q", help="Search term", default=searchQuery)
  argparser.add_argument("--max-results", help="Max results", default=50)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)