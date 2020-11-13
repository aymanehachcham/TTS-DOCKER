#!/bin/bash

set -e

python manage.py collectstatic --noinput

uswgi --socket :8000 --master --enable-threads --module ttsApi.wsgi