FROM python:3.7-alpine
MAINTAINER Angel Rojas

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /apiuser
WORKDIR /apiuser
COPY ./apiuser /apiuser

RUN adduser -D user
USER user

