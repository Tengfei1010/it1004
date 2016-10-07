#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 9/21/16.
"""
import urllib

from django import template

register = template.Library()


@register.filter(name='divide')
def divide(value, arg):
    try:
        return int(value) / int(arg)
    except:
        return None


@register.filter(name='mod')
def mod(value, arg):
    try:
        return int(value) % int(arg)
    except:
        return None


@register.simple_tag(name='url_replace')
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
