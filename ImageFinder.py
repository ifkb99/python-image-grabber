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

i_client = imgurpython.ImgurClient(Config.imgur_id, Config.imgur_secret)
imgur_api = 'https://api.imgur.com/3/' #http://api.imgur.com/

def FileType(URL):
    return URL.rsplit('.')

def DownloadImage(URL, path, name[,number]):
    image = urllib.urlopen(URL.link)
    file_path = ['//'].join(os.getcwd(), path, name + number + FileType(URL))
    image_data = image.read()
    downloaded_image = file(file_path, 'wb')
    downloaded_image.write(image_data)
    image.close()

def AlbumOrSingle(URL, name):
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
                DownloadImage(URL, path_test, name, pic_num)
                pic_num += 1
        
        else:
            DownloadImage(URL, path_test, name)
    except:
        return False
