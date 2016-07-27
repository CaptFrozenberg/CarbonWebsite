from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.views.generic.base import TemplateView
from django.views.generic import FormView
from generic.mixins import LangListMixin
from main.forms import ContactForm
from showcase.models import Industry

from django.utils.translation import get_language_from_request

class MainPageView(TemplateView, LangListMixin):
    template_name = 'mainpage.html'
    
    def get_context_data(self, **kwargs):
        industrys = Industry.objects.all()
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['industrys'] = industrys
        return context

class ContactView(FormView, LangListMixin):
    template_name = 'contacts.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['form'] = ContactForm
        return context

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main')

class GaleryView(TemplateView):
    template_name = 'photos.html'