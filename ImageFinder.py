#make a batch file to run this
#run in command prompt
#work with requests library and shutil

import praw
import urllib
import Config
import os, sys
import imgurpython
import traceback
import argparse

r = praw.Reddit(user_agent=Config.user_agent)
parser = argparse.ArgumentParser()

i_client = imgurpython.ImgurClient(Config.imgur_id, Config.imgur_secret)
imgur_api = 'https://api.imgur.com/'#3/' #http://api.imgur.com/

default_path = '\\pics\\'
default_sub = 'awwnime'

def FileType(URL):
    return URL.rsplit('.')

def DownloadImage(URL, path, name[, number]):
    image = urllib.urlopen(URL.link)
    file_path = ['\\'].join(os.getcwd(), path, name + number + FileType(URL))
    image_data = image.read()
    downloaded_image = file(file_path, 'wb')
    downloaded_image.write(image_data)
    image.close()

def AlbumOrSingle(args, URL, name):
    try:
        name = name.replace(".", "")
        name = name.replace("#", "")
        name = name.replace("?", "")
        name = name.replace("!", "")
        name = name.replace("~", "")
        name = name.replace('"', "")
        name = name.replace("'", "")
        if '/a/' in URL: #add doujin folder support
            pic_num = 1
            album_key = URL.rsplit('/')[-1]
            album = i_client.get_album_images([''].join(imgur_api, album_key))
            for image in album:
                DownloadImage(URL, args.path, name, pic_num)
                pic_num += 1
        else:
            DownloadImage(URL, args.path, name)
    except:
        sys.stdout.write('Failed', traceback.print_exception)
        return False

def main():
    parser.add_argument('--query', type=str, default='NULL',
                        help='What do you want to search for?')
    parser.add_argument('--path', type=str, default=default_path,
                        help='Type the path you would like to store the pics in')
    parser.add_argument('--subreddit', type=str, default=default_sub,
                        help='The subbreddit(s) you would like to search')
    args = parser.parse_args()
    serach = r.search(args.query, args.subreddit)
    for pic in search:
        
        AlbumOrSingle(args, URL, name)
    

if __name == '__main__':
    main()
