import sys
import time
import random
import string
import psutil
import os
import requests
import json
import urllib3
from colorama import init, Fore, Style

init(autoreset=True)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- 1. KONFIGURASI API KEY ---
a = "sk-or-v1-7995770d42"
b = "78c5cbb2d0ab4335adf3"
c = "b69dfff451870ce8"
d = "9f73cf8b7a9544ce02"

OPENROUTER_API_KEY = a + b + c + d
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

# --- 2. FUNGSI AKSES LLM (MULTI-MODEL INTELLIGENCE) ---
def tanya_llm_online(prompt_user, context_data=""):
    loading_bar(2, "MENGHUBUNGI OTAK AI")
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://google.com",
        "X-Title": "Rey Agent Student",
    }
    
    # INSTRUKSI: Memaksa AI berpikir fakta, bukan ngarang
    system_instruction = (
        "You are Rey Agent. Answer accurately in Indonesian. "
        "You are an expert encyclopedia. If asked about fruit/food, explain its taste and texture. "
        "If asked about universities, provide factual faculties. Do not hallucinate."
    )
    
    if context_data:
        system_instruction += f"\n\n[DATA FAKTA]:\n{context_data}\n\nGunakan data di atas jika relevan."

    # DAFTAR PRIORITAS MODEL (Dari yang Paling Pintar ke Cadangan)
    models_to_try = [
        "google/gemini-2.0-flash-lite-preview-02-05:free", # Prioritas 1: Sangat Pintar (Google)
        "meta-llama/llama-3-8b-instruct:free",             # Prioritas 2: Stabil (Meta)
        "mistralai/mistral-7b-instruct:free"               # Prioritas 3: Cadangan (Mistral)
    ]

    for model in models_to_try:
        data = {
            "model": model, 
            "messages": [
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt_user}
            ]
        }
        
        try:
            # Timeout 30 detik agar cukup waktu mikir
            response = requests.post(OPENROUTER_BASE_URL, headers=headers, json=data, verify=False, timeout=30)
            
            if response.status_code == 200:
                hasil_json = response.json()
                if 'choices' in hasil_json and len(hasil_json['choices']) > 0:
                    isi = hasil_json['choices'][0]['message'].get('content', '')
                    
                    # Bersihkan sampah tag
                    clean_msg = isi.replace("<s>", "").replace("[OUT]", "").replace("[/OUT]", "").strip()
                    
                    if clean_msg:
                        return clean_msg # BERHASIL! (Keluar dari loop)
            
            # Jika gagal/kosong, loop akan lanjut ke model berikutnya secara otomatis
            
        except Exception:
            continue # Lanjut ke model berikutnya jika timeout/error

    return "Maaf, semua server AI sedang sibuk saat ini. Mohon coba 1 menit lagi."

# --- 3. FUNGSI VISUAL ---
def ketik_efek(text, delay=0.01, warna=Fore.GREEN):
    sys.stdout.write(warna)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def loading_bar(durasi=2, pesan="PROCESS"):
    print(Fore.YELLOW + f"[{pesan}] Memulai proses...")
    toolbar_width = 30
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) 
    for i in range(toolbar_width):
        time.sleep(durasi / toolbar_width)
        sys.stdout.write(Fore.CYAN + "█")
        sys.stdout.flush()
    sys.stdout.write(Style.RESET_ALL + "]\n")

def tampilkan_header():
    ascii_art = r"""
  _____  _______   __
 |  __ \|  ___\ \ / /
 | |__) | |__  \ V / 
 |  _  /|  __|  | |  
 | | \ \| |____ | |  
 |_|  \_\______||_|  
                      
   REY AGENT V.10 - ULTIMATE INTELLIGENCE
    """
    print(Fore.CYAN + Style.BRIGHT + ascii_art)
    print(Fore.WHITE + "==================================================")
    print(Fore.WHITE + "   SYSTEM ONLINE. MULTI-MODEL BRAIN ACTIVATED.")
    print(Fore.WHITE + "==================================================\n")

