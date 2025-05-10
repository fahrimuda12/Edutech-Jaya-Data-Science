# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000 dan dikenal menghasilkan lulusan berkualitas. Namun, dalam beberapa tahun terakhir, institusi ini menghadapi tantangan serius berupa tingginya tingkat dropout mahasiswa, yaitu siswa yang tidak menyelesaikan pendidikan mereka. Hal ini menimbulkan kekhawatiran terhadap reputasi institusi, efisiensi sumber daya, serta kualitas layanan akademik yang diberikan.

### Permasalahan Bisnis
1. Tingkat Dropout Mahasiswa yang Tinggi
   Banyak mahasiswa di Jaya Jaya Institut tidak menyelesaikan pendidikan mereka hingga lulus, yang mencerminkan adanya masalah serius dalam proses pendidikan atau dukungan yang diberikan.
2. Dampak Negatif pada Reputasi Institusi
   Angka dropout yang tinggi dapat menurunkan citra institusi di mata masyarakat, orang tua, dan calon mahasiswa baru, karena dianggap gagal menjaga keberhasilan akademik mahasiswanya.
3. Pemborosan Sumber Daya 
   Mahasiswa yang tidak menyelesaikan studi tetap menyerap sumber daya seperti dosen, fasilitas kampus, dan biaya operasional lainnya yang akhirnya tidak memberikan hasil maksimal.
4. Kesulitan dalam Perencanaan Akademik
   Tingginya dropout membuat manajemen sulit memprediksi kebutuhan jangka panjang seperti jumlah kelas, kapasitas ruang, kebutuhan pengajar, hingga anggaran pendidikan.
5. Risiko Menurunnya Kepercayaan dan Daya Saing
   Jika masalah ini tidak segera diatasi, institusi berisiko kehilangan kepercayaan publik dan tertinggal dari kompetitor dalam menarik dan mempertahankan mahasiswa.


### Cakupan Proyek
Proyek ini difokuskan pada upaya untuk memahami dan memprediksi potensi dropout mahasiswa di Jaya Jaya Institut berdasarkan data historis yang tersedia. Cakupan proyek meliputi:
1. Pengumpulan dan Pemahaman Data ✅
   - Menggunakan dataset performa mahasiswa yang telah disediakan oleh institusi.
   - Mengevaluasi kualitas data dan membersihkan data jika ditemukan nilai kosong, duplikat, atau anomali.

2. Eksplorasi dan Analisis Data (EDA) ✅
   - Menganalisis distribusi status mahasiswa (Dropout, Graduate, Enrolled).
   - Mengidentifikasi pola dan faktor-faktor penting yang berhubungan dengan dropout seperti nilai, status utang, kehadiran, dan beasiswa.

3. Pembangunan Model Prediksi Dropout
   - Menetapkan variabel target (Status) dan fitur-fitur prediktif.
   - Membangun model klasifikasi untuk memprediksi kemungkinan mahasiswa akan dropout.
   - Melakukan pelatihan, validasi, dan evaluasi model menggunakan metrik seperti akurasi, precision, recall, dan ROC-AUC.

4. Interpretasi Hasil dan Penentuan Faktor Kunci
   - Menggunakan teknik seperti feature importance untuk mengidentifikasi variabel yang paling memengaruhi keputusan dropout.
   - Menyediakan insight yang actionable bagi pihak institusi.

5. Visualisasi dan Dashboard
   - Menyusun dashboard interaktif menggunakan Metabase untuk:
   - Memantau status mahasiswa.
   - Mengidentifikasi mahasiswa yang berisiko dropout.
   - Menyediakan filter untuk analisis berdasarkan jurusan, semester, atau faktor risiko.

6. Rekomendasi Strategis
   - Memberikan saran berbasis data untuk mendukung pencegahan dropout, seperti pemberian bimbingan, intervensi finansial, atau dukungan akademik.



### Persiapan

Sumber data: data.csv

Setup environment:
```
# Install necessary Python libraries
pip install pandas numpy matplotlib seaborn scikit-learn

# Install Metabase for dashboard creation
# Follow the official Metabase installation guide for your operating system

# Set up Jupyter Notebook for analysis
pip install notebook

# Verify installation
python --version
pip list
```

## Business Dashboard
Untuk membantu Jaya Jaya Institut dalam memahami performa akademik mahasiswa serta memantau risiko dropout secara berkala, telah dibuat sebuah **business dashboard interaktif menggunakan Metabase**. Dashboard ini dirancang dengan fokus pada kemudahan interpretasi oleh pihak manajemen non-teknis, sehingga mereka dapat dengan cepat mengakses informasi penting tanpa perlu menganalisis data secara manual.

Dashboard [Attrition Dashboard](./Attrition%20Dashboard.pdf) yang ditampilkan memberikan visualisasi komprehensif terkait fenomena karyawan keluar (attrition) dan secara efektif menjawab beberapa permasalahan utama yang dihadapi divisi HR Maju Maju Jaya, antara lain:

1. Distribusi Status Mahasiswa
   Visualisasi pie chart atau bar chart untuk melihat proporsi mahasiswa berdasarkan status akademik.

2. Faktor Dropout Teratas
   Tabel dan grafik yang menunjukkan pengaruh variabel seperti Debtor, Tuition_fees_up_to_date, dan Curricular_units_grade terhadap dropout.

3. Prediksi Risiko Dropout Mahasiswa Aktif
   Daftar mahasiswa aktif yang diklasifikasikan berdasarkan tingkat risiko (tinggi / rendah) berdasarkan model prediktif.

4. Filter Dinamis
   Pengguna dapat memfilter data berdasarkan jurusan, jenis kelamin, beasiswa, semester, dan lainnya untuk analisis yang lebih terfokus.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
