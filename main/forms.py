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
        content = self.cleaned_data['content']
        contact_email = self.cleaned_data['contact_email']
        recipients = ['info@carbon-service.ru']
        send_mail(subject, content, contact_email, recipients)

