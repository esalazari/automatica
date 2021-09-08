FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/app/automaticaing

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./ /app/