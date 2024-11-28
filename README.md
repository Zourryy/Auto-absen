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
   pkg install python -y

3. Clone repository
Clone repository proyek ini dengan perintah:

```bash
git clone https://github.com/Zourryy/Auto-absen
```


4. Izinkan akses penyimpanan di Termux
Jalankan perintah berikut untuk mengizinkan Termux mengakses penyimpanan perangkat:

```bash
termux-setup-storage
```

5. Perbarui dan tingkatkan paket Termux
Jalankan perintah berikut untuk memastikan sistem up-to-date:

```bash
yes | pkg update -y && yes | pkg upgrade -y
```

6. Install pip
Pasang Python package manager dengan perintah berikut:

```bash
yes | pkg install python-pip -y
```

7. Install Selenium
Pasang Selenium versi 4.9.1 menggunakan pip:

```bash
pip install selenium==4.9.1
```

8. Pasang Chromium dan dependensi lainnya
Install repository tambahan dan browser Chromium:

```bash
yes | pkg install x11-repo -y
yes | pkg install tur-repo -y
yes | pkg install chromium -y
```


Penjelasan Singkat

pkg install python -y: Memasang Python ke dalam Termux untuk menjalankan script Python.

git clone: Mengunduh repository script dari GitHub.

termux-setup-storage: Mengizinkan Termux mengakses penyimpanan perangkat.

pkg update && pkg upgrade: Memastikan semua paket di Termux diperbarui ke versi terbaru.

pip install selenium: Memasang pustaka Selenium versi tertentu.

pkg install chromium: Memasang browser Chromium yang digunakan oleh Selenium untuk otomatisasi.


Cara Menjalankan Script

1. Masuk ke direktori script:

```
cd Auto-absen
```

2. Jalankan script Python:
```
python absen.py
```

3. Masukkan informasi yang diperlukan ketika diminta:
4. contoh

Nama sekolah :SMKN 3 Kuningan

Username akun sekolah:(biasanya username akun sekolahan id di ambil dari NISN)

Password akun sekolah:(password biasanya tahun/bulan/tanggal lahir exmp (yy/mm/dd))


Setelah itu, script akan secara otomatis melakukan proses absensi sesuai dengan jadwal yang ditentukan.
