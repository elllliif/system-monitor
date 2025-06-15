FROM python:3.10-slim

WORKDIR /app

# Gerekli python kütüphanelerini doğrudan kur
RUN pip install --no-cache-dir psutil schedule

# Python scriptini kopyala
COPY sistem_raporu.py .

# Scripti çalıştır
CMD ["python", "sistem_raporu.py"]
