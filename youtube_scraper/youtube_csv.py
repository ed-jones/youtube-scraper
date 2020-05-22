import csv, os
from youtube_scraper.globals import *

class YouTubeCSV():
    def __init__(self, api_key, output_file):
        self.api_key = api_key
        self.output_file = output_file

    def getHeading(self):
        csvHeading = []
        for videoDetails in VIDEO_DETAILS_LIST:
            csvHeading += videoDetails['columnNames']
        return [csvHeading]

    def write(self, dataToWrite):
        with open(self.output_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(dataToWrite)