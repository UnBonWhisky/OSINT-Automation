FROM python:alpine3.10

ENV PYTHONIOENCODING=utf-8

COPY . /app

WORKDIR /app

RUN apk add build-base libffi-dev && \
    /usr/local/bin/python -m pip install --upgrade pip && \
    pip install --default-timeout=900 -r requirements.txt

EXPOSE 1202

CMD ["python", "main.py"]