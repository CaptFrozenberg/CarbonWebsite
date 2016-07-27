from django.db import models
from django.utils.translation import ugettext as _

class GaleryItem(models.Model):
    name_ru = models.CharField(max_length=40, verbose_name=_('Название на русском языке'))
    name_en = models.CharField(max_length=40, verbose_name=_('Название на английском языке'))
    description_ru = models.TextField(verbose_name=_('Описание на русском языке'))
    description_en = models.TextField(verbose_name=_('Описание на английском языке'))
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата публикации'))
    image = models.ImageField(verbose_name=_('Изображение'),
                              error_messages={'required': _('Укажите файл изображения'),
                                              'invalid_image': _('Данный формат изображения не поддерживается сайтом'),
                                              'empty': _('Выгружаемый файл пуст')}
                              )

    def __str__(self):
        return self.name_ru
