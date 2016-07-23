from django.db import models
from django.conf import settings

class News(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='Заголовок')
    pub_date = models.DateField(verbose_name='Дата публикации')
    short_content = models.TextField(max_length=200, verbose_name='Краткое содержание')
    content = models.TextField(verbose_name='Содержание')
    #language = models.CharField(max_length=20, choices=settings.LANGUAGES)
