FROM python:3.10.0-alpine
RUN apk update 
RUN apk add apache2
WORKDIR app
COPY . . 
EXPOSE 80

