from downloadimage import DownloadImage

class AlbumOrSingle:

    def __init__(self, URL, path, name):
        self.URL = URL
        self.path = path
        self.name = name
    
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
            di = DownloadImage(self.URL, self.path, self.name)
            print(self.URL)
            if '/a/' in self.URL: 
                di.download_album()
            else:
                di.download_single()
        except OSError as e:
            print('OSError: ', e)
            return False
