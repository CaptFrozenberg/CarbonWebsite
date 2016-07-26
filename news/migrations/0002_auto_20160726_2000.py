# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import precise_bbcode.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='_content_rendered',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=precise_bbcode.fields.BBCodeTextField(no_rendered_field=True, verbose_name='Содержание'),
        ),
    ]
