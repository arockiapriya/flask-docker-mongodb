# source: https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5
# Dockerfile - this is a comment. Delete me if you want.

FROM python:3.7.3-alpine3.9

ADD . /app

WORKDIR /app

RUN apk update \
     && apk add libpq postgresql-dev \
     && apk add build-base

RUN pip install -r requirements.txt

EXPOSE 6002

CMD ["gunicorn", "-b", "0.0.0.0:6002", "application"]