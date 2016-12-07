# python-image-grabber
grabs images from reddit using python

This is an update of a script I had working in python 2.7, and since imgur decided that I need to use its api do do anything now I decided to update the whole script

todo:

- add support for gui (easygui?)
- add support for downloading comics
- add proper licensing
- add a .gitignore
- probably make a separate todo.md file

features:

- commandline functionality
- works with imgur albums
- stores previously downloaded URLs in order to prevent overwriting images
- nsfw filter
- now with object oriented programming!

## How can I use this program?

Firstly, you need to download the PRAW and imgurpython modules if you do not have them already.

This can be done easily using pip by opening your command line program and typing

```
pip install [module_name]
```

where [module_name] is replaced with the module you are downloading.

Second, create a config.py file that contains your reddit and imgur api information. You can make a reddit app or access a current one [here](https://www.reddit.com/prefs/apps/ "Reddit App Info") and imgur api credentials can be obtained [here](https://api.imgur.com/oauth2/addclient "Imgur Api Info"). An account at each site is required for the api info.

Thrid, this program currently only works through command line. To use the program open command line and type

```
%PATH%\python imagefinder.py --query=[search] --subreddit=[subreddit] --path=[path] --nsfw_filter=[True/False]
```

with %PATH% as the directory of the script, and the words in brackets with the specifications for your search. The variables can be assigned in any order. You can also choose to not assign some variables and they will default to values I have given them. For instance, the nsfw filter defaults to False, so you would not need to include it at all in order to download nsfw images. You can change these values at the top of the main.py file. Once you hit enter the program will run, and the files will be downloaded to the given path.

That's it! Lastly, feel free to use this program wherever and however you would like, along with any modifications you would like to make. My only request is that you credit me if this program is used in any project or program that you make.
