# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 02:13
from __future__ import unicode_literals

import beeblog.utils
import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=datetime.datetime.now(), verbose_name='创建时间')),
                ('updated', models.DateTimeField(blank=True, default=None, null=True, verbose_name='修改时间')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('tread', models.BigIntegerField(default=0, verbose_name='踩')),
                ('support', models.BigIntegerField(default=0, verbose_name='赞')),
                ('views', models.BigIntegerField(default=0, verbose_name='浏览数')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=datetime.datetime.now(), verbose_name='创建时间')),
                ('updated', models.DateTimeField(blank=True, default=None, null=True, verbose_name='修改时间')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('name', models.CharField(max_length=100, verbose_name='作者名称')),
                ('url', models.CharField(max_length=200, verbose_name='作者链接')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=beeblog.utils.get_file_path, verbose_name='作者头像')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=datetime.datetime.now(), verbose_name='创建时间')),
                ('updated', models.DateTimeField(blank=True, default=None, null=True, verbose_name='修改时间')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('category_text', models.CharField(max_length=20, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beeblog.Author', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='beeblog.Category', verbose_name='文章分类'),
        ),
    ]
