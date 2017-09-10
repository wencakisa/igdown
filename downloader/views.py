import mimetypes
from wsgiref.util import FileWrapper

from django.shortcuts import render
from django.http.response import HttpResponse

from .ig_downloader import InstagramDownloader


def home(request):
    return render(request, 'base.html')

def download(request):
    download_url = request.POST['download_url']
    downloader = InstagramDownloader(download_url)
    downloader.download()

    filename = downloader.get_output_filename()

    wrapper = FileWrapper(open(filename, mode='rb'))
    content_type = mimetypes.guess_type(downloader.get_download_url())

    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Disposition'] = "attachment; filename={}".format(filename)

    return response
