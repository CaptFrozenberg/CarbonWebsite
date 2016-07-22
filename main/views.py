from django.shortcuts import render

from django.views.generic.base import TemplateView
from generic.mixins import LangListMixin

class MainPageView(TemplateView, LangListMixin):
    template_name = 'mainpage.html'
