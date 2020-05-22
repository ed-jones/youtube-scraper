from googleapiclient.discovery import build
from youtube_scraper.globals import *
from youtube_scraper.youtube_csv import YouTubeCSV
import csv, os, re, sys

class CSVUpdate(YouTubeCSV):

    def __init__(self, api_key, input_file, output_file):
        super().__init__(api_key, output_file)
        self.input_file = input_file

        if not os.path.isfile(input_file):
            print('File ' + input_file + ' not found')
            exit()

        if not os.path.isfile(output_file):   
            self.write(self.getHeading())

        video_id_list = ''
        row_count = 0
        with open(input_file) as csv_file:
            row_count = sum(1 for line in csv_file)

        with open(input_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            row_increment = 0

            for row in csv_reader:
                if row_increment != 0:
                    if not re.match(r"^([a-z0-9_-]{11})$", row[0], re.I):
                        print('Badly formed video id on line ' + str(row_increment) + '. Ignoring this video')
                    else:
                        video_id_list += row[0] + ','

                        if row_increment%50 == 0:

                            sys.stdout.write("\rProgress: "+str(round(10000*row_increment/row_count)/100)+'%')
                            video_id_list = video_id_list[:-1]
                            self.write(self.getBody(video_id_list)) 
                            video_id_list = ''
                row_increment += 1

            self.write(self.getBody(video_id_list)) 
        

    def getBody(self, video_id_list):
        csvBody = []

        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=self.api_key)
        
        request = youtube.videos().list(
            part="id, snippet, statistics, contentDetails",
            id=video_id_list
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
