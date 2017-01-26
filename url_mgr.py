from downloadimage import DownloadImage
import os

class AlbumOrSingle:

    def __init__(self, URL, path, name, doujin):
        self.URL = URL
        self.path = path
        self.name = name
        self.doujin = doujin
    
    def urltype(self):
        try:
            self.name = self.name.replace(".", "")
            self.name = self.name.replace("#", "")
            self.name = self.name.replace("?", "")
            self.name = self.name.replace("!", "")
            self.name = self.name.replace("~", "")
            self.name = self.name.replace('"', "")
            self.name = self.name.replace("'", "")
            self.name = self.name.replace('\\', '')
            self.name = self.name.replace('(', '')
            self.name = self.name.replace(')', '')
            di = DownloadImage(self.URL, self.path, self.name, self.doujin)
            print(self.URL)
            if '/a/' in self.URL: 
                di.download_album()
            else:
                di.download_single()
        except OSError as e:
            print('OSError: ', e)
            return False

def repeat_mgr(path):
    # make file storage directory if it does not exist
    if not os.path.isdir(path): 
        os.mkdir(path)
    # check for/create url storage doc
    if not os.path.isdir(os.getcwd() + 'links.txt'):
        f = open('links.txt', 'a+')
        f.write('\n')# needs something in file in order to mmap
        f.close()
