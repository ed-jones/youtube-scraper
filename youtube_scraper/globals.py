YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
MAX_RESULTS = 50
REGION_CODE = 'AU'
OUTPUT_FILE_NAME = 'youtube_data.csv'
VIDEO_DETAILS_LIST = [
    {'columnNames': ['id']},
    {'part': 'snippet', 'columnNames': ['channelTitle', 'categoryId', 'tags', 'title', 'description']},
    {'part': 'statistics', 'columnNames': ['viewCount', 'likeCount', 'dislikeCount', 'commentCount']},
    {'part': 'contentDetails', 'columnNames': ['duration', 'definition', 'caption']}
]
