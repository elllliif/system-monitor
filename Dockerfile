FROM python:3.10-slim

WORKDIR /app

# Gerekli python kütüphanelerini doğrudan kur
RUN pip install --no-cache-dir psutil schedule

# Python scriptini kopyala
COPY send_email.py .

# Scripti çalıştır
CMD ["python", "send_email.py"]
