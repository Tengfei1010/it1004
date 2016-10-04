#!/usr/bin/env bash

nohup ~/Env/py3env/bin/gunicorn -b 0.0.0.0:8000 --workers=5 mysite.wsgi:application &
