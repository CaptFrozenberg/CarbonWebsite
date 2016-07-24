from django.conf.urls import url, include
from .views import GaleryView

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^galery/$',GaleryView.as_view(), name='galery'),
]