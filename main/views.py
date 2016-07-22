from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import FormView
from generic.mixins import LangListMixin
from main.forms import ContactForm

class MainPageView(TemplateView, LangListMixin):
    template_name = 'mainpage.html'

class ContactView(FormView, LangListMixin):
    template_name = 'contacts.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['form'] = ContactForm
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        # print "form is valid"
        return super(ContactView, self).form_valid(form)