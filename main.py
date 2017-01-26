# make a batch file to run this
# run in command prompt
# work with requests library and shutil

import praw
import config
from url_mgr import AlbumOrSingle, repeat_mgr
import os, sys
import argparse
import mmap
import traceback

r = praw.Reddit(user_agent=config.reddit_user_agent,
                client_id=config.reddit_client_id,
                client_secret=config.reddit_secret)

parser = argparse.ArgumentParser()

default_path = os.getcwd() + '\\pics\\'
default_sub = 'awwnime'
default_search = 'kuroneko'

def main():
    parser.add_argument('--query', type=str, default=default_search,
                        help='What do you want to search for?')
    parser.add_argument('--path', type=str, default=default_path,
                        help='Type the path you would like to store the pics in')
    parser.add_argument('--subreddit', type=str, default=default_sub,
                        help='The subbreddit(s) you would like to search')
    args = parser.parse_args()
    
    query_results = praw.models.Subreddit(r, args.subreddit).search(query=args.query)# limit for debug
    search = list(query_results)
    path = args.path

    repeat_mgr(path)
    
    f = open('links.txt', 'a+')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    for submission in search:
        URL = vars(submission)['url']
        name = vars(submission)['title']
        if s.find(bytes(URL,'utf-8')) != -1: # commented != to == for debug
            sys.stdout.write(''.join(('Dupe found at: ', name, '\n')))
        else:
            try:
                aos = AlbumOrSingle(URL, path, name, doujin)
                aos.urltype()
                sys.stdout.write(name)
                f.write(' '.join([URL, ':: ']))
            except:
                sys.stdout.write(''.join(('Error at: ', name, '\n')))
                traceback.print_exc()
    f.close()
    sys.stdout.write('Finished!')
    
if __name__ == '__main__':
    main()
