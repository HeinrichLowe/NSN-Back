# syntax=docker/dockerfile:1

FROM python:3.12-alpine

WORKDIR /app

RUN apk update && apk add --no-cache postgresql-client

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "./wait-for-db.sh"]
