from wsgiref.util import FileWrapper

from django.shortcuts import render
from django.http.response import HttpResponse

from .ig_downloader import InstagramDownloader


def home(request):
    return render(request, 'downloader/index.html')

def download(request):
    download_url = request.POST['download_url']
    downloader = InstagramDownloader(download_url)
    downloader.download()

    filename = downloader.get_output_filename()
    wrapper = FileWrapper(open(filename, mode='rb'))
    response = HttpResponse(wrapper)
    response['Content-Disposition'] = "attachment; filename={}".format(filename)

    return response
