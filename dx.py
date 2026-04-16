import json
import os
import time
import sys
import requests # Pastikan sudah install: pip install requests

# KONFIGURASI WARNA
R = "\033[31m" # Red
G = "\033[32m" # Green
Y = "\033[33m" # Yellow
C = "\033[36m" # Cyan
P = "\033[35m" # Purple
W = "\033[0m"  # White

# --- CONFIG API ---
# Ganti dengan URL API dan Key yang kamu punya
API_ENDPOINT = "https://api.internal-database.com/search" 
API_KEY = "MASUKKAN_API_KEY_KAMU_DISINI"

def banner():
    os.system("clear")
    print(f"{P}╔══════════════════════════════════════════╗")
    print(f"{P}║ {W}      TERMINAL TRACKER PRO (API)      {P} ║")
    print(f"{P}╚══════════════════════════════════════════╝{W}")

def loading(text):
    sys.stdout.write(f"{Y}[~] {text}")
    for _ in range(3):
        time.sleep(0.4)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"{W}")

def get_data_from_api(phone):
    """Fungsi untuk mengambil NIK dari API berdasarkan No HP"""
    loading(f"Requesting data for {phone}")
    
    # Simulasi Request ke API (Sesuaikan dengan dokumentasi API-mu)
    try:
        # Contoh jika menggunakan request asli:
        # response = requests.get(f"{API_ENDPOINT}?phone={phone}&key={API_KEY}")
        # data = response.json()
        # return data['nik']
        
        time.sleep(1) # Simulasi delay network
        # Ini adalah NIK dummy jika API belum dikoneksikan
        return "3275011212950001" 
    except Exception as e:
        print(f"{R}[!] Connection Error: {e}{W}")
        return None

def parse_nik_local(nik, db):
    """Fungsi membedah NIK menggunakan data.json lokal"""
    print(f"{G}[+] Decrypting NIK: {nik}{W}")
    
    prov_code = nik[0:2]
    kab_code = nik[0:4]
    kec_code = nik[0:6]
    
    prov = db.get("provinsi", {}).get(prov_code, "Unknown")
    kab = db.get("kabkot", {}).get(kab_code, "Unknown")
    kec_data = db.get("kecamatan", {}).get(kec_code, "Unknown--N/A")
    
    kec_name, pos = kec_data.split("--") if "--" in kec_data else (kec_data, "N/A")
    
    print(f"\n{C}========== RESULT FOUND ==========")
    print(f"{W}NIK      : {G}{nik}")
    print(f"{W}PROVINSI : {G}{prov}")
    print(f"{W}KOTA/KAB : {G}{kab}")
    print(f"{W}KECAMATAN: {G}{kec_name}")
    print(f"{W}KODE POS : {G}{pos}")
    print(f"{C}=================================={W}")

def main():
    # Load Database Lokal
    try:
        with open("data.json", "r") as f:
            db = json.load(f)
    except:
        print(f"{R}[!] File data.json tidak ditemukan!{W}")
        return

    banner()
    
    # 1. Input Nomor HP
    target_phone = input(f"{C}[?] Masukkan No HP Target: {W}")
    
    # 2. Ambil NIK secara otomatis via API
    nik_result = get_data_from_api(target_phone)
    
    if nik_result:
        print(f"{G}[✓] NIK Terdeteksi: {nik_result}{W}")
        time.sleep(1)
        
        # 3. Bedah NIK tersebut secara detail
        loading("Memproses detail alamat dari database lokal")
        parse_nik_local(nik_result, db)
    else:
        print(f"{R}[!] Data tidak ditemukan di server API.{W}")

    print(f"\n{Y}Tekan Enter untuk kembali...{W}")
    input()

if __name__ == "__main__":
    main()
