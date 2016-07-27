from django.db import models
from django.utils.translation import ugettext as _
from precise_bbcode.fields import BBCodeTextField

class News(models.Model):
    title_ru = models.CharField(max_length=30, unique=True, verbose_name=_('Заголовок на русском языке'))
    title_en = models.CharField(max_length=30, unique=True, verbose_name=_('Заголовок на английском языке'))
    pub_date = models.DateField(verbose_name=_('Дата публикации'))
    short_content_ru = models.TextField(max_length=200, verbose_name=_('Краткое содержание на русском языке'))
    short_content_en = models.TextField(max_length=200, verbose_name=_('Краткое содержание на английском языке'))
    content_ru = BBCodeTextField(verbose_name=_('Содержание на русском языке'))
    content_en = BBCodeTextField(verbose_name=_('Содержание на английском языке'))
    image = models.ImageField(verbose_name=_('Изображение'),
                              error_messages={ 'required' : _('Укажите файл изображения'),
                                               'invalid_image' : _('Данный формат изображения не поддерживается сайтом'),
                                               'empty' : _('Выгружаемый файл пуст')}
                              )

    def __str__(self):
        return self.title_ru
