FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_VERSION=0.1.0

# security: non-root user
RUN groupadd -r app && useradd --no-log-init -r -g app app
WORKDIR /app

# deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# code
COPY src/ ./

EXPOSE 8000
USER app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
