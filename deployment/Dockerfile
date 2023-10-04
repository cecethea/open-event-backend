FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

# Allows docker to cache installed dependencies between builds
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY requirements-dev.txt requirements-dev.txt
RUN pip install -r requirements-dev.txt


COPY deployment/scripts /app/deployment/scripts

RUN chmod -R +x /app/deployment/scripts/*

COPY . ./