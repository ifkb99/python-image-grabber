# python-image-grabber
grabs images from reddit using python

This is an update of a script I had working in python 2.7, and since imgur decided that I need to use its api do do anything now I decided to update the whole script

todo:

- add support for gui (easygui?)
- add support for downloading comics
- add nsfw filter option

features:

- commandline functionality
- works with imgur albums
- now with object oriented programming!

## How can I use this program?

Firstly, you need to download the PRAW and imgurpython modules if you do not have them already.

This can be done easily using pip by opening your command line program and typing

```
pip install [module_name]
```

where [module_name] is replaced with the module you are downloading.

Second, create a config.py file that contains your reddit and imgur api information. You can make a reddit app or access a current one [here](https://www.reddit.com/prefs/apps/ "Reddit App Info") to get your reddit api information and imgur [here](https://api.imgur.com/oauth2/addclient "Imgur Api Info"). An account at each site is required for the api info.

Finally, this program currently only works through command line. To use the program open command line and type

```
%PATH%\imagefinder.py --query=[search] --subreddit=[subreddit] --path=[path]
```

with [search] replaced with what you want to search, [subreddit] replaced with the subreddit to search(can do multiple subs with + sign), and [path] with the path you want. They can be assigned in any order.
