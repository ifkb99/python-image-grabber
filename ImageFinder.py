#make a batch file to run this
#run in command prompt
#work with requests library and shutil

import praw
import urllib.request, shutil
import Config, DownloadImage
import os, sys
import imgurpython
import traceback
import argparse
import mmap#_backed_array

r = praw.Reddit(user_agent=Config.user_agent)
parser = argparse.ArgumentParser()

i_client = imgurpython.ImgurClient(Config.imgur_id, Config.imgur_secret)
imgur_api = 'https://api.imgur.com/3/' #http://api.imgur.com/

default_path = '\\pics\\'
default_sub = 'awwnime'
default_search = 'kuroneko'

##def FileType(URL): #get image filetype
##    return ''.join(('.', URL.rsplit('.')[-1]))
##
##def DownloadImage(URL, path, name, number=''):
##    image = urllib.request.urlopen(URL)
##    file_name = ''.join((name, str(number), FileType(URL)))
##    file_path = '{}{}{}'.format(os.getcwd(), path, file_name) #I'm just trying different stuff here
##    print(name)
##    image_data = image.read()
##    with open(file_path, 'wb+') as file:
##        file.write(image_data)
##    image.close()

def AlbumOrSingle(URL, name, path):
    try:
        name = name.replace(".", "")
        name = name.replace("#", "")
        name = name.replace("?", "")
        name = name.replace("!", "")
        name = name.replace("~", "")
        name = name.replace('"', "")
        name = name.replace("'", "")
        name = name.replace('\\', '')
        name = name.replace('(', '')
        name = name.replace(')', '')
        if '/a/' in URL: #add doujin folder support
            pic_num = 1
            album_id = URL.rsplit('/a/')[-1]
            album = i_client.get_album_images(album_id) #>only asks for album id >I reply with entire link
            for picture in album:
                DownloadImage.download(picture.link, path, name, str(pic_num)) #image.link instead of URL
                pic_num += 1
        else:
            DownloadImage(URL, path, name)
    except:
        sys.stdout.write('Failed: ')
        traceback.print_exc()
        return False

def main():
    parser.add_argument('--query', type=str, default=default_search,
                        help='What do you want to search for?')
    parser.add_argument('--path', type=str, default=default_path,
                        help='Type the path you would like to store the pics in')
    parser.add_argument('--subreddit', type=str, default=default_sub,
                        help='The subbreddit(s) you would like to search')
    args = parser.parse_args()
    
    query_results = r.search(query=args.query, subreddit=args.subreddit)
    search = list(query_results)
    path = args.path

    if not os.path.isdir(os.getcwd() + path):
        os.mkdir(os.getcwd() + path)

    f = open('links.txt', 'a+')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    
    for submission in search:
        URL = vars(submission)['url']
        name = vars(submission)['title']
        if s.find(bytes(URL,'utf-8')) == -1: #commented != to == for debug
            sys.stdout.write(''.join(('Dupe found at: ', name, '\n')))
        else:
            try:
                AlbumOrSingle(URL, name, path)
                f.write(' '.join([URL, ':: ']))
            except:
                sys.stdout.write(''.join(('Error at: ', name, '\n')))
    f.close()
    sys.stdout.write('Finished!')
    

if __name__ == '__main__':
    main()