# --- 4. KNOWLEDGE BASE (DATA LOKAL) ---
def get_data_upi():
    return """
    FAKTA UPI PURWAKARTA:
    1. Nama: Universitas Pendidikan Indonesia (UPI) Kampus Purwakarta.
    2. Alamat: Jl. Veteran No.8, Nagri Kaler, Purwakarta.
    3. Prodi: 
       - S1 PGSD (Pendidikan Guru Sekolah Dasar)
       - S1 PGPAUD (Pendidikan Guru PAUD)
       - S1 Sistem Telekomunikasi
       - S1 PSTI (Pendidikan Sistem & Teknologi Informasi)
       - S1 Mekatronika & AI
    4. Fasilitas: Lab Robotika, Lab Komputer, Asrama, Perpustakaan.
    """

# --- TOOLS LAIN ---
def tool_generate_password():
    loading_bar(1, "ENCRYPTING")
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for i in range(12))

def tool_system_check():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    return f"STATUS KESEHATAN LAPTOP:\n- CPU Load : {cpu}%\n- RAM Usage: {ram}%"

def tool_cari_file(keyword_pencarian):
    loading_bar(3, "SEARCHING DRIVE C")
    folder_awal = "C:\\"
    kata_diabaikan = ["tolong", "carikan", "cari", "lokasi", "spesifik", "file", "di", "laptop", "saya", "kamu", "dong", "yang", "bernama", "judul"]
    
    raw_words = keyword_pencarian.split()
    keywords_bersih = []
    for kata in raw_words:
        kata_clean = kata.strip(".,?!\"'").lower()
        if kata_clean and kata_clean not in kata_diabaikan:
            keywords_bersih.append(kata_clean)
            
    if not keywords_bersih: return "Mohon masukkan nama file yang lebih spesifik."

    target_display = " + ".join(keywords_bersih)
    print(Fore.YELLOW + f"[SEARCH] Mencari kombinasi kata: [{target_display}]...")

    hasil_pencarian = []
    folder_dilarang = ['Windows', 'Program Files', 'Program Files (x86)', 'ProgramData', '$Recycle.Bin', 'AppData']
    
    for root, dirs, files in os.walk(folder_awal):
        skip = False
        for d in folder_dilarang:
            if d in root: skip = True; break
        if skip: continue
            
        try:
            for file in files:
                semua_kata_ada = True
                nama_file_lower = file.lower()
                for k in keywords_bersih:
                    if k not in nama_file_lower:
                        semua_kata_ada = False; break
                if semua_kata_ada:
                    hasil_pencarian.append(os.path.join(root, file))
                    if len(hasil_pencarian) >= 3: break
        except: continue
        if len(hasil_pencarian) >= 3: break
    
    if hasil_pencarian: return "FILE DITEMUKAN:\n" + "\n".join(hasil_pencarian)
    return f"File dengan kata '{target_display}' tidak ditemukan."

# --- 5. OTAK AI (SMART ROUTING) ---
def otak_ai(input_user):
    text = input_user.lower()
    
    kampus_lain = ["cibiru", "sumedang", "tasik", "serang", "bumi siliwangi", "bandung", "setiabudi"]
    is_other_campus = any(k in text for k in kampus_lain)
    
    # 1. Routing UPI PURWAKARTA (Spesifik)
    if ("purwakarta" in text) or ("upi" in text and not is_other_campus):
        return tanya_llm_online(input_user, context_data=get_data_upi())

    # 2. Routing Umum & Tools
    elif is_other_campus or "upi" not in text:
        if "password" in text:
            return f"Password Baru: {tool_generate_password()}"
        elif "cpu" in text or "ram" in text or "kesehatan" in text or ("cek" in text and "laptop" in text):
            return tool_system_check()
        elif "cari" in text and "file" in text:
            return tool_cari_file(text)
        
        # Tanya AI Umum (Tanpa Context UPI)
        return tanya_llm_online(input_user, context_data="") 

    return "Maaf, saya bingung."

# --- MAIN ---
def main():
    tampilkan_header()
    while True:
        try:
            user_input = input(Fore.MAGENTA + "USER >> " + Fore.WHITE)
            if not user_input: continue
            if "keluar" in user_input.lower(): break
            
            response = otak_ai(user_input)
            print(Fore.CYAN + "REY AGENT: " + Fore.WHITE + response + "\n")
            
        except KeyboardInterrupt: break

if __name__ == "__main__":
    main()