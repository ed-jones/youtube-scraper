from googleapiclient.discovery import build
from youtube_scraper.globals import *
import csv, os, re, sys

def main(api_key, path_to_csv):
    if not os.path.isfile(path_to_csv):
        print('File ' + path_to_csv + ' not found')
        exit()

    video_id_list = ''

    if not os.path.isfile(OUTPUT_FILE_NAME):
        addHeading()

    row_count = 0
    with open(path_to_csv) as csv_file:
        row_count = sum(1 for line in csv_file)

    with open(path_to_csv) as csv_file:
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
                        addBody(api_key, video_id_list)  
                        video_id_list = ''
            row_increment += 1
        
def addHeading():
    csvHeading = []
    for videoDetails in VIDEO_DETAILS_LIST:
        csvHeading += videoDetails['columnNames']
    writeToCSV([csvHeading])

def addBody(api_key, video_id_list):
    csvBody = []

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=api_key)
    
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

    writeToCSV(csvBody)

def writeToCSV(dataToWrite):
    with open(OUTPUT_FILE_NAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dataToWrite)
