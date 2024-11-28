# Auto Absen

Sebuah script Python sederhana untuk melakukan absensi otomatis di sistem sekolah berbasis web. Script ini dirancang agar dapat berjalan di perangkat Android menggunakan Termux.

## Persyaratan

- Termux (unduh di [F-Droid](https://f-droid.org/packages/com.termux/))
- Python 3.9 atau lebih baru
- Selenium 4.9.1
- Chromium untuk menjalankan browser dalam mode headless

## Instalasi

Ikuti langkah-langkah berikut untuk mengatur script ini:

1. **Unduh dan pasang Termux**  
   Unduh Termux dari [link ini](https://f-droid.org/packages/com.termux/).

2. **Install Python**  
   Buka Termux dan ketikkan perintah berikut:  
   ```bash
   pkg install python

3. Clone repository
Clone repository proyek ini dengan perintah:

git clone https://github.com/Zourryy/Auto-absen


4. Izinkan akses penyimpanan di Termux
Jalankan perintah berikut untuk mengizinkan Termux mengakses penyimpanan perangkat:

termux-setup-storage


5. Perbarui dan tingkatkan paket Termux
Jalankan perintah berikut:

yes | pkg update -y && yes | pkg upgrade -y


6. Install pip
Pasang Python package manager dengan perintah berikut:

yes | pkg install python-pip -y


7. Install Selenium
Pasang Selenium versi 4.9.1:

pip install selenium==4.9.1


8. Pasang Chromium dan dependensi lainnya
Install repository tambahan dan browser Chromium:

yes | pkg install x11-repo -y
yes | pkg install tur-repo -y
yes | pkg install chromium -y



Penjelasan Singkat

Selenium digunakan untuk mengontrol browser dan melakukan otomatisasi pada halaman web absensi.

Chromium adalah browser yang digunakan Selenium untuk melakukan tugas ini dalam mode headless.

Perintah di atas memastikan semua dependensi dipasang dan sistem diperbarui.


Cara Menjalankan Script

1. Masuk ke direktori script:

cd Auto-absen


2. Jalankan script Python:

python absen.py


3. Masukkan informasi yang diperlukan ketika diminta:

Nama sekolah (misalnya: SMKN 3 Kuningan)

Username akun sekolahan.id

Password akun sekolahan.id


Setelah itu, script akan secara otomatis melakukan proses absensi sesuai dengan jadwal yang ditentukan.
