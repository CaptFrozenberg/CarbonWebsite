from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Industry, Project

class IndustryView(TemplateView):
    template_name = 'showcase.html'

    def get_context_data(self, **kwargs):
        context = super(IndustryView, self).get_context_data(**kwargs)
        context['industry'] = Industry.objects.get(key=self.kwargs['industry'])
        context['projects'] = Project.objects.filter(industry__key=self.kwargs['industry'])
        # context['key'] = self.kwargs['industry']
        return context

