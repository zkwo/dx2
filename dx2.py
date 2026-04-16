import json
import os
import time
import sys

# KONFIGURASI WARNA
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[35m"
BLUE = "\033[34m"

# FUNGSI MEMBERSIHKAN LAYAR
def clear():
    os.system("clear")

# BANNER DARI KODE 2
def banner():
    clear()
    print(PURPLE + "⣿⡟⠁     ⠨⠝⣿⣿⣿⣿⣿⣿⡛⠭⠈⠹⣿⣿" + RESET)
    print(PURPLE + "⣿⣴⣶⣶⣦⣄  ⠈⢻⣿⣿⣿⢻⠁⣤⣶⣶⣶⣼⣿" + RESET)
    print(PURPLE + "⣿⣿⡿⢟⡛⠟⠿⢆⢻⣿⣿⣿⢧⠾⠛⠟⣛⢿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⢛⡁      ⢀⣿⣿⣿⣿⣇    ⠁⣙⠻⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣶⣷⣿⣿⠟⣿⣿⣿⠿⣿⣷⣷⣾⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣿⣿⠿⢫⡄⣿⣿⣿⣦⣝⢿⣿⣿⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⡧⢙⠛⣛⣭⣴⣧⡛⢿⠿⠿⠿⢗⣥⣶⣬⣟⠛⡛⢡⣿" + RESET)
    print(PURPLE + "⣿⡆⢣⡈⠻⣿⠿⠿⠁⢉⡉⠈⠻⠿⢿⡿⠋⡰⢁⣾⣿" + RESET)
    print(PURPLE + "⣿⣿⣆⢑⢤⣤⣤⡄⢀⣚⣛⢂⢀⣤⣤⣤⠜⢁⣾⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣦⡻⣾⣿⣿⣷⠸⠿⢃⣼⣿⣿⡾⣡⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣿⣶⡹⢿⣿⡇  ⢸⣿⡿⣟⣽⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣿⣿⣿⣷⣾⣇⡀⢀⣼⣴⣾⣿⣿⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿" + RESET)
    print(RED + " ___ __  __      ___   ___  ___  _  _  _____" + RESET) 
    print(RED + "/ __|\ \/ /___  / _ \ / __||_ _|| \| ||_   _|" + RESET)
    print(RED + "\__ \ >  <|___|| (_) |\__ \ | | | .` |  | |" + RESET)  
    print(RED + "|___//_/\_\     \___/ |___/|___||_|\_|  |_|" + RESET)                                             
    print(CYAN + "===============================================================" + RESET)
    print(BLUE + "Status : ACTIVE | Terminal Tracking System" + RESET)
    print(CYAN + "---------------------------------------------------------------" + RESET)

# EFEK LOADING
def loading_anim(text):
    sys.stdout.write(YELLOW + text)
    for _ in range(3):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(RESET)

# EFEK SCANNING DARI KODE 1
def scan_effect(target):
    print(f"\n{CYAN}[*] INITIATING TRACKING ON: {target}{RESET}")
    time.sleep(1)
    text = "[ SCANNING DATABASE & CELLULAR TOWER ]"
    for c in text:
        sys.stdout.write(GREEN + c + RESET)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

    for i in range(0, 101, 25):
        print(f"{YELLOW}>> LOCALIZING DATA: {i}%{RESET}")
        time.sleep(0.4)
    print(GREEN + "[✓] DATA FOUND!" + RESET)
    time.sleep(1)

# LOAD DATABASE JSON
def load_db():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(RED + "[!] Error: data.json tidak ditemukan!" + RESET)
        return None
    except json.JSONDecodeError:
        print(RED + "[!] Error: Format data.json rusak!" + RESET)
        return None

# FUNGSI UTAMA PARSING
def parse_nik(nik, data):
    if not nik.isdigit() or len(nik) != 16:
        print(RED + "\n[!] ERROR: NIK TIDAK VALID (HARUS 16 DIGIT)" + RESET)
        return

    # Logika Potong String NIK
    tanggal = nik[6:8]
    bulan = nik[8:10]
    tahun = nik[10:12]
    prov_code = nik[0:2]
    kab_code = nik[0:4]
    kec_code = nik[0:6]
    uniq = nik[12:16]

    # Cek Jenis Kelamin
    cekjk = int(nik[6:8])
    jk = "LAKI-LAKI" if cekjk <= 40 else "PEREMPUAN"
    
    # Jika perempuan, tanggal lahir di NIK ditambah 40
    if cekjk > 40:
        real_tgl = cekjk - 40
        tanggal = str(real_tgl).zfill(2)

    # Ambil data dari JSON
    provinsi = data.get("provinsi", {}).get(prov_code, "Tidak Diketahui")
    kabkot = data.get("kabkot", {}).get(kab_code, "Tidak Diketahui")
    kec_raw = data.get("kecamatan", {}).get(kec_code, "Tidak Diketahui--N/A")

    if "--" in kec_raw:
        kec_name, pos = kec_raw.split("--")
    else:
        kec_name, pos = kec_raw, "N/A"

    # TAMPILAN HASIL AKHIR
    print("\n" + RED + ">>> [ TARGET IDENTIFIED ] <<<" + RESET)
    print(CYAN + "-----------------------------" + RESET)
    print(f"{GREEN} Tanggal Lahir : {tanggal}-{bulan}-{tahun}{RESET}")
    print(f"{GREEN} Jenis Kelamin : {jk}{RESET}")
    print(f"{GREEN} Provinsi      : {provinsi}{RESET}")
    print(f"{GREEN} Kab/Kota      : {kabkot}{RESET}")
    print(f"{GREEN} Kecamatan     : {kec_name.strip()}{RESET}")
    print(f"{GREEN} Kode Pos      : {pos.strip()}{RESET}")
    print(f"{GREEN} 𝗨𝗻𝗶𝗾 𝗖𝗼𝗱𝗲   : {uniq}{RESET}")
    print(CYAN + "-----------------------------" + RESET)

def main():
    db = load_db()
    if not db:
        return

    banner()
    
    # PROSES 1: Input Nomor HP (Simulasi)
    nomor_hp = input(YELLOW + "\n[?] Input Nomor Target: " + RESET)
    loading_anim("Searching Signal")
    scan_effect(nomor_hp)
    
    # PROSES 2: Menampilkan NIK "Hasil Lacak" 
    # (Di sini user diminta input NIK yang didapat)
    print(f"\n{PURPLE}[!] Signal Locked on Device Linked to NIK{RESET}")
    nik_input = input(RED + "[>] Enter Linked NIK to Decrypt: " + RESET)
    
    loading_anim("Decrypting Identity")
    
    # PROSES 3: Parsing Data
    parse_nik(nik_input, db)
    
    print(YELLOW + "\nScan Selesai. Tekan Enter untuk keluar..." + RESET)
    input()

if __name__ == "__main__":
    main()
