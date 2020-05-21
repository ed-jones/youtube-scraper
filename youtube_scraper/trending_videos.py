from googleapiclient.discovery import build
from youtube_scraper.globals import *
import csv, os

def main(api_key):
    if not os.path.isfile(OUTPUT_FILE_NAME):
        addHeading()
    addBody(api_key)

def addHeading():
    csvHeading = []
    for videoDetails in VIDEO_DETAILS_LIST:
        csvHeading += videoDetails['columnNames']
    writeToCSV([csvHeading])

def addBody(api_key):
    csvBody = []

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=api_key)
    
    request = youtube.videos().list(
        part="id, snippet, statistics, contentDetails",
        chart="mostPopular",
        maxResults=MAX_RESULTS,
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

    writeToCSV(csvBody)

def writeToCSV(dataToWrite):
    with open(OUTPUT_FILE_NAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dataToWrite)
