from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'downloader'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^download/$', views.download, name='download')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
