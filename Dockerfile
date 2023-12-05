FROM ubuntu
RUN apt-get update
RUN apt install  -y apache2 
ADD . /var/www/html
EXPOSE 80
ENTRYPOINT apachectl -D FOREGROUND
ENV name CognCise
