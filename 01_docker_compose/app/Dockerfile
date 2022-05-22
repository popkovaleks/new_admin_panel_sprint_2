FROM python:3
WORKDIR /usr/src/app
copy requirements.txt ./

run pip3 install --no-cache-dir -r requirements.txt

copy . .
EXPOSE 8000/tcp
cmd sleep 5 && python manage.py migrate --fake movies && python manage.py migrate && python manage.py collectstatic --no-input  && gunicorn config.wsgi -b 0.0.0.0:8000