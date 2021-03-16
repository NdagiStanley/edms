FROM python:3.7-slim-buster
LABEL maintainer="ndagis@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt && rm -rf /root/.cache/pip/

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser --disabled-password --gecos "" user
USER user
