FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH=/usr/src/booking/app

RUN apt update && apt install make

WORKDIR /usr/src/booking

COPY requirements.txt /usr/src/booking/

RUN pip install -r requirements.txt

COPY . .