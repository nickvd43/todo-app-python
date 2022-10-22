# Todo-app API in python

This repo contains an API build with python using the fastAPI libary.
The API is build on top of a MySQL database. This app can be used by a front-end
application to create, read, update and delete todo items. The application has been 
containerized in docker to allow everyone to easily use the API. 

A docker-compose.yml is set up to run both the database and the API on your local machine

# How to use

To run the API and database using docker compose you will need to install docker: https://docs.docker.com/get-docker/ 

If you have installed docker you will need to pull the repository from git and open a terminal window in your local folder containing the project files. In your terminal run the following command: 

`docker build -t myapiforcompose .` 

This will create a docker image from the dockerfile that is present in the project folder. After that process is done you can simply run the following command:

`docker-compose up`

And it will launch both the MySQL server and the API. There is a test.py file present with some basic requests so you can test it out yourself. 

