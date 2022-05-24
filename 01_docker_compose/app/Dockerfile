FROM python:3.10
WORKDIR /usr/src/app
copy requirements.txt ./

run pip3 install --no-cache-dir -r requirements.txt

copy . .
EXPOSE 8000/tcp

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]