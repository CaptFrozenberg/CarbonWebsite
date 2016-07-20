from django.shortcuts import render

from django.views.generic.base import TemplateView

class MainPageView(TemplateView):
    template_name = 'mainpage.html'
