from django.conf.urls import url, include
from news.views import NewsView

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^news/$', NewsView.as_view(), name='news'),

]
