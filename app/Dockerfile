# Dockerfile in ~/prima-sre-challenge/app

FROM python:3.12-slim
WORKDIR /app

# COPY from src folder (relative to app)
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

