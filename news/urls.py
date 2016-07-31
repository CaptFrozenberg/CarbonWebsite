from django.conf.urls import url, include
from news.views import NewsView, NewsDetailView
from django.views.generic.dates import ArchiveIndexView
from .models import News


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^news/$', ArchiveIndexView.as_view(model=News, date_field='pub_date', template_name='news.html'), name='news'),
    # url(r'^news/$', NewsView.as_view(), name='news'),
    url(r'^news/detail/(?P<news_id>[0-9]+)/$', NewsDetailView.as_view(), name='news_detail')

]
