#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 9/18/16.
"""
from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'category/(?P<category_id>[0-9]+)/$', views.list_category_article_view, name='category'),
    url(r'recent/(?P<days>\d+)/$', views.list_recent_articles_view, name='recent'),
    url(r'author/(?P<author_id>[0-9]+)/$', views.list_author_article_view, name='author'),
    url(r'search/$', views.list_search_article_view, name='search')
]
