FROM python:3.10-slim-buster

WORKDIR /streaming

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /streaming/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /streaming
