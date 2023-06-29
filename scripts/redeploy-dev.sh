#!/bin/bash

git pull origin main

python manage.py migrate
python manage.py collectstatic

sudo apache2ctl restart