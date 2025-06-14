FROM python:3.10-slim

# Çalışma dizini oluştur
WORKDIR /app

# Gerekli paketleri yükle
RUN pip install psutil

# Script dosyasını kopyala
COPY send_email.py .

# Container çalıştırıldığında scripti başlat
CMD ["python", "send_email.py"]
