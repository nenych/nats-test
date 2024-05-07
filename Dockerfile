FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY *.py ./

RUN pip install -r requirements.txt