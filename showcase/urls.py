from django.conf.urls import url, include
from .views import IndustryView

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^showcase/(?P<industry>[a-zA-Z0-9-_]+)/$', IndustryView.as_view(), name='showcase')

]