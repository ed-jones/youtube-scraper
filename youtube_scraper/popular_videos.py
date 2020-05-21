from googleapiclient.discovery import build
from globals import *
import csv, os

def main():
    if not os.path.isfile(OUTPUT_FILE_NAME):
        addHeading()
    addBody()

def addHeading():
    csvHeading = []
    for videoDetails in VIDEO_DETAILS_LIST:
        csvHeading += videoDetails['columnNames']
    writeToCSV([csvHeading])

def addBody():
    csvBody = []

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    
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

if __name__ == "__main__":
    main()