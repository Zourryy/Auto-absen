import json
import os

# Nama file konfigurasi
config_file = "config.json"

# Fungsi untuk memperbarui data akun di file config.json
def update_account():
    # Meminta input dari pengguna
    username = input("Masukkan username Sekolahan.id: ")
    password = input("Masukkan password Sekolahan.id: ")
    nama_sekolah = input("Masukkan nama sekolah: ")

    # Menyusun data yang akan disimpan ke dalam JSON
    data = {
        "username": username,
        "password": password,
        "nama_sekolah": nama_sekolah
    }

    # Menyimpan data ke file config.json
    with open(config_file, "w") as file:
        json.dump(data, file, indent=4)

    print("Data akun berhasil diperbarui!")

# Menjalankan fungsi update_account
if __name__ == "__main__":
    update_account()
