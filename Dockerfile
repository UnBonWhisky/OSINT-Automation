FROM python:alpine3.10

COPY . /app

WORKDIR /app

RUN apk add build-base libffi-dev gfortran openblas-dev && \
    /usr/local/bin/python -m pip install --upgrade pip && \
    pip install --default-timeout=900 -r requirements.txt

EXPOSE 8500

CMD ["python", "main.py"]