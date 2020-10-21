# pull official base image
FROM python:3.8.6
# set work directory
WORKDIR /Users/a12345/Desktop
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies

RUN pip install --upgrade pip
RUN pip install psycopg2
COPY ./requirements.txt .


# copy project
COPY . .  