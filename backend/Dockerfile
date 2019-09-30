FROM python:3.7-alpine as alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY . /code/

RUN apk update                                  \
    && apk add --no-cache                       \
                       curl                     \
                       bash                     \
                       gettext                  \
    && apk add --no-cache --virtual .build-deps \
                       zlib                     \
                       libpq                    \
                       git                      \
                       # Pillow deps
    && pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && apk --purge del .build-deps
