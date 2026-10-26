# Metode Penelitian

## Pendekatan dan Desain Penelitian

Penelitian ini menggunakan pendekatan kuantitatif dengan metode survei eksplanatif (*explanatory survey*). Pendekatan kuantitatif dipilih karena penelitian bertujuan menguji hipotesis teoritis mengenai hubungan kausal dan korelasional antarvariabel yang telah dioperasionalkan secara terukur [@griffiths2005components; @yu2024development]. Desain penelitian bersifat *cross-sectional*, yaitu pengumpulan data dilakukan pada satu titik waktu tertentu (*one point in time*) dari populasi sasaran guna mengukur persepsi, perilaku penggunaan, tingkat kecanduan, dan tingkat produktivitas mahasiswa secara simultan.

Alur tahapan pelaksanaan penelitian disusun secara sistematis meliputi:

1. **Tahap Konseptualisasi**: Perumusan masalah penelitian, kajian literatur empiris, penyusunan kerangka berpikir, dan formulasi hipotesis.
2. **Tahap Pengembangan Instrumen**: Penyusunan kuesioner berdasarkan indikator operasional variabel yang telah divalidasi oleh literatur sebelumnya.
3. **Tahap Uji Coba Instrumen (*Pilot Testing*)**: Penyebaran awal kuesioner kepada 30 responden untuk menguji validitas konstruk dan reliabilitas instrumen.
4. **Tahap Pengumpulan Data Lapangan**: Penyebaran kuesioner final secara daring kepada sampel mahasiswa yang memenuhi kriteria inklusi.
5. **Tahap Analisis dan Pengujian Statistik**: Pengujian asumsi klasik, analisis deskriptif statistik, analisis regresi linier berganda, dan pengujian analisis jalur (*path analysis*).
6. **Tahap Interpretasi dan Pelaporan**: Pembahasan temuan empiris, komparasi dengan penelitian terdahulu, perumusan kesimpulan, serta saran perbaikan kebijakan akademik.

## Operasionalisasi Variabel Penelitian

Operasionalisasi variabel memetakan konsep teoritis ke dalam indikator terukur menggunakan skala Likert lima tingkat, dari skor 1 (Sangat Tidak Setuju) hingga 5 (Sangat Setuju). Variabel penelitian terbagi atas tiga kategori:

| Klasifikasi Variabel | Nama Variabel | Dimensi Indikator | Skala Ukur |
| --- | --- | --- | --- |
| Variabel Bebas ($X_1$) | Faktor Teknologis | 1. Persepsi Kemudahan (*Perceived Ease of Use*); 2. Persepsi Kecepatan Umpan Balik (*Response Latency*); 3. Interaktivitas Alami Bahasa (*Conversational Naturalness*); 4. Kelengkapan Solusi Koding dan Teks (*Solution Completeness*). | Ordinal (Likert 1-5) |
| Variabel Bebas ($X_2$) | Faktor Psikologis | 1. Kecemasan Akademik (*Academic Anxiety*); 2. Kecemasan Tertinggal Teknologi (*AI FoMO*); 3. Efikasi Diri Penggunaan AI (*AI Self-Efficacy*); 4. Ketiadaan Regulasi Belajar Mandiri (*Self-Regulation Deficit*). | Ordinal (Likert 1-5) |
| Variabel Bebas ($X_3$) | Faktor Lingkungan Sosial | 1. Pengaruh Teman Sebaya (*Peer Influence*); 2. Norma Subyektif Lingkungan Kampus; 3. Tingginya Tuntutan Beban Tugas Kuliah; 4. Ketiadaan Pengawasan Ketat Deteksi AI. | Ordinal (Likert 1-5) |
| Variabel Antara ($Y$) | Kecanduan *AI Assistant* (*Problematic AI Usage*) | 1. Kemenonjolan Kognitif (*Salience*); 2. Modifikasi Emosi (*Mood Modification*); 3. Eskalasi Durasi (*Tolerance*); 4. Distres saat Akses Terputus (*Withdrawal Symptoms*); 5. Konflik Diri dan Akademik (*Interpersonal/Academic Conflict*); 6. Kegagalan Membatasi Diri (*Relapse/Loss of Control*). | Ordinal (Likert 1-5) |
| Variabel Terikat ($Z$) | Produktivitas Mahasiswa | 1. Efisiensi Pengelolaan Waktu Belajar; 2. Kedalaman Penguasaan Materi/Konsep; 3. Orisinalitas dan Kualitas Luaran Tugas; 4. Kemandirian dan Retensi Kognitif Pemrograman. | Ordinal (Likert 1-5) |

