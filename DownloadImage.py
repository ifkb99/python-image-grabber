import urllib.request
import os

class DownloadImage:

    def __init__(self, URL, path, name, number=''):
        self.URL = URL
        self.path = path
        self.name = name
        self.number = number

    def filetype(self):
        return ''.join(('.', self.URL.rsplit('.')[-1]))

    def download(self):
        image = urllib.request.urlopen(self.URL)
        file_name = ''.join((self.name, str(self.number), filetype(self.URL)))
        file_path = '{}{}{}'.format(os.getcwd(), self.path, file_name) #I'm just trying different stuff here
        print(self.name)
        image_data = image.read()
        with open(file_path, 'wb+') as file:
            file.write(image_data)
        image.close()
