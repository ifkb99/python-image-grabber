import argparse
import os, sys
import mmap
import praw
import config
from url_mgr import AlbumOrSingle

r = praw.Reddit(user_agent=config.reddit_user_agent,
                client_id=config.reddit_client_id,
                client_secret=config.reddit_secret)

parser = argparse.ArgumentParser()

default_path = 'C:\Users\{}\Pictures'.format(os.getlogin())

def main():
    parser.add_argument('--url', type=str, default=none,
                        help='Type the doujin URL (from reddit)')
    parser.add_argument('--path', type=str, default=default_path,
                        help='The path to store the doujin in')
    args = parser.parse_args()

    post = praw.models.Submission(r, url=args.url)
    URL = vars(post)['url']
    name = vars(post)['title']
    
    aos = AlbumOrSingle(URL, args.path, name)
    aos.urltype()
    sys.stdout.write('Finished!\n')
