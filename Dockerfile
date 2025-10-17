FROM python:3.11-slim

WORKDIR /app

ENV PIP_NO_CACHE_DIR=1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY artifacts/ /app/artifacts/
COPY app/ /app/app/

ENTRYPOINT ["python", "-m", "app.run"]
