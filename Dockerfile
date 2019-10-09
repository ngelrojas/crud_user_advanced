FROM python:3.7-alpine
MAINTAINER Angel Rojas

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev \
        jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        tk-dev \
        tcl-dev \
        harfbuzz-dev \
        fribidi-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /apiuser
WORKDIR /apiuser
COPY ./apiuser /apiuser

RUN adduser -D user
USER user

