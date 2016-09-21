#!/usr/bin/env bash

nohup ~/Env/py3/bin/gunicorn --workers=5 mysite.wsgi:application &
