FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir --upgrade pip

COPY . .

CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000