import urllib.request
import os
import config
import imgurpython

class DownloadImage:

    def __init__(self, URL, path, name, number=''):
        self.i_client = imgurpython.ImgurClient(config.imgur_id, config.imgur_secret)
        self.URL = URL
        self.path = path
        self.name = name
        self.number = number

    def filetype(self):
        return ''.join(('.', self.URL.rsplit('.')[-1]))

    def download_single(self):
        image = urllib.request.urlopen(self.URL)
        file_name = ''.join((self.name, str(self.number), self.filetype()))
        file_path = '{}{}{}'.format(os.getcwd(), self.path, file_name)
        if os.path.isdir(file_path):
            file_path = '{}0{}'.format(file_path[4:], self.filetype())
        image_data = image.read()
        with open(file_path, 'wb+') as file:
            file.write(image_data)
        image.close()

    def download_album(self):
        self.number = 1
        album_id = self.URL.rsplit('/a/')[-1]
        album = self.i_client.get_album_images(album_id)
        for picture in album:
            self.download_single()
            self.number += 1
