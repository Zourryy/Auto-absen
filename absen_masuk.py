import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Fungsi untuk membaca data dari file konfigurasi
def load_credentials():
    with open("config.json", "r") as file:
        data = json.load(file)
    return data

# Memuat data akun
credentials = load_credentials()
username = credentials["username"]
password = credentials["password"]
nama_sekolah = credentials["nama_sekolah"]

# Setup driver dan fungsi lainnya
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Fungsi untuk mengetikkan nama sekolah dengan delay 0.5 detik per huruf
def ketik_nama_sekolah(sekolah_input, nama_sekolah):
    for char in nama_sekolah:
        sekolah_input.send_keys(char)
        time.sleep(0.5)

# Fungsi untuk memilih sekolah dan mengklik setelah mengetik
def pilih_sekolah(driver, nama_sekolah):
    sekolah_input = driver.find_element(By.XPATH, '//*[@id="input-26"]')
    ketik_nama_sekolah(sekolah_input, nama_sekolah)
    time.sleep(2)
    try:
        hasil_sekolah = driver.find_element(By.XPATH, '//*[@id="list-item-48-0"]/div/div')
        hasil_sekolah.click()
        print("Sekolah berhasil dipilih!")
    except Exception as e:
        print(f"Error saat memilih sekolah: {e}")

# Fungsi absensi masuk
def absen_masuk(driver, username, password, nama_sekolah):
    driver.get("https://student.sekolahan.id/login")
    pilih_sekolah(driver, nama_sekolah)
    time.sleep(3)

    username_input = driver.find_element(By.XPATH, '//*[@id="input-31"]')
    password_input = driver.find_element(By.XPATH, '//*[@id="input-34"]')
    username_input.send_keys(username)
    password_input.send_keys(password)

    submit_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div/button')
    submit_button.click()

    time.sleep(10)

    # Menekan tombol absen masuk
    try:
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)
        absen_masuk_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[1]/div/div/div[1]/button[1]/span')
        absen_masuk_button.click()
        print("Tombol absen masuk berhasil diklik!")
        time.sleep(10)
    except Exception as e:
        print(f"Error saat menekan tombol absen masuk: {e}")

# Menjalankan absensi
driver = setup_driver()
absen_masuk(driver, username, password, nama_sekolah)
