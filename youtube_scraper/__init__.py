__version__ = '0.1.0'

import sys, os
import youtube_scraper.trending_videos

def main():
    api_key = ''

    if not os.path.isfile('api_key.txt'):
        print('Enter your YouTube Data API Key:')
        api_key = input()
        f = open("api_key.txt", "a")
        f.write(api_key)
        exit()
    else:
        f = open("api_key.txt", "r")
        api_key = f.read()

    if len(sys.argv) == 2:
        if sys.argv[1] == 'trending':
            trending_videos.main(api_key)
        else:
            print('Invalid argument. Please read the README.md file')

    elif len(sys.argv) == 3:
        if sys.argv[1] == 'csv':
            print('csv videos')
            
    else:
        print('Incorrect number of arguments. Please read the README.md file')
