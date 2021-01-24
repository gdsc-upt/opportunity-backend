#!/bin/sh

set -ex

python manage.py check --deploy
python manage.py collectstatic --no-input --verbosity 0
python manage.py makemigrations --check --dry-run || (echo "Run makemigrations before deploying." && false)
python manage.py migrate --no-input

APP_ROOT=/usr/app
chmod -R u=rwX,g=rX,o= ${APP_ROOT}/*
chown -RL root:django ${APP_ROOT}
chown -RL django:django ${APP_ROOT}/logs ${APP_ROOT}/media
find /usr/app -type d -exec chmod g+s {} +

export PORT=8000

imports='from administration.models import User;'
create_superuser='User.objects.create_superuser("admin", "admin@example.com", "admin") if not User.objects.all() else True'

echo "$imports $create_superuser" | python manage.py shell

su-exec django gunicorn main.wsgi --timeout 180 --log-file -
