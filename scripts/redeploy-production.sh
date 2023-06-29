#!/bin/bash

git pull origin main

python manage.py migrate --settings "url_shortner.production_settings"
python manage.py collectstatic --noinput --settings "url_shortner.production_settings"

sudo apache2ctl restart