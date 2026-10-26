# KATA PENGANTAR {-}

Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, dan karunia-Nya, sehingga proposal skripsi yang berjudul **"Analisis Faktor-Faktor Penyebab Kecanduan Penggunaan AI Assistant dan Dampaknya terhadap Produktivitas Mahasiswa"** dapat terselesaikan dengan baik. Proposal ini disusun sebagai salah satu syarat untuk menyelesaikan program studi Strata Satu (S-1) pada Program Studi Sistem Informasi, Fakultas Ilmu Komputer dan Teknologi Informasi, Universitas Gunadarma.

Penyusunan proposal skripsi ini tidak lepas dari bimbingan, arahan, dan bantuan moril maupun materiil dari berbagai pihak. Oleh karena itu, dengan kerendahan hati, penulis menyampaikan rasa hormat dan terima kasih yang sebesar-besarnya kepada:

1. Prof. Dr. E. S. Margianti, S.E., M.M., selaku Rektor Universitas Gunadarma.
2. [PERLU DATA: Nama Dekan beserta Gelar], selaku Dekan Fakultas Ilmu Komputer dan Teknologi Informasi, Universitas Gunadarma.
3. [PERLU DATA: Nama Ketua Jurusan beserta Gelar], selaku Ketua Program Studi Sistem Informasi, Universitas Gunadarma.
4. Kepala Bagian Sidang Skripsi Universitas Gunadarma beserta seluruh staf sekretariat yang telah membantu kelancaran administrasi akademik.
5. Bapak Lolak Jiakrlo, M.Kom., selaku Dosen Pembimbing yang telah meluangkan waktu, memberikan bimbingan, arahan analitis, saran ilmiah, serta motivasi yang berharga dalam penyusunan karya ilmiah ini.
6. Rekan-rekan mahasiswa Program Studi Sistem Informasi angkatan [PERLU DATA: angkatan], serta seluruh sahabat yang senantiasa saling mendukung dalam proses perkuliahan dan penyusunan proposal ini.
7. Kedua orang tua tercinta dan keluarga besar, atas doa tulus, kasih sayang tanpa henti, kesabaran, serta pengorbanan yang tak ternilai bagi keberhasilan studi penulis.

Penulis menyadari sepenuhnya bahwa proposal skripsi ini masih memiliki keterbatasan. Oleh sebab itu, kritik dan saran yang konstruktif dari para pembaca sangat diharapkan demi penyempurnaan laporan skripsi pada tahap berikutnya. Semoga karya ilmiah ini dapat memberikan sumbangsih pemikiran yang bermanfaat bagi pengembangan ilmu sistem informasi dan institusi Universitas Gunadarma.

```{=typst}
#v(0.8cm)
#align(right)[
  Depok, Oktober 2026

  #v(1cm)
  Farchan G
]
#pagebreak()
#outline(
  title: [#align(center)[#text(size: 14pt, weight: "bold")[DAFTAR ISI]]],
  depth: 3,
)
#context {
  if opt-daftar-gambar {
    let imgs = query(figure.where(kind: image))
    if imgs.len() > 0 {
      pagebreak()
      outline(
        title: align(center)[#text(size: 14pt, weight: "bold")[DAFTAR GAMBAR]],
        target: figure.where(kind: image),
      )
    }
  }
  if opt-daftar-tabel {
    let tbls = query(figure.where(kind: table))
    if tbls.len() > 0 {
      pagebreak()
      outline(
        title: align(center)[#text(size: 14pt, weight: "bold")[DAFTAR TABEL]],
        target: figure.where(kind: table),
      )
    }
  }
}
#pagebreak()
#set page(numbering: "1")
#counter(page).update(1)
```

```{=openxml}
<w:p><w:pPr><w:jc w:val="right"/><w:spacing w:before="454"/></w:pPr><w:r><w:t>Depok, Oktober 2026</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="right"/><w:spacing w:before="567"/></w:pPr><w:r><w:t>Farchan G</w:t></w:r></w:p>
```
