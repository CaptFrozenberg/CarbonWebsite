from django.db import models
from django.utils.translation import ugettext as _

class GaleryItem(models.Model):
    name = models.CharField(max_length=40, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата публикации'))
    image = models.ImageField(verbose_name=_('Изображение'),
                              error_messages={'required': _('Укажите файл изображения'),
                                              'invalid_image': _('Данный формат изображения не поддерживается сайтом'),
                                              'empty': _('Выгружаемый файл пуст')}
                              )

    def __str__(self):
        return self.name
