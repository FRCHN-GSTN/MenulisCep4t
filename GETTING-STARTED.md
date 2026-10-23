# Panduan Memulai: Zero to PDF (Laporan Generator)

Selamat datang! Dokumen ini dirancang khusus untuk membantu Anda--baik pemula yang belum pernah mengetik kode maupun pengguna berpengalaman--untuk menghasilkan laporan akademik PDF berstandar profesional dalam waktu singkat.

---

## Pilih Jalur yang Sesuai dengan Anda

| Jalur | Persyaratan | Cocok Untuk |
|---|---|---|
| **[1. Opsi AI Agent](#1-opsi-ai-agent-paling-cepat--otomatis)** | AI Agent (OpenCode, Claude Code, Antigravity) | Pemula yang ingin laporan dibuatkan otomatis dari project |
| **[2. Opsi Docker](#2-opsi-docker-tanpa-install-tools-lokal)** | Docker Desktop | Pengguna yang tidak mau install Pandoc/Typst di komputer |
| **[3. Opsi Manual (CLI)](#3-opsi-manual-cli-kompilasi-lokal)** | Pandoc + Typst + ImageMagick | Pengguna Linux/Mac yang sudah biasa dengan CLI |

---

## 1. Opsi AI Agent (Paling Cepat & Otomatis)

Jika Anda sudah memiliki folder project (misal: Web, Mobile App, Machine Learning, IoT, Game) dan ingin AI menulis isi laporan untuk Anda:

```bash
# 1. Clone repositori ini ke direktori project Anda
git clone https://github.com/muadzhdz/laporan-generator.git project-kamu
cd project-kamu/

# 2. Ganti logo.jpg dengan logo kampus/sekolah Anda
# (Nama file HARUS tetap logo.jpg)

# 3. Jalankan AI Agent pilihan Anda di terminal, lalu instruksikan:
"Baca prompt.md dan bantu saya membuat laporan untuk project ini"

# 4. AI akan membaca struktur project Anda dan bertanya secara interaktif.
# Cukup jawab pertanyaan AI satu per satu.

# 5. Setelah AI selesai, jalankan kompilasi PDF:
docker compose run --rm laporan-generator
# atau jika punya Pandoc/Typst lokal:
./build.sh
```

---

## 2. Opsi Docker (Tanpa Install Tools Lokal)

Tidak perlu menginstall Pandoc, Typst, atau ImageMagick di komputer Anda. Semua dependensi sudah terkemas dalam container Docker terisolasi.

### Langkah-langkah:
1. Pastikan **Docker Desktop** sudah terinstall dan berjalan di komputer Anda. ([Download Docker](https://www.docker.com/products/docker-desktop/))
2. Buka terminal di dalam folder project ini.
3. Edit isi laporan manual di folder `chapters/` dan data di `metadata.yml`.
4. Jalankan perintah kompilasi:
   ```bash
   docker compose run --rm laporan-generator
   ```
5. File `Laporan.pdf` siap di folder project Anda!

> **Tips:** Gunakan `make docker-watch` untuk auto-rebuild otomatis setiap kali Anda menyimpan perubahan file markdown.

---

## 3. Opsi Manual CLI (Kompilasi Lokal)

Jika Anda lebih menyukai kompilasi cepat di mesin lokal Linux/macOS:

### Prasyarat System Packages:
* **Ubuntu/Debian**:
  ```bash
  sudo apt install pandoc imagemagick xz-utils
  wget -q https://github.com/typst/typst/releases/download/v0.15.1/typst-x86_64-unknown-linux-musl.tar.xz -O /tmp/typst.tar.xz
  tar -xJf /tmp/typst.tar.xz -C /tmp
  sudo mv /tmp/typst-x86_64-unknown-linux-musl/typst /usr/local/bin/
  ```
* **Arch Linux**:
  ```bash
  sudo pacman -S pandoc typst imagemagick
  ```
* **Nix / NixOS**:
  ```bash
  nix develop
  ```
* **Windows (PowerShell / Winget)**:
  ```powershell
  winget install JohnMacFarlane.Pandoc
  winget install Typst.Typst
  winget install ImageMagick.ImageMagick
  ```

### Jalankan Build:

**Linux / macOS:**
```bash
# Inisialisasi git hooks (opsional)
make init

# Build PDF (atau ./laporan build)
make build

# Export Word (.docx)
make docx

# Buka PDF di viewer
make view
```

**Windows (PowerShell):**
```powershell
# Cek dependensi & berkas
.\laporan.ps1 check

# Build PDF
.\laporan.ps1 build

# Buka PDF di viewer
.\laporan.ps1 view
```

---

## Glosarium Istilah Teknis

* **Pandoc**: Program pengubah format dokumen (mengonversi Markdown menjadi Typst/PDF/Word/HTML).
* **Typst**: Engine typesetting dokumen modern, cepat, dan ringan berbasis bahasa penataan letak yang intuitif.
* **BibTeX**: Format standar untuk menyimpan data referensi/daftar pustaka akademik (`references.bib`).
* **CSL (Citation Style Language)**: Berkas aturan penulisan sitasi (pada project ini menggunakan standar APA Style `apa.csl`).
* **PAGEREF DOCX**: Mekanisme penomoran halaman otomatis pada Daftar Isi dokumen Microsoft Word.

---

## FAQ & Troubleshooting Singkat

* **Q: Mengapa penomoran bab saya menjadi ganda seperti "BAB I: BAB 1"?**  
  *A:* Di file Markdown `chapters/bab*.md`, gunakan heading `# Judul Bab` tanpa menyertakan kata "BAB 1". Template Typst akan menambahkan kata "BAB I" secara otomatis.

* **Q: Bagaimana cara menambahkan gambar/screenshot?**  
  *A:* Simpan file gambar di folder `gambar/` lalu panggil di Markdown menggunakan sintaks `![](gambar/nama-file.png)`.

* **Q: Bagaimana format sitasi yang benar?**  
  *A:* Masukkan entri BibTeX di `references.bib`, lalu panggil di Markdown menggunakan sintaks `[@citekey]`.

* **Q: Bagaimana cara menyesuaikan format dengan kampus saya?**  
  *A:* Gunakan `./laporan preset list` untuk memilih preset kampus bawaan (UI, ITB, UGM, ITS, UNPAD), atau pindai buku pedoman PDF kampus Anda dengan `./laporan preset scan /path/ke/pedoman.pdf`.

---

Untuk panduan lebih mendalam mengenai skema metadata, preset kampus, dan arsitektur template, silakan baca dokumentasi di folder `docs/`:
- [docs/campus-guide.md](docs/campus-guide.md)
- [docs/preset-schema.md](docs/preset-schema.md)
- [docs/metadata-schema.md](docs/metadata-schema.md)
- [docs/template-guide.md](docs/template-guide.md)
- [docs/troubleshooting.md](docs/troubleshooting.md)
