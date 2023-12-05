FROM ubuntu
RUN apt-get update
RUN apt install  -y apache2 
WORKDIR app
COPY . . 
EXPOSE 80

