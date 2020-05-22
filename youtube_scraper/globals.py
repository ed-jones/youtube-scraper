from datetime import datetime

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
MAX_RESULTS = 50
REGION_CODE = 'AU'
datetime_obj = datetime.now()
todays_date = str(datetime_obj.year) + '-' + str(datetime_obj.month) + '-' + str(datetime_obj.day)
OUTPUT_FILE_NAME = 'youtube_data_' + todays_date + '.csv'
VIDEO_DETAILS_LIST = [
    {'columnNames': ['id']},
    {'part': 'snippet', 'columnNames': ['channelTitle', 'categoryId', 'tags', 'title', 'description']},
    {'part': 'statistics', 'columnNames': ['viewCount', 'likeCount', 'dislikeCount', 'commentCount']},
    {'part': 'contentDetails', 'columnNames': ['duration', 'definition', 'caption']}
]

__all__ = ['YOUTUBE_API_SERVICE_NAME', 'YOUTUBE_API_VERSION', 'MAX_RESULTS', 'REGION_CODE', 'OUTPUT_FILE_NAME', 'VIDEO_DETAILS_LIST']