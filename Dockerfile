FROM python:3.10-slim-bookworm

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip &&  \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /usr/src/app/entrypoint.sh