Instrumen pengukuran kecanduan ($Y$) diadaptasi dari skala baku *Problematic ChatGPT Use Scale* (PCUS) yang divalidasi oleh Yu, Chen, & Yang [@yu2024development] dan Maral dkk. [@maral2025problematic], disesuaikan dengan konteks umum asisten AI di lingkungan universitas.

## Populasi dan Sampel

### Karakteristik Populasi Sasaran

Populasi dalam penelitian ini adalah seluruh mahasiswa aktif Program Studi Sistem Informasi jenjang Strata Satu (S-1) Fakultas Ilmu Komputer dan Teknologi Informasi (FIKTI) Universitas Gunadarma angkatan [PERLU DATA: isi tahun angkatan, mis. 2021 s.d. 2024], dengan estimasi total populasi aktif sebesar $N = \text{[PERLU DATA: isi jumlah total mahasiswa aktif SI Gunadarma, mis. 1200]}$ mahasiswa.

Kriteria inklusi responden:

1. Terdaftar sebagai mahasiswa aktif Program Studi Sistem Informasi Universitas Gunadarma pada tahun akademik berjalan.
2. Telah menggunakan sekurang-kurangnya satu layanan *AI assistant* (seperti ChatGPT, Claude, Copilot, atau Gemini) untuk keperluan penunjang tugas akademik dalam tiga bulan terakhir.
3. Bersedia mengisi kuesioner penelitian secara sukarela melalui lembar persetujuan (*informed consent*).

### Penentuan Ukuran Sampel

Penentuan ukuran sampel minimum dihitung menggunakan rumus Slovin dengan tingkat presisi atau toleransi kesalahan (*margin of error*) sebesar $e = 5\%$ ($0{,}05$):

$$n = \frac{N}{1 + N(e)^2}$$

Sebagai contoh estimasi operasional bila populasi aktif tercatat sebanyak 1.000 mahasiswa:

$$n = \frac{1000}{1 + 1000(0{,}05)^2} = \frac{1000}{1 + 2{,}5} = \frac{1000}{3{,}5} \approx 286 \text{ responden}$$

[PERLU DATA: masukkan angka pasti jumlah populasi aktual dan hasil hitung sampel akhir sesuai data prodi].

### Teknik Pengambilan Sampel

Teknik pengambilan sampel yang digunakan adalah *purposive sampling* yang dikombinasikan dengan *proportional stratified random sampling*. *Purposive sampling* diterapkan untuk memastikan responden memenuhi kriteria inklusi keaktifan penggunaan *AI assistant*. Stratifikasi dilakukan berdasarkan angkatan perkuliahan guna merepresentasikan keberagaman beban tugas kurikulum dari tingkat awal hingga penyusunan tugas akhir/skripsi.

## Teknik Pengumpulan Data

Data penelitian dikumpulkan melalui dua sumber data utama:

1. **Data Primer**: Diperoleh secara langsung melalui penyebaran kuesioner elektronik terstruktur (*Google Forms*) yang dibagikan melalui grup komunikasi resmi mahasiswa Sistem Informasi Gunadarma. Kuesioner terdiri dari bagian profil demografis (jenis kelamin, angkatan, frekuensi penggunaan, jenis platform AI favorit) dan butir-butir pernyataan skala sikap.
2. **Data Sekunder**: Diperoleh melalui studi dokumentasi pedoman skripsi Universitas Gunadarma, artikel jurnal bereputasi internasional dan nasional, buku teks metodologi penelitian, serta data statistik pendukung dari program studi.

## Instrumen dan Uji Kelayakan Instrumen

### Uji Validitas Konstruk

Uji validitas instrumen bertujuan mengukur sejauh mana setiap butir pernyataan pada kuesioner mampu merefleksikan variabel yang hendak diukur. Validitas diuji melalui teknik korelasi *Pearson Product Moment*. Butir pernyataan dinyatakan valid apabila nilai koefisien korelasi hitung lebih besar dari $r_{\text{tabel}}$ pada tingkat signifikansi $\alpha = 0{,}05$:

$$r_{xy} = \frac{n\sum XY - (\sum X)(\sum Y)}{\sqrt{\left[n\sum X^2 - (\sum X)^2\right]\left[n\sum Y^2 - (\sum Y)^2\right]}}$$

