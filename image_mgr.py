from downloadimage import DownloadImage

class AlbumOrSingle: # http://stackoverflow.com/questions/11421659/passing-variables-creating-instances-self-the-mechanics-and-usage-of-classes

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
            if '/a/' in self.URL: # enters, but does not complete download
                di.download_album()
            else:
                di.download_single()
        except OSError as e:
            print('OSError: ', e)
            return False
