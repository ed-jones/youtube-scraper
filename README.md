# YouTube Scraper
Designed to collect data from YouTube for ISIT219

## Setup
1. Make sure you have the latest version of Python installed https://www.python.org/downloads/
2. Make sure you have the latest version of Poetry installed https://python-poetry.org/docs/
3. Inside the repo's root directory run `poetry install`
4. You must acquire a YouTube Data API key [like so](https://developers.google.com/youtube/registering_an_application)
5. When the API Key is obtained it must be entered into `youtube-scraper/globals.py`

## Usage
* Generate a CSV of trending videos: `poetry run youtube-scraper trending`
> This command will create a new file if none exists and populates it with trending videos from today. The same script can be run again the following day to add that day's videos to the list.
* Generate a CSV of videos based on an existing CSV: `poetry run youtube-scraper csv {/path/to/file.csv}`
> This command will generate a new CSV file based on the id column of an existing CSV. This is useful if you need to update your data, or add new data columns.