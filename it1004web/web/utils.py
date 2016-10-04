#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 9/17/16.
"""
import os
import uuid


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.directory_string_var, filename)
