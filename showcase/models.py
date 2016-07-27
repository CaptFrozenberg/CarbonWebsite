from django.db import models
from django.utils.translation import ugettext as _
from precise_bbcode.fields import BBCodeTextField

class Industry(models.Model):
    title_ru = models.CharField(max_length=30, verbose_name=_('Название на русском языке'))
    title_en = models.CharField(max_length=30, verbose_name=_('Название на английском языке'))
    img_key = models.SlugField(max_length=10, blank=True, null=True)
    key = models.SlugField(max_length=10, default='')
    description_ru = models.TextField(verbose_name=_('Краткое описание на русском языке'))
    description_en = models.TextField(verbose_name=_('Краткое описание на английском языке'))
    content_ru = BBCodeTextField(max_length=500, verbose_name=_('Полное описание на русском языке'))
    content_en = BBCodeTextField(max_length=500, verbose_name=_('Полное описание на английском языке'))
    src = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_ru

class Project(models.Model):
    name_ru = models.CharField(max_length=50, verbose_name=_('Название на русском языке'))
    name_en = models.CharField(max_length=50, verbose_name=_('Название на английском языке'))
    content_ru = BBCodeTextField(verbose_name=_('Содержание на русском языке'))
    content_en = BBCodeTextField(verbose_name=_('Содержание на английском языке'))
    industry = models.ForeignKey(Industry, verbose_name=_('Отрасль'))

    def __str__(self):
        return self.name_ru
