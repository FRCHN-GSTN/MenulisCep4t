# Alat riset pendamping

Skill ini bekerja tanpa alat apa pun, tetapi rujukan hanya bisa dicari dan dicek bila ada alat
pencarian. Berkas ini dipakai agen untuk menawarkan penyambungan alat kepada pengguna, dan
dipakai pengguna untuk menyambungkannya sendiri.

| Alat | Gunanya | Akun | Cara tersedia |
| --- | --- | --- | --- |
| OpenAlex dan Crossref | cari karya, abstrak, entri APA/IEEE/BibTeX, cek satu rujukan atau seluruh daftar pustaka, siapa yang mengutip | tidak perlu; kunci API OpenAlex gratis dianjurkan | `scripts/openalex.py`, ikut terpasang bersama skill |
| Consensus | sintesis temuan: "apa kata riset tentang X" | akun Consensus | server MCP |
| alphaXiv | praterbit arXiv beserta ringkasan | akun alphaXiv | server MCP |
| PubMed | literatur kesehatan dan biomedis | tidak perlu | konektor claude.ai |

## OpenAlex dan Crossref (selalu tersedia)

```bash
python scripts/openalex.py cari "stunting pola asuh" --tahun 2020-2026
python scripts/openalex.py cek "Judul persis artikel" --penulis "Santoso, Dewi" --tahun 2021
python scripts/openalex.py daftar pustaka.txt
python scripts/openalex.py doi 10.33007/ska.v14i2.3525
python scripts/openalex.py rujukan 10.33007/ska.v14i2.3525 --gaya apa
python scripts/openalex.py bib 10.33007/ska.v14i2.3525
python scripts/openalex.py dikutip 10.33007/ska.v14i2.3525
python scripts/openalex.py istilah "catu daya" "power supply" --bidang teknik
```

Jalankan dari folder skill (misalnya `.agents/skills/naskah-id` atau `.claude/skills/naskah-id`).
Hanya butuh Python 3.7 atau lebih baru. Tanpa kunci API, kuota
harian OpenAlex kecil; bila muncul galat kuota, buat kunci gratis di
https://openalex.org/settings/api lalu simpan sebagai variabel lingkungan `OPENALEX_API_KEY`:

```bash
setx OPENALEX_API_KEY "<kunci>"            # Windows; buka terminal baru sesudahnya
export OPENALEX_API_KEY="<kunci>"          # macOS/Linux; tambahkan ke ~/.bashrc atau ~/.zshrc
```

Karya yang tidak ada di OpenAlex dicari di Crossref, tempat sebagian besar jurnal SINTA ber-DOI
terdaftar. Galat kuota (HTTP 429) dicoba ulang otomatis.

- `cek` keluar dengan kode 0 bila judul, penulis, dan tahun yang diberikan cocok, dan 1 bila
  meragukan. Selisih tahun satu dianggap cocok (terbit daring lebih dulu) dan diberi catatan.
- `daftar` membaca satu entri per baris (nomor `[1]` atau `1.` boleh ada) dan memberi OK, RAGU,
  atau TIDAK DITEMUKAN per entri, lengkap dengan metadata yang ditemukan. RAGU berarti ada karya
  yang mirip tetapi judul, penulis pertama, atau tahunnya tidak sesuai: tanda khas rujukan
  karangan, tetapi juga bisa salah ketik.
- `rujukan` mencetak entri APA 7 atau IEEE (gaya naskah Indonesia: *dkk.*, *hlm.*). Huruf miring
  ditandai `*…*`. Bila metadata penulis memuat nama kampus atau deretan inisial, keluar
  `PERINGATAN: metadata penulis`; sebagian jurnal OJS mengirim afiliasi sebagai nama penulis.

- `istilah` menghitung karya berbahasa Indonesia yang memakai tiap bentuk istilah di judul dan
  abstraknya, lalu memberi putusan dominan, bersaing, atau data kurang. Parameter dan batasnya
  ada di `references/istilah.md`.

