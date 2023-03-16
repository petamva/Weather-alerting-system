FROM python:3.8.10-slim

LABEL maintainer="petros.tamvakis@athenarc.gr"

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY . /app

RUN chmod +x boot.sh

ENTRYPOINT ["./boot.sh"]
