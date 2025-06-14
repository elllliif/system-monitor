import psutil
import time
import smtplib
from email.mime.text import MIMEText

# SMTP ayarları
SMTP_SERVER = "smtp.ethereal.email"  
SMTP_PORT = 587
SMTP_USER = "elias.homenick77@ethereal.email"
SMTP_PASS = "w2eCZCdg4hB3uvTfSF"

FROM_EMAIL = SMTP_USER
TO_EMAIL = "elif772017@gotmail.com"  # raporun gideceği mail


def get_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return f"CPU Kullanımı: {cpu}%\nRAM Kullanımı: {memory}%"

def send_email(body):
    msg = MIMEText(body)
    msg['Subject'] = 'Sistem Kaynak Kullanımı Raporu'
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

def main():
    while True:
        usage_report = get_system_usage()
        print("Rapor gönderiliyor:\n", usage_report)
        try:
            send_email(usage_report)
            print("Mail gönderildi.")
        except Exception as e:
            print("Mail gönderilemedi:", e)
        time.sleep(300)  # 5 dakika bekle

if __name__ == "__main__":
    main()
