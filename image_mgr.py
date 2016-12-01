import urllib.request
import os
import traceback

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


class AlbumOrSingle:

    def __init__(self, URL, name, path):
        self.URL = URL
        self.name = name
        self.path = path
    
    def urltype(self):
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
            if '/a/' in self.URL: #add doujin folder support
                pic_num = 1
                album_id = self.URL.rsplit('/a/')[-1]
                album = i_client.get_album_images(album_id) #>only asks for album id >I reply with entire link
                for picture in album:
                    DownloadImage.download(picture.link, self.path, self.name, str(pic_num)) #image.link instead of URL
                    pic_num += 1
            else:
                DownloadImage.download(self.URL, self.path, self.name)
        except:
            sys.stdout.write('Failed: ')
            traceback.print_exc()
            return False