Butir instrumen yang memiliki nilai $r_{\text{hitung}} < r_{\text{tabel}}$ atau nilai signifikansi $p > 0{,}05$ akan dieliminasi dari instrumen final.

### Uji Reliabilitas

Uji reliabilitas dilakukan untuk mengukur konsistensi internal instrumen kuesioner apabila dilakukan pengukuran berulang. Uji reliabilitas dihitung menggunakan formula *Cronbach's Alpha* ($\alpha$):

$$\alpha = \left(\frac{k}{k-1}\right) \left(1 - \frac{\sum \sigma_b^2}{\sigma_t^2}\right)$$

Suatu konstruk variabel dinyatakan reliabel dan andal apabila memiliki koefisien *Cronbach's Alpha* $\ge 0{,}70$.

## Teknik Analisis Data

Pengolahan data empiris dilakukan menggunakan perangkat lunak statistik (SPSS / SmartPLS) melalui serangkaian pengujian:

### Analisis Statistik Deskriptif

Statistik deskriptif digunakan untuk menyajikan gambaran umum profil responden dan tendensi sentral dari variabel penelitian melalui perhitungan nilai rata-rata (*mean*), standar deviasi, nilai minimum-maksimum, serta distribusi frekuensi persentase kategori penilaian.

### Uji Asumsi Klasik

Sebelum pengujian hipotesis regresi dilakukan, serangkaian uji asumsi klasik diterapkan untuk memastikan model estimasi bersifat *Best Linear Unbiased Estimator* (BLUE):

1. **Uji Normalitas**: Menguji residual data terdistribusi normal melalui uji statistik *Kolmogorov-Smirnov* (nilai Asymp. Sig. $> 0{,}05$) dan analisis visual grafik *Normal P-P Plot*.
2. **Uji Multikolinearitas**: Memastikan tidak terdapat korelasi sempurna antarvariabel bebas dengan mensyaratkan nilai *Variance Inflation Factor* (VIF) $< 10$ dan nilai *Tolerance* $> 0{,}10$.
3. **Uji Heteroskedastisitas**: Memastikan tidak timbul ketidaksamaan varians residual antar-pengamatan melalui uji *Glejser* atau pola grafik *scatterplot*.

### Analisis Regresi Linier Berganda dan Analisis Jalur

Untuk menguji pengaruh langsung faktor anteseden terhadap kecanduan AI ($Y$), disusun persamaan regresi berganda pertama:

$$Y = \alpha_1 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \epsilon_1$$

Sedangkan untuk menganalisis dampak kecanduan AI assistant terhadap produktivitas mahasiswa ($Z$), disusun persamaan struktural kedua:

$$Z = \alpha_2 + \beta_4 Y + \epsilon_2$$

Serta pengujian model simultan terpadu:

$$Z = \alpha_3 + \gamma_1 X_1 + \gamma_2 X_2 + \gamma_3 X_3 + \beta_5 Y + \epsilon_3$$

Keterangan notasi:
- $X_1, X_2, X_3$ : Faktor Teknologis, Psikologis, dan Lingkungan Sosial
- $Y$ : Tingkat Kecanduan *AI Assistant*
- $Z$ : Produktivitas Akademik Mahasiswa
- $\alpha$ : Nilai Konstanta Intersept
- $\beta_1 \dots \beta_5, \gamma_1 \dots \gamma_3$ : Koefisien Jalur / Koefisien Regresi
- $\epsilon_1, \epsilon_2, \epsilon_3$ : Nilai Galat Residual (*error term*)

### Uji Hipotesis Statistik

Pengujian keberartian parameter statistik dilakukan melalui:

1. **Uji Parsial (Uji t)**: Menguji pengaruh parsial variabel independen terhadap variabel dependen dengan kriteria penerimaan jika $t_{\text{hitung}} > t_{\text{tabel}}$ atau nilai $p < 0{,}05$.
2. **Uji Simultan (Uji F)**: Menguji apakah variabel bebas secara bersama-sama berpengaruh signifikan terhadap variabel terikat dengan kriteria $F_{\text{hitung}} > F_{\text{tabel}}$ atau $p < 0{,}05$.
3. **Koefisien Determinasi ($R^2$)**: Mengukur seberapa besar proporsi variasi variabel dependen dapat dijelaskan oleh variasi variabel-variabel independen dalam model.
4. **Uji Mediasi (*Sobel Test*)**: Menguji signifikansi pengaruh tidak langsung faktor anteseden terhadap produktivitas melalui perantaraan kecanduan *AI assistant*.
