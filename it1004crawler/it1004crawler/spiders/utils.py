#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 9/25/16.
"""
from hashlib import md5


def encode_utf8(string):
    return string.encode('utf-8')


def get_md5_digest(string):
    return md5(string.encode('utf-8')).hexdigest()
