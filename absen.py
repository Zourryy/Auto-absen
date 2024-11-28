import os
import schedule
import time
from datetime import datetime

def jalankan_absen_masuk():
    # Jalankan absen_masuk.py
    print(f"{datetime.now()}: Menjalankan absen_masuk.py")
    os.system("python absen_masuk.py")

def jalankan_absen_pulang():
    # Jalankan absen_pulang.py
    print(f"{datetime.now()}: Menjalankan absen_pulang.py")
    os.system("python absen_pulang.py")

# Atur jadwal dari Senin hingga Jumat
schedule.every().monday.at("06:50").do(jalankan_absen_masuk)
schedule.every().tuesday.at("06:50").do(jalankan_absen_masuk)
schedule.every().wednesday.at("06:50").do(jalankan_absen_masuk)
schedule.every().thursday.at("06:50").do(jalankan_absen_masuk)
schedule.every().friday.at("06:50").do(jalankan_absen_masuk)

schedule.every().monday.at("16:00").do(jalankan_absen_pulang)
schedule.every().tuesday.at("15:15").do(jalankan_absen_pulang)
schedule.every().wednesday.at("15:15").do(jalankan_absen_pulang)
schedule.every().thursday.at("15:15").do(jalankan_absen_pulang)
schedule.every().friday.at("14:45").do(jalankan_absen_pulang)

print("Scheduler aktif...")

while True:
    # Periksa apakah ada tugas yang harus dijalankan
    schedule.run_pending()
    time.sleep(1)