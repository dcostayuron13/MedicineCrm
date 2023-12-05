FROM ubuntu
RUN apt-get update
RUN apt install  -y apache2 
WORKDIR app
COPY . . 
python manage.py migrate
EXPOSE 80

