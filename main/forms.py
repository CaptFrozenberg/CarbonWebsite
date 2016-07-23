from django import forms
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

class ContactForm(forms.Form):
    contact_name = forms.CharField(label = '', required=True,
                                   widget=forms.TextInput(attrs={'id' : 'name', 'placeholder': _('Имя')}), )
    contact_email = forms.EmailField(label= '', required=True,
                                     widget=forms.EmailInput(attrs={'id': 'e-mail', 'placeholder': 'E-mail'}))
    subject = forms.CharField(label = '', required=True,
                              widget=forms.TextInput(attrs={'id' : 'title', 'placeholder': _('Тема сообщения')}))
    content = forms.CharField(label= '', required=True,
                              widget=forms.Textarea(attrs={'id' : 'text', 'placeholder': _('Текст сообщения')}))

    def send_email(self):
        subject = self.cleaned_data['subject']
        contact_name = self.cleaned_data['contact_name']
        contact_email = self.cleaned_data['contact_email']
        content = '{0} \n\n{1}: {2} \n\n{3}, {4} '.format(self.cleaned_data['content'], _('Ответить на адрес'),
                                                      contact_email, _('С наилучшими пожеланиями'), contact_name)
        sender_email = 'rodionov.zenitem@yandex.ru'
        recipients = ['captfrozenberg@gmail.com']
        send_mail(subject, content, sender_email, recipients)
