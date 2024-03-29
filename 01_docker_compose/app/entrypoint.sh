#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py migrate --fake movies
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn config.wsgi -b 0.0.0.0:8000

exec "$@"