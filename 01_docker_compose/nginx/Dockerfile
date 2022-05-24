FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/
COPY ./conf.d/site.conf /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;"]