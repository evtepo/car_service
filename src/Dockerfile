FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get -y install netcat-traditional \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY docker/launch.sh .
COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "launch.sh"]