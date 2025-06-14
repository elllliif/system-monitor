# Python'un hafif bir sürümünü temel alıyoruz
FROM python:3.10-slim

# Çalışma dizinimizi /app yapıyoruz
WORKDIR /app

# send_email.py dosyasını konteynıra kopyalıyoruz
COPY send_email.py .

# Gerekli Python paketi psutil'i yüklendi
RUN pip install psutil

# Container başladığında çalışacak komut
CMD ["python", "send_email.py"]
