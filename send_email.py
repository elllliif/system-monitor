import psutil           # Sistem kaynaklarını almak için
import schedule         # Zamanlama yapmak için
import time             # Uyku (bekleme) fonksiyonu için
import smtplib          # SMTP protokolü ile mail göndermek için
from email.mime.text import MIMEText         # E-posta içeriği oluşturmak için
from email.mime.multipart import MIMEMultipart # Çoklu içerik için (text + html vb.)


# SMTP sunucu ayarları (Ethereal test hesabı bilgileri)
SMTP_SERVER = "smtp.ethereal.email"  
SMTP_PORT = 587
SMTP_USER = "juana.yost68@ethereal.email"
SMTP_PASS = "8bC8QzFQSatKvbrU6X"

# Gönderen ve alıcı e-posta adresleri
FROM_EMAIL = SMTP_USER
TO_EMAIL = "elif772017@gotmail.com"  # Raporun gönderileceği mail adresi


# Sistem kaynaklarını ölçen fonksiyon
def get_system_info():
    # CPU kullanım yüzdesini 1 saniye aralıkla ölç
    cpu = psutil.cpu_percent(interval=1)
    # RAM bilgilerini al
    memory = psutil.virtual_memory()
    # Disk kullanım bilgilerini al (ana dizin /)
    disk = psutil.disk_usage('/')

    # Bilgileri okunabilir formatta hazırla
    info = f"""
    SYSTEM RESOURCE USAGE

    CPU Usage: {cpu}%
    RAM Usage: {memory.percent}% (Used: {memory.used / (1024 ** 3):.2f} GB / Total: {memory.total / (1024 ** 3):.2f} GB)
    Disk Usage: {disk.percent}% (Used: {disk.used / (1024 ** 3):.2f} GB / Total: {disk.total / (1024 ** 3):.2f} GB)
    """
    return info

# E-posta gönderme fonksiyonu
def send_email(subject, body):
    # E-posta mesajını oluştur (gönderen, alıcı, konu)
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    # Mesaj gövdesini ekle 
    
    msg.attach(MIMEText(body, "plain"))

    try:
        # SMTP sunucusuna bağlan
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # Bağlantıyı TLS ile güvenli hale getir
        server.starttls()
        # SMTP sunucusunda oturum aç (kullanıcı adı + parola)
        server.login(SMTP_USER, SMTP_PASS)
        # E-postayı gönder
        server.send_message(msg)
        # Bağlantıyı kapat
        server.quit()
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        # Hata olursa ekrana yazdır
        print("E-posta gönderilemedi:", str(e))

# 5 dakikada bir çalışacak görev
def job():
    print("Sistem kaynakları kontrol ediliyor...")
    info = get_system_info()                  # Sistem bilgisini al
    send_email("🔔 Sistem Kaynak Raporu", info)  # E-posta gönder

# Her 5 dakikada bir job fonksiyonunu planla
schedule.every(5).minutes.do(job)

print("Servis başlatıldı. Her 5 dakikada bir sistem raporu gönderilecek.")

# Sonsuz döngü - program çalıştığı sürece devam eder
while True:
    schedule.run_pending()  # Zamanı gelmiş işleri çalıştır
    time.sleep(1)           # CPU kullanımını azaltmak için 1 saniye bekle
