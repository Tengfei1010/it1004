# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.TextField(blank=True, null=True, verbose_name='链接'),
        ),
    ]