import shutil

import requests
from bs4 import BeautifulSoup


class InstagramDownloader:
    def __init__(self, media_url):
        self.media_url = media_url

        if not self.media_url.startswith('https://www.instagram.com/p/'):
            raise ValueError('Invalid Instagram URL.')

    def get_soup(self):
        response = requests.get(self.media_url)

        return BeautifulSoup(response.text, 'html.parser')

    def get_download_url(self):
        soup = self.get_soup()

        content_video_meta = soup.find('meta', property='og:video')
        content_image_meta = soup.find('meta', property='og:image')
        content_meta = content_video_meta or content_image_meta

        return content_meta.get('content')

    def get_output_filename(self):
        return self.get_download_url().split('/')[-1]

    def download(self):
        download_url = self.get_download_url()
        response = requests.get(download_url, stream=True)

        filename = self.get_output_filename()
        with open(filename, mode='wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)

        print('File successfuly downloaded.')
