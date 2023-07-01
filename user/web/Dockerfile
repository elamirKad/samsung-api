FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /user

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
