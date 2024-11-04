import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# URL halaman absensi
URL_ABSEN = "https://student.sekolahan.id/"
URL_LOGIN = "https://student.sekolahan.id/login"

# Cookie login yang sudah kamu miliki
cookies = {
    "_ga_RK58RM9LJ2": "GS1.2.1723733070.1.0.1723733070.0.0.0",  # Sesuaikan nama dan nilai cookie
    "_ga": "GA1.1.541079114.1723733070",
    "G_ENABLED_IDPS": "google", 
    "_ga_PMQHBDYVCC": "GS1.1.1730537849.7.1.1730538679.0.0.0", 
}

# Buat sesi dengan cookie
session = requests.Session()
session.cookies.update(cookies)

# Fungsi untuk memeriksa login
def cek_login():
    response = session.get(URL_ABSEN)
    soup = BeautifulSoup(response.text, "html.parser")

    # Cek apakah kita berada di halaman login
    if "Masuk" in soup.text:  # Sesuaikan dengan teks yang ada di halaman login
        print("Anda belum login, harap masukkan cookie.")
        return False
    return True

# Fungsi untuk absen masuk
def absen_masuk():
    response = session.get(URL_ABSEN)
    soup = BeautifulSoup(response.text, "html.parser")
    # Menggunakan class untuk mencari tombol absen masuk
    absen_masuk_button = soup.find("button", {"class": "ma-2 v-btn v-btn--elevated v-btn--has-bg theme--light v-size--large"})
    
    if absen_masuk_button and "Presensi Mulai" in absen_masuk_button.get_text():
        # Simulasikan klik pada tombol absen masuk
        print("Absensi masuk berhasil dilakukan.")
    else:
        print("Gagal absen masuk, tombol tidak ditemukan atau belum aktif.")

# Fungsi untuk absen pulang
def absen_pulang():
    response = session.get(URL_ABSEN)
    soup = BeautifulSoup(response.text, "html.parser")
    # Menggunakan class dan teks tombol untuk mencari tombol absen pulang
    absen_pulang_button = soup.find("button", {"class": "ma-2 v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--large secondary"})
    
    if absen_pulang_button and "Presensi Selesai" in absen_pulang_button.get_text():
        # Simulasikan klik pada tombol absen pulang
        print("Absensi pulang berhasil dilakukan.")
    else:
        print("Gagal absen pulang, tombol tidak ditemukan atau belum aktif.")


# Waktu absen berdasarkan hari
waktu_absen = {
    "Monday": {"masuk": "06:50", "pulang": "16:00"},
    "Tuesday": {"masuk": "06:53", "pulang": "15:19"},
    "Wednesday": {"masuk": "06:55", "pulang": "15:20"},
    "Thursday": {"masuk": "06:45", "pulang": "15:17"},
    "Friday": {"masuk": "06:56", "pulang": "14:30"},
}

# Absen otomatis berdasarkan jadwal
def absen_otomatis():
    # Loop untuk mengecek waktu
    while True:
        sekarang = datetime.now()
        hari = sekarang.strftime("%A")  # Ambil nama hari, misal "Monday", "Tuesday", dst.
        jam_sekarang = sekarang.strftime("%H:%M")

        # Cek apakah hari adalah Senin-Jumat
        if hari in waktu_absen:
            if cek_login():  # Cek apakah sudah login
                # Ambil waktu absensi untuk hari ini
                waktu_hari_ini = waktu_absen[hari]
                waktu_absen_masuk = waktu_hari_ini["masuk"]
                waktu_absen_pulang = waktu_hari_ini["pulang"]

                # Absen masuk
                if jam_sekarang == waktu_absen_masuk:
                    absen_masuk()
                    time.sleep(60)  # Hindari loop berulang dalam satu menit

                # Absen pulang
                elif jam_sekarang == waktu_absen_pulang:
                    absen_pulang()
                    time.sleep(60)

        # Tunggu 30 detik sebelum cek waktu lagi
        time.sleep(30)

# Jalankan fungsi absen otomatis
absen_otomatis()
