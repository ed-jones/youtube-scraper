__version__ = '0.1.0'

import sys, os, argparse
from youtube_scraper.trending_videos import TrendingVideos
from youtube_scraper.csv_update import CSVUpdate
from youtube_scraper.globals import *

def main():
    api_key = ''

    if os.path.isfile('api_key.txt'):
        f = open("api_key.txt", "r")
        api_key = f.read()
    else:
        print("Missing API Key")
        exit()

    parser = argparse.ArgumentParser(description='Generate a CSV file from YouTube data')

    parser.add_argument('-api_key', help="Add or update your YouTube Data API key")

    subparsers = parser.add_subparsers(title='Source', help='Source of YouTube data', dest='source')

    parser_trending = subparsers.add_parser('trending', help='Downloads YouTube data from trending')
    parser_trending.add_argument('-n', metavar='0-'+str(MAX_RESULTS), nargs='?', help='Number of videos to get', type=int, default=MAX_RESULTS)
    parser_trending.add_argument('-o', metavar='/path/to/output.csv', nargs='?', help='Location of output CSV file', type=argparse.FileType('w'), default=OUTPUT_FILE_NAME)

    parser_csv = subparsers.add_parser('csv', help='Downloads YouTube Data based on an existing CSV file')
    parser_csv.add_argument('-i', metavar='/path/to/input.csv', nargs='?', help='Location of input CSV file', type=argparse.FileType('r'), required=True)
    parser_csv.add_argument('-o', metavar='/path/to/output.csv', nargs='?', help='Location of output CSV file', type=argparse.FileType('w'), default=OUTPUT_FILE_NAME)

    args = parser.parse_args()
    
    if args.api_key:
        try:
            f = open("api_key.txt", "w")
            f.write(args.api_key)
            print("Successfully updated API Key")
        except:
            print("There was an error updating API Key: " + sys.exc_info()[0])

        exit()

    if args.source is None:
        parser.parse_args(['-h'])

    if args.source == 'trending':
        try:
            TrendingVideos(api_key, args.n, args.o.name)
            print("Done")
        except:
            print("There was an error getting trending videos: " + sys.exc_info()[0])

    if args.source == 'csv':
        try:
            CSVUpdate(api_key, args.i.name, args.o.name)
            print("Done")
        except:
            print("There was an error generating new CSV: " + sys.exc_info()[0])
