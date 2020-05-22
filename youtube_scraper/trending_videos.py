from googleapiclient.discovery import build
from youtube_scraper.globals import *
from youtube_scraper.youtube_csv import YouTubeCSV
import csv, os

class TrendingVideos(YouTubeCSV):

    def __init__(self, api_key, max_results, output_file):
        super().__init__(api_key, output_file)

        self.max_results = max_results
        self.output_file = output_file

        if not os.path.isfile(self.output_file):   
            self.write(self.getHeading())
        self.write(self.getBody())

    def getBody(self):
        csvBody = []

        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=self.api_key)
        
        request = youtube.videos().list(
            part="id, snippet, statistics, contentDetails",
            chart="mostPopular",
            maxResults=self.max_results,
            regionCode=REGION_CODE,
        )

        response = request.execute()

        for items in response['items']:
            newRow = []
            for videoDetails in VIDEO_DETAILS_LIST:
                for column in videoDetails['columnNames']:
                    if 'part' in videoDetails:
                        newRow.append(items[videoDetails['part']][column] if column in items[videoDetails['part']] else '')
                    else:
                        newRow.append(items[column] if column in items else '')

            csvBody.append(newRow)

        return csvBody

