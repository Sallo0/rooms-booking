FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH=/usr/src/app/src

RUN apt update && apt install make

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install -r requirements.txt

COPY . .