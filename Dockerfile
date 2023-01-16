FROM python:alpine3.16

ENV PYTHONIOENCODING=utf-8

COPY . /app

WORKDIR /app

RUN apk add build-base libffi-dev && \
    /usr/local/bin/python -m pip install --upgrade pip && \
    pip install --default-timeout=900 -r requirements.txt

CMD ["python3", "main.py"]