__version__ = '0.1.0'

import sys

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'trending':
            print('trending videos')
        elif sys.argv[1] == 'id':
            print('video id')
        else:
            print('Invalid argument. Please read the README.md file')
    else:
        print('Incorrect number of arguments. Please read the README.md file')