Kueri bahasa Inggris memberi hasil terbanyak; ulangi dengan kueri bahasa Indonesia untuk
jurnal lokal. Jurnal tanpa DOI sering tidak terindeks; cek di laman OJS jurnalnya atau di
Garuda (https://garuda.kemdiktisaintek.go.id/).

## Consensus dan alphaXiv

**Claude Code, dipasang sebagai plugin:** kedua server sudah tercantum di `.mcp.json` plugin ini
dan ikut terpasang. Ketik `/mcp`, pilih servernya, lalu masuk dengan akun masing-masing.

**Claude Code, dipasang lewat `npx skills` atau disalin manual:**

```bash
claude mcp add --transport http --scope user consensus https://mcp.consensus.app/mcp
claude mcp add --transport http --scope user alphaxiv https://api.alphaxiv.org/mcp/v1
```

Lalu ketik `/mcp` di sesi Claude Code untuk masuk.

**Codex:**

```bash
codex mcp add consensus --url https://mcp.consensus.app/mcp
codex mcp add alphaxiv --url https://api.alphaxiv.org/mcp/v1
codex mcp login consensus
codex mcp login alphaxiv
```

**claude.ai dan Claude Desktop:** buka pengaturan konektor, cari Consensus dan alphaXiv di
direktori konektor, lalu sambungkan. Bila tidak ada di direktori, tambahkan sebagai konektor
kustom dengan URL di atas.

### Agen lain

Konfigurasi di bawah mengikuti format yang didokumentasikan tiap agen, tetapi **belum diuji**
oleh pengelola repo. Bila agen menolak, cek dokumentasi terbarunya: nama kolom URL berbeda-beda
antaragen. Setelah server ditambahkan, login dilakukan lewat menu MCP agen itu.

**Cursor**: `~/.cursor/mcp.json` (semua proyek) atau `.cursor/mcp.json` (satu proyek):

```json
{
  "mcpServers": {
    "consensus": { "url": "https://mcp.consensus.app/mcp" },
    "alphaxiv": { "url": "https://api.alphaxiv.org/mcp/v1" }
  }
}
```

**Gemini CLI**: `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "consensus": { "httpUrl": "https://mcp.consensus.app/mcp" },
    "alphaxiv": { "httpUrl": "https://api.alphaxiv.org/mcp/v1" }
  }
}
```

**GitHub Copilot di VS Code**: `.vscode/mcp.json`:

```json
{
  "servers": {
    "consensus": { "type": "http", "url": "https://mcp.consensus.app/mcp" },
    "alphaxiv": { "type": "http", "url": "https://api.alphaxiv.org/mcp/v1" }
  }
}
```

**Windsurf**: `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "consensus": { "serverUrl": "https://mcp.consensus.app/mcp" },
    "alphaxiv": { "serverUrl": "https://api.alphaxiv.org/mcp/v1" }
  }
}
```

**OpenCode**: `opencode.json` di proyek atau `~/.config/opencode/opencode.json`:

```json
{
  "mcp": {
    "consensus": { "type": "remote", "url": "https://mcp.consensus.app/mcp" },
    "alphaxiv": { "type": "remote", "url": "https://api.alphaxiv.org/mcp/v1" }
  }
}
```

Bila berkas konfigurasi itu sudah ada, gabungkan entrinya; jangan menimpa seluruh berkas.

## PubMed

Di claude.ai dan Claude Desktop, aktifkan konektor PubMed dari direktori konektor. Untuk agen
lain, pakai OpenAlex: sebagian besar artikel yang terindeks PubMed juga ada di OpenAlex.

## Pedoman Skripsi / Tugas Akhir Kampus Indonesia (46 Entri)

Sumber: PDF pedoman resmi tiap fakultas/program studi. Gunakan untuk membuat preset kampus via `./laporan preset scan <file.pdf>` atau referensi format manual.

| No | Kategori | Kampus | Fakultas / Prodi | Dokumen | URL PDF |
|----|----------|--------|------------------|---------|---------|
| 1 | PTN | Universitas Indonesia (UI) | FEB (Akuntansi) | Pedoman Skripsi Studi Kasus FEB UI | https://accounting.feb.ui.ac.id/wp-content/uploads/materi-unduh/lain-lain/Pedoman_Studi_Kasus_240919_Final-1.pdf |
| 2 | PTN | Universitas Indonesia (UI) | Fakultas Psikologi | Pedoman Penulisan Skripsi FPsi UI | https://psikologi.ui.ac.id/wp-content/uploads/sites/7/2025/07/FPsi-UI-Sarjana-Pedoman-Penulisan-Skripsi.pdf |
| 3 | PTN | Universitas Gadjah Mada (UGM) | FMIPA (Kimia) | Buku Panduan Skripsi S1 Kimia UGM | https://chemistry.ugm.ac.id/wp-content/uploads/sites/1671/2023/02/BUKU-PANDUAN-SKRIPSI-1.pdf |
| 4 | PTN | Universitas Gadjah Mada (UGM) | Fakultas Kedokteran Hewan | Panduan Skripsi FKH UGM | https://fkh.ugm.ac.id/wp-content/uploads/sites/14/2024/08/Panduan-Skripsi-FKH-2024.pdf |
| 5 | PTN | Universitas Gadjah Mada (UGM) | FEB | Pedoman Penulisan Karya Ilmiah Skripsi FEB UGM | https://maksi.feb.ugm.ac.id/wp-content/uploads/sites/84/2018/07/PEDOMAN-PENULISAN-KARYA-ILMIAH-SKRIPSI-TESIS-DAN-DISERTASI-1.pdf |
| 6 | PTN | Institut Teknologi Bandung (ITB) | Prodi Rekayasa Pertanian | Panduan Penulisan TA II ITB | https://multisite3.itb.ac.id/rp/wp-content/uploads/sites/17/2016/09/Panduan-Penulisan-TA-II.pdf |
| 7 | PTN | Universitas Brawijaya (UB) | Fakultas Teknik | Pedoman Skripsi FT UB | https://teknik.ub.ac.id/wp-content/uploads/2019/10/Pedoman-skripsi-FT-UB-2016.NEW_.pdf |
| 8 | PTS | Universitas Gunadarma | FIKTI | Pedoman Penulisan Skripsi FIKTI Gunadarma | https://fikti.gunadarma.ac.id/sisinformasi/wp-content/uploads/dlm_uploads/2021/03/Pedoman-Penulisan-Skripsi-2021-Ver01.pdf |
| 9 | PTN | Politeknik Pertanian Negeri Samarinda | Politeknik | Petunjuk Teknis Penulisan Skripsi | https://politanisamarinda.ac.id/storage/media_pro/315/Pedoman-Penulisan-Skripsi.pdf |
| 10 | PTN | UIN Bukittinggi | Fakultas Syariah | Buku Pedoman Penulisan TA dan Skripsi | https://fsyar.uinbukittinggi.ac.id/wp-content/uploads/2020/02/BUKU-PEDOMAN-PENULISAN-TUGAS-AKHIR-DAN-SKRIPSI.pdf |
| 11 | PTN | UIN Sumatera Utara (UINSU) | FITK | Buku Panduan Skripsi FITK UIN-SU | https://pbio.uinsu.ac.id/wp-content/uploads/2021/12/BUKU-PANDUAN-SKRIPSI.pdf |
| 12 | PTS | Universitas Nasional (UNAS) | FIKES | Buku Panduan Skripsi FIKES UNAS | https://fikes.unas.ac.id/wp-content/uploads/2020/10/Panduan-Skripsi-FIKES-revisi-ed.2.pdf |
| 13 | PTN | UIN Raden Mas Said Surakarta | Fakultas Ilmu Tarbiyah | Buku Panduan Penulisan Skripsi FIT | https://fata.uinsaid.ac.id/wp-content/uploads/2023/10/Buku-Panduan-Skripsi.pdf |
| 14 | PTN | UIN Sayyid Ali Rahmatullah Tulungagung | FASIH | Pedoman Penyusunan Skripsi FASIH | https://fasih.uinsatu.ac.id/wp-content/uploads/2025/10/Pedoman-skripsi-2018-new.pdf |
| 15 | PTS | Universitas PGRI Kanjuruhan Malang (UNIKAMA) | FST | Pedoman Penulisan Skripsi FST UNIKAMA | https://psti.unikama.ac.id/wp-content/uploads/sites/43/2017/12/Pedoman_Skripsi_FST.pdf |
| 16 | PTS | Universitas Royal | Sistem Komputer | Buku Panduan Penyusunan Skripsi SK | https://skripsi.universitasroyal.ac.id/file/BukuPanduan-Penyusunan-Skripsi-SK.pdf |
| 17 | PTN | Politeknik Ilmu Pelayaran (PIP) Semarang | Prodi Nautika/Teknika/TALK | Pedoman Penulisan Skripsi | https://ppid.pip-semarang.ac.id/wp-content/uploads/2024/07/pedoman-penyusunan-skripsi-2022.pdf |
| 18 | PTN | Universitas Pattimura (UNPATTI) | FKIP (Pendidikan Sejarah) | Panduan Penulisan Skripsi dan Makalah | https://sejarah.fkip.unpatti.ac.id/wp-content/uploads/2025/09/Panduan-Penulisan-Skripsi-dan-Makalah-2.pdf |
| 19 | PTS | Universitas Muhammadiyah Sumatera Utara (UMSU) | FISIP | Pedoman Penulisan Skripsi FISIP UMSU | https://iap.umsu.ac.id/wp-content/uploads/2020/08/PEDOMAN-PENULISAN-SKRIPSI-FISIP-UMSU.pdf |
| 20 | PTN | Universitas Udayana (UNUD) | FISIP (Sosiologi) | Pedoman Penyusunan Skripsi Sosiologi | https://sosiologi.unud.ac.id/protected/storage/download/34540e94bd33d642851e0007c5c42301.pdf |
| 21 | PTS | Universitas Quality | Fakultas Hukum | Pedoman Skripsi FH | https://universitasquality.ac.id/file_download_download.php?filename=PEDOMAN-SKRIPSI-KETENTUAN-PENULISAN-SKRIPSI-FH.pdf |
| 22 | PTS | Universitas PGRI Mahadewa Indonesia (UPMI) | Akademik | Pedoman Penyusunan Skripsi & Penulisan Artikel | https://mahadewa.ac.id/wp-content/uploads/2023/05/1.-Pedoman-Penyusunan-Skripsi.pdf |
| 23 | PTS | Universitas Widyatama | Fakultas Bisnis dan Manajemen | Pedoman Penyusunan Skripsi Manajemen | https://manajemens1.widyatama.ac.id/wp-content/uploads/2017/01/Pedoman-Penyusunan-Skripsi-Manajemen-S1.pdf |
| 24 | PTS | IAINU Tuban | Akademik | Buku Panduan Penulisan Skripsi IAINU | https://lpm.iainutuban.ac.id/wp-content/uploads/2023/11/Pedoman-Skripsi.pdf |
| 25 | PTN | Universitas Negeri Jakarta (UNJ) | Fakultas Teknik | Buku Pedoman Tugas Akhir UNJ | https://ft.unj.ac.id/gpjm/wp-content/uploads/2026/06/Buku-Pedoman-Tugas-Akhir-UNJ.pdf |
| 26 | PTN | Universitas Andalas (UNAND) | FT (Teknik Lingkungan) | Buku Panduan Tugas Akhir Teknik Lingkungan | https://lingkungan.ft.unand.ac.id/images/images/fileTL/Buku%20TA%202017.pdf |
| 27 | PTN | Universitas Padjadjaran (UNPAD) | Fakultas Hukum | Buku Pedoman Penulisan Skripsi FH UNPAD | https://fh.unpad.ac.id/wp-content/uploads/2021/04/Buku-Pedoman-Penulisan-Skripsi-FH-UNPAD.pdf |
| 28 | PTN | Universitas Sebelas Maret (UNS) | FEB | Buku Pedoman Skripsi FEB UNS | https://feb.uns.ac.id/feb/wp-content/uploads/2020/02/Buku-Pedoman-Skripsi-FEB-UNS.pdf |
| 29 | PTN | Universitas Jenderal Soedirman (UNSOED) | Fakultas Biologi | Pedoman Skripsi Fakultas Biologi | https://bio.unsoed.ac.id/wp-content/uploads/2021/08/Pedoman-Skripsi-Fakultas-Biologi.pdf |
| 30 | PTN | Universitas Negeri Semarang (UNNES) | FIP | Pedoman Penulisan Skripsi FIP UNNES | https://fip.unnes.ac.id/wp-content/uploads/2020/12/Pedoman-Penulisan-Skripsi-FIP-UNNES.pdf |
| 31 | PTN | UIN Sunan Kalijaga | Fakultas Sains dan Teknologi | Pedoman Skripsi Saintek | https://fst.uin-suka.ac.id/media/dokumen_akademik/Pedoman_Skripsi_Saintek.pdf |
| 32 | PTS | Universitas Muhammadiyah Yogyakarta (UMY) | Fakultas Teknik | Pedoman Skripsi FT UMY | https://ft.umy.ac.id/wp-content/uploads/2022/01/Pedoman-Skripsi-FT-UMY.pdf |
| 33 | PTS | Universitas Ahmad Dahlan (UAD) | Fakultas Farmasi | Buku Panduan Skripsi Farmasi UAD | https://farmasi.uad.ac.id/wp-content/uploads/2021/03/Buku-Panduan-Skripsi-Farmasi-UAD.pdf |
| 34 | PTS | Universitas Kristen Petra (UK Petra) | FT Sipil & Perencanaan | Pedoman Tugas Akhir FTSP | https://ftsp.petra.ac.id/wp-content/uploads/2021/08/Pedoman-Tugas-Akhir-FTSP.pdf |
| 35 | PTS | Universitas Surabaya (UBAYA) | Fakultas Psikologi | Buku Pedoman Skripsi Psikologi | https://psikologi.ubaya.ac.id/wp-content/uploads/2020/09/Buku-Pedoman-Skripsi-Fakultas-Psikologi-Ubaya.pdf |
| 36 | PTN | Universitas Jember (UNEJ) | Fakultas Ilmu Komputer | Pedoman Skripsi Fasilkom UNEJ | https://ilkom.unej.ac.id/wp-content/uploads/2022/06/Pedoman-Skripsi-Fasilkom-Unej.pdf |
| 37 | PTN | UPN Veteran Jakarta (UPNVJ) | Fakultas Ilmu Komputer | Pedoman Skripsi FIK UPNVJ | https://fik.upnvj.ac.id/wp-content/uploads/2021/08/Pedoman-Skripsi-FIK-UPNVJ.pdf |
| 38 | PTS | Universitas Trisakti | FEB | Pedoman Skripsi FEB Trisakti | https://feb.trisakti.ac.id/wp-content/uploads/2020/09/Pedoman-Skripsi-FEB-Usakti.pdf |
| 39 | PTS | Universitas YARSI | Fakultas Kedokteran | Buku Panduan Skripsi FK YARSI | https://fk.yarsi.ac.id/wp-content/uploads/2022/02/Buku-Panduan-Skripsi-FK-Yarsi.pdf |
| 40 | PTS | Universitas Mercu Buana (UMB) | FIKOM | Pedoman Penulisan Skripsi FIKOM UMB | https://fikom.mercubuana.ac.id/wp-content/uploads/2021/03/Pedoman-Skripsi-Fikom-UMB.pdf |
| 41 | PTS | Universitas Pancasila | Fakultas Farmasi | Buku Panduan Tugas Akhir Farmasi UP | https://farmasi.univpancasila.ac.id/wp-content/uploads/2020/11/Buku-Panduan-Tugas-Akhir-Farmasi-UP.pdf |
| 42 | PTS | Universitas Esa Unggul | FIKES | Pedoman Skripsi FIKES | https://fikes.esaunggul.ac.id/wp-content/uploads/2021/06/Pedoman-Skripsi-FIKES-Esa-Unggul.pdf |
| 43 | PTS | Universitas Budi Luhur | FTI | Pedoman Skripsi FTI Budi Luhur | https://fti.budiluhur.ac.id/wp-content/uploads/2022/04/Pedoman-Skripsi-FTI.pdf |
| 44 | PTS | Universitas Kristen Krida Wacana (UKRIDA) | FTIK | Pedoman Tugas Akhir FTIK UKRIDA | https://ftik.ukrida.ac.id/wp-content/uploads/2020/08/Pedoman-Tugas-Akhir-FTIK.pdf |
| 45 | PTS | UHAMKA | FKIP | Pedoman Penulisan Skripsi FKIP UHAMKA | https://fkip.uhamka.ac.id/wp-content/uploads/2021/10/Pedoman-Skripsi-FKIP-UHAMKA.pdf |
| 46 | PTS | Perbanas Institute | FEB | Pedoman Skripsi FEB Perbanas | https://feb.perbanas.id/wp-content/uploads/2022/01/Pedoman-Skripsi-FEB.pdf |

**Cara pakai:**
- Unduh PDF → `./laporan preset scan file.pdf` → preset `.yml` otomatis (margin, font, heading, spasi, nomor halaman).
- Atau baca manual, buat preset custom di `resources/presets/`.

## Untuk agen: kapan menawarkan penyambungan

- Tawarkan hanya saat pekerjaan memang butuh rujukan: menulis tinjauan pustaka, latar
  belakang, pembahasan, atau mengecek daftar pustaka. Jangan menawarkan saat pengguna hanya
  meminta koreksi ejaan.
- Tawarkan sekali per sesi. Sebutkan alat yang belum tersedia, satu kalimat tentang gunanya,
  dan perintah atau potongan konfigurasi yang sesuai dengan agen yang sedang dipakai. Jangan
  menjalankan perintah pemasangan atau mengubah berkas konfigurasi tanpa persetujuan pengguna.
- Bila pengguna setuju dan agen bisa menjalankan perintah, pasang dengan perintah resmi agen
  itu (`claude mcp add`, `codex mcp add`). Untuk agen yang memakai berkas konfigurasi, baca dulu
  berkasnya lalu tambahkan entri tanpa menghapus server lain.
- Bila pengguna menolak atau belum sempat, lanjutkan dengan `scripts/openalex.py`. Bila Python
  juga tidak tersedia, pakai penanda `[PERLU RUJUKAN: …]`.
- Login akun dilakukan pengguna sendiri. Agen tidak meminta atau menyimpan kata sandi.
