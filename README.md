# 🧠 REY AGENT V.10 - Ultimate Intelligent Terminal System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Multi--Model-purple?style=for-the-badge)

**Rey Agent** adalah asisten virtual berbasis *Command Line Interface* (CLI) yang dirancang dengan arsitektur **Hybrid AI**. Program ini menggabungkan kemampuan eksekusi teknis komputer (Local Tools) dengan kecerdasan buatan berbasis Cloud (LLM) yang tangguh dan sadar konteks.

---

## 🚀 Fitur Unggulan (Key Features)

### 1. 🧠 Context-Aware Intelligence (Smart Routing)
Agent ini tidak sekadar menjawab asal-asalan. Ia memiliki logika **Smart Routing** untuk membedakan konteks pertanyaan:
* **Local Knowledge:** Jika ditanya tentang "UPI Purwakarta", Agent menggunakan database internal yang akurat (Anti-Halusinasi).
* **General Knowledge:** Jika ditanya tentang kampus lain (misal: UNDIP) atau pengetahuan umum, Agent beralih ke *Global Knowledge* tanpa mencampuradukkan data.

### 2. 🛡️ Robust Multi-Model Failover (Anti-Macet)
Sistem ini dirancang untuk **tahan banting** terhadap gangguan server atau limit API. Agent akan mencoba model AI secara berurutan:
1.  **Google Gemini 2.0 Flash** (Prioritas 1: Paling Cerdas).
2.  **Meta Llama 3** (Prioritas 2: Sangat Stabil).
3.  **Mistral 7B** (Prioritas 3: Cadangan).
*Jika satu model gagal, Agent otomatis pindah ke model berikutnya tanpa crash.*

### 3. 🔍 Deep Search Engine
Pencarian file rekursif di seluruh **Drive C:** yang dioptimalkan dengan *Smart Filtering* (melewati folder sistem berat) dan *Flexible Keyword Matching* (mencocokkan kombinasi kata yang terpisah).

### 4. 💻 Hardware & Utility Tools
* **System Monitor:** Cek kesehatan CPU & RAM Real-time.
* **Security:** Generator Password acak yang kuat.
* **Digital Note:** Mencatat log ke file `.txt`.

---

## 📦 Instalasi & Cara Menjalankan

Pastikan Anda telah menginstall **Python 3.10** atau lebih baru.

1.  **Clone Repository**
    ```bash
    git clone [https://github.com/UsernameAnda/Rey-AI-Agent-V10.git](https://github.com/UsernameAnda/Rey-AI-Agent-V10.git)
    cd Rey-AI-Agent-V10
    ```

2.  **Install Dependencies**
    Install library yang dibutuhkan menggunakan `pip`:
    ```bash
    pip install -r requirements.txt
    ```
    *(Library utama: `requests`, `psutil`, `colorama`, `urllib3`)*

3.  **Jalankan Program**
    ```bash
    python agent_tugas.py
    ```

---

## 🤖 Contoh Perintah (Commands)

Anda dapat berinteraksi menggunakan bahasa manusia (*Natural Language*). Berikut contoh perintah yang dapat ditangani:

| Kategori | Contoh Input User |
| :--- | :--- |
| **Wawasan Umum** | *"Apa rasanya buah nangka?"* |
| | *"Jelaskan teori relativitas singkat"* |
| **Info Kampus (Context)** | *"Ada prodi apa saja di UPI Purwakarta?"* (Data Lokal) |
| | *"Ada fakultas apa di Universitas Diponegoro?"* (Data Global) |
| **Manajemen File** | *"Tolong carikan file skripsi bab 1"* |
| | *"Cari lokasi file foto liburan"* |
| **Monitoring Sistem** | *"Cek kesehatan laptop dong"* |
| **Keamanan** | *"Buatkan password untuk instagram"* |

---

## 🛠️ Struktur Project

* `agent_tugas.py`: Kode utama (Main Logic, Routing, Tools, UI).
* `requirements.txt`: Daftar library python yang dibutuhkan.
* `rahasia_agent.txt`: Output file untuk fitur pencatatan.
* `README.md`: Dokumentasi proyek.

---

## 👨‍💻 Author & Credits

Project ini dibuat untuk memenuhi Tugas Mata Kuliah **Kecerdasan Buatan (AI)**.

* **Developer:** [Nama Kamu]
* **NIM:** [NIM Kamu]
* **Tech Stack:** Python, OpenRouter API (Gemini/Llama/Mistral).

---
*Disclaimer: Program ini menggunakan API Key OpenRouter yang dikonfigurasi untuk keperluan akademik.*
