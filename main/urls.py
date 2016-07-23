from django.conf.urls import url, include
from main.views import MainPageView, ContactView, NewsView, GaleryView

urlpatterns = [

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^news/$', NewsView.as_view(), name='news'),
    url(r'^galery/$', GaleryView.as_view(), name='galery'),

]