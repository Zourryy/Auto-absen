Kode ini adalah skrip Python untuk melakukan absensi otomatis di situs web dengan autentikasi berbasis cookie. Skrip ini berfungsi untuk memeriksa status login, mencari tombol absensi masuk dan pulang, serta menjalankan absensi sesuai jadwal yang ditentukan.

### Fungsi Utama dan Kegunaan Kode

1. **cek_login()**: Memeriksa apakah pengguna sudah login atau belum dengan mengecek keberadaan teks "Masuk" pada halaman. Jika pengguna belum login, akan mengeluarkan pesan agar memasukkan cookie yang benar.

2. **absen_masuk()**: Mencari tombol "Presensi Mulai" di halaman web. Jika tombol ditemukan dan aktif, skrip akan memproses absensi masuk dan menampilkan pesan berhasil.

3. **absen_pulang()**: Sama seperti `absen_masuk`, tetapi mencari tombol "Presensi Selesai" untuk memproses absensi pulang.

4. **absen_otomatis()**: Melakukan absensi secara otomatis berdasarkan jadwal yang ditentukan. Skrip akan berjalan terus menerus, memeriksa waktu saat ini, dan melakukan absensi pada waktu yang sesuai.

### Library dan Dependensi yang Perlu Diinstal

Untuk menjalankan kode ini di Termux, Anda perlu menginstal Python serta library yang dibutuhkan:

1. **Python**: Bahasa pemrograman yang digunakan untuk menjalankan skrip.
   - Instal di Termux dengan:
     ```bash
     pkg install python
     ```

2. **requests**: Library untuk mengirim permintaan HTTP.
   - Instal dengan:
     ```bash
     pip install requests
     ```

3. **beautifulsoup4**: Library untuk melakukan parsing HTML dan mencari elemen pada halaman.
   - Instal dengan:
     ```bash
     pip install beautifulsoup4
     ```

### Cara Menggunakan Skrip

1. Masukkan cookie yang sesuai di variabel `cookies` dalam skrip.
2. Jalankan skrip dengan:
   ```bash
   python absen-sc.py
   ```
3. Skrip akan memeriksa waktu setiap 30 detik untuk memastikan bahwa absensi dilakukan tepat waktu sesuai jadwal.
