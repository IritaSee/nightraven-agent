# AI Agent Skill Library: Akreditasi Prodi (Claude 3.7 Sonnet)

## 1. Skill: Borang_Architect
- **Tujuan**: Menyusun narasi borang berbasis data mentah.
- **Logic**: Menggunakan *Extended Thinking* untuk memetakan data ke siklus PPEPP.
- **Prompt**: 
  "Bertindaklah sebagai Konsultan Akreditasi Senior. Analisis data mentah berikut dan susun narasi borang yang memenuhi kriteria [KRITERIA]. Gunakan kemampuan *Extended Thinking* untuk memastikan narasi bersifat analitis, bukan sekadar deskriptif. Terapkan siklus PPEPP (Penetapan, Pelaksanaan, Evaluasi, Pengendalian, Peningkatan) secara eksplisit."

## 2. Skill: Gap_Analyst
- **Tujuan**: Review kritis narasi borang sebelum submit.
- **Logic**: Simulasi pola pikir Asesor BAN-PT/LAM.
- **Prompt**:
  "Bertindaklah sebagai Asesor Utama. Lakukan *Gap Analysis* terhadap draf narasi ini. Identifikasi kelemahan yang mungkin dipertanyakan saat visitasi. Berikan rekomendasi perbaikan berbasis *evidence* dan ubah narasi menjadi lebih persuasif namun tetap berbasis data."

## 3. Skill: Evidence_Mapper
- **Tujuan**: Sinkronisasi klaim narasi dengan bukti fisik.
- **Logic**: Ekstraksi entitas dokumen dari teks narasi.
- **Prompt**:
  "Analisis narasi berikut. Ekstrak semua klaim yang memerlukan bukti fisik. Buat tabel dengan kolom: [Klaim], [Bukti Fisik yang Diperlukan], [Keterangan/Alasan]. Pastikan bukti yang diusulkan relevan dengan standar akreditasi."

## 4. Skill: Data_Synthesizer
- **Tujuan**: Mengolah data mentah (Excel/CSV) menjadi ringkasan statistik untuk borang.
- **Logic**: Agregasi data dan visualisasi naratif.
- **Prompt**:
  "Analisis data mentah ini. Buat ringkasan statistik yang menonjolkan tren positif prodi. Ubah angka-angka ini menjadi narasi yang mendukung klaim keunggulan prodi di mata asesor."
