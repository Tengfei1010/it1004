#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 9/21/16.
"""

from django.shortcuts import redirect


def index(request):
    return redirect('/blog')
