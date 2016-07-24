from django.conf.urls import url, include
from news.views import NewsView, NewsAddView

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^news/$', NewsView.as_view(), name='news'),
    url(r'^news/add/$', NewsAddView.as_view(), name='news_add')

]
