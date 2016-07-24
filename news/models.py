from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

class News(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name=_('Заголовок'))
    pub_date = models.DateField(verbose_name=_('Дата публикации'))
    short_content = models.TextField(max_length=200, verbose_name=_('Краткое содержание'))
    content = models.TextField(verbose_name=_('Содержание'))
    language = models.CharField(max_length=20, choices=settings.LANGUAGES)
    image = models.ImageField(verbose_name=_('Изображение'),
                              error_messages={ 'required' : _('Укажите файл изображения'),
                                               'invalid_image' : _('Данный формат изображения не поддерживается сайтом'),
                                               'empty' : _('Выгружаемый файл пуст')}
                              )

    def __str__(self):
        return self.title
