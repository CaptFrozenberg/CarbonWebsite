from django.shortcuts import render
from django.utils.translation import get_language_from_request
from django.views.generic.base import TemplateView
from news.models import News

class NewsView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        lang_code = get_language_from_request(self.request, check_path=True)
        context = super(NewsView, self).get_context_data(**kwargs)
        context['news_list'] = News.objects.filter(language=lang_code)
        print(len(News.objects.filter(language=lang_code)))
        print(lang_code)
        return context
