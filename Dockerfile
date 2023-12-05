FROM ubuntu
RUN sudo apt update 
RUN sudo apt install -y apache2 
WORKDIR app
COPY . . 
EXPOSE 80

