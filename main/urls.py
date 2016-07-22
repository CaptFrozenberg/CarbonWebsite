from django.conf.urls import url, include
from main.views import MainPageView

urlpatterns = [

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', MainPageView.as_view(), name='main'),
]