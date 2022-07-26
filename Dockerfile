FROM python:3.7-slim-buster

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src

COPY src/ /src/

COPY tests/ /tests/

WORKDIR /src

