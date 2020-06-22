FROM python:3.7.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PIP_FORMAT=legacy

RUN apt-get -y update && apt-get install -y python-pip python-dev libzbar-dev bash \
    gcc python3-dev git libc-dev

RUN echo 'deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main' >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends apt-utils

RUN apt-get install -y netcat && apt-get autoremove -y

RUN adduser --disabled-password --gecos '' myuser

# RUN groupadd -r xuzer && useradd -r -g xuzer xuzer

RUN pip install --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN pip install --no-cache-dir jupyterlab

RUN mkdir -p /main

WORKDIR /main

COPY ./dockerfiles/py/bootWeb.sh /bootWeb.sh
RUN chmod +x /bootWeb.sh

# Jupyter
COPY ./dockerfiles/py/jupyter_run.sh /jupyter_run.sh
RUN chmod +x /jupyter_run.sh