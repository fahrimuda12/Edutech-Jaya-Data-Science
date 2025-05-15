# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000 dan dikenal menghasilkan lulusan berkualitas. Namun, dalam beberapa tahun terakhir, institusi ini menghadapi tantangan serius berupa tingginya tingkat dropout mahasiswa, yaitu siswa yang tidak menyelesaikan pendidikan mereka. Hal ini menimbulkan kekhawatiran terhadap reputasi institusi, efisiensi sumber daya, serta kualitas layanan akademik yang diberikan.

### Permasalahan Bisnis
1. Tingkat Dropout Mahasiswa yang Tinggi
   Banyak mahasiswa di Jaya Jaya Institut tidak menyelesaikan pendidikan mereka hingga lulus, yang mencerminkan adanya masalah serius dalam proses pendidikan atau dukungan yang diberikan.
2. Dampak Negatif pada Reputasi Institusi
   Angka dropout yang tinggi dapat menurunkan citra institusi di mata masyarakat, orang tua, dan calon mahasiswa baru, karena dianggap gagal menjaga keberhasilan akademik mahasiswanya.
3. Kesulitan dalam Perencanaan Akademik
   Tingginya dropout membuat manajemen sulit memprediksi kebutuhan jangka panjang seperti jumlah kelas, kapasitas ruang, kebutuhan pengajar, hingga anggaran pendidikan.
4. Risiko Menurunnya Kepercayaan dan Daya Saing
   Jika masalah ini tidak segera diatasi, institusi berisiko kehilangan kepercayaan publik dan tertinggal dari kompetitor dalam menarik dan mempertahankan mahasiswa.


### Cakupan Proyek
Proyek ini difokuskan pada upaya untuk memahami dan memprediksi potensi dropout mahasiswa di Jaya Jaya Institut berdasarkan data historis yang tersedia. Cakupan proyek meliputi:
1. Pengumpulan dan Pemahaman Data ✅
   - Menggunakan dataset performa mahasiswa yang telah disediakan oleh institusi.
   - Mengevaluasi kualitas data dan membersihkan data jika ditemukan nilai kosong, duplikat, atau anomali.

2. Eksplorasi dan Analisis Data (EDA) ✅
   - Menganalisis distribusi status mahasiswa (Dropout, Graduate, Enrolled).
   - Mengidentifikasi pola dan faktor-faktor penting yang berhubungan dengan dropout seperti nilai, status utang, kehadiran, dan beasiswa.

3. Pembangunan Model Prediksi Status Mahasiswa ✅
   - Menetapkan variabel target (Status) dan fitur-fitur prediktif.
   - Membangun model klasifikasi untuk memprediksi kemungkinan mahasiswa akan dropout.
   - Melakukan pelatihan, validasi, dan evaluasi model menggunakan metrik seperti akurasi, precision, recall, dan ROC-AUC.

4. Interpretasi Hasil dan Penentuan Faktor Kunci ✅
   - Menggunakan teknik seperti feature importance untuk mengidentifikasi variabel yang paling memengaruhi keputusan dropout.
   - Menyediakan insight yang actionable bagi pihak institusi.

5. Visualisasi dan Dashboard ✅
   - Menyusun dashboard interaktif menggunakan Metabase untuk:
   - Memantau status mahasiswa.
   - Mengidentifikasi mahasiswa yang berisiko dropout.
   - Menyediakan filter untuk analisis berdasarkan status, semester, course, dan status hubungan.

### Persiapan

Sumber data: [Jaya Jaya Institut - Performance Studet](dataset/data.csv)

Setup environment:
```
# Membuat virtual environment (Opsional)
python -m venv myenv
myenv\Scripts\activate

# Install depedency yang dibutuhkan
pip install -r requirements.txt

# Install Metabase untuk membuat dashboard
# Follow the official Metabase installation guide for your operating system

# Set up Jupyter Notebook untuk train model dan analysis data
pip install notebook

# Verify installation
python --version
pip list
```

## Business Dashboard
Untuk membantu Jaya Jaya Institut dalam memahami performa akademik mahasiswa serta memantau risiko dropout secara berkala, telah dibuat sebuah **business dashboard interaktif menggunakan Metabase**. Dashboard ini dirancang dengan fokus pada kemudahan interpretasi oleh pihak manajemen non-teknis, sehingga mereka dapat dengan cepat mengakses informasi penting tanpa perlu menganalisis data secara manual.

Dashboard [Student Dashboard](./Edutech%20Performance%20Student.pdf) yang ditampilkan memberikan visualisasi komprehensif terkait fenomena mahasiswa tidak selesai studi (dropout) dan secara efektif menjawab beberapa permasalahan utama yang dihadapi Jaya Jaya Inisitut, antara lain:

1. Tingginya Dropout Rate
   Dashboard menampilkan angka dropout 32.12%, memberi gambaran jelas tentang tingkat mahasiswa tidak selesai studi tinggi.

2. Pemahaman Penyebab Dropout
   Disajikan analisis faktor-faktor seperti:
   - Grafik rata-rata nilai ujian masuk dan semester per status
   - Course yang mengalami dropout
   - Perbandingann Dropout berdasarkan kategorikal seperti day attending evening
   - Perbandingan mahasiswa berdasarkan kategorikal terhadap statusnya
  
3. Monitoring Real-Time
   Dashboard dilengkapi filter interaktif (status pernikahan, status, course) untuk pantauan dinamis.

4. Antisipasi Dini
   Data dari dashboard bisa dijadikan dasar untuk membangun model prediktif risiko mahasiswa dropout. Ditambah machine learning yang dapat memberikan prediksi tersebut

5. Pengambilan Keputusan Lebih Tepat
   Visualisasi data mendukung kebijakan pihak institut berbasis insight dari data sumber, bukan asumsi.

6. Prediksi Risiko Dropout Mahasiswa Aktif
   Daftar mahasiswa aktif yang diklasifikasikan berdasarkan tingkat risiko (tinggi / rendah) berdasarkan prediktif analysis.

Kredensial Business Dashboard Metabase
```
username/email:root@mail.com
password:root123
```


## Menjalankan Sistem Machine Learning
Untuk menjalankan prototype sistem machine learning yang telah dibuat, ikuti langkah-langkah berikut:

1. **Persiapan Lingkungan**
   Pastikan semua library yang diperlukan telah terinstal. Jika belum, jalankan perintah berikut:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```

2. **Muat Dataset**
   Pastikan file `data.csv` tersedia di direktori kerja Anda. Dataset ini akan digunakan untuk pelatihan dan evaluasi model.

3. **Jalankan Notebook**
   Buka file `notebook.ipynb` menggunakan Jupyter Notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

4. **Langkah-Langkah dalam Notebook**
   - **Data Preprocessing**: Notebook akan memuat dataset, membersihkan data, dan melakukan encoding pada variabel kategorikal.
   - **Exploratory Data Analysis (EDA)**: Analisis data untuk memahami pola dan distribusi.
   - **Model Training**: Model machine learning (seperti Random Forest atau Logistic Regression) akan dilatih menggunakan data yang telah diproses.
   - **Model Evaluation**: Evaluasi model dilakukan menggunakan metrik seperti akurasi, precision, recall, dan ROC-AUC.
   - **Prediksi**: Model akan digunakan untuk memprediksi risiko dropout mahasiswa.

5. **Simpan Model**
   Model yang telah dilatih akan disimpan dalam format `.joblib` untuk digunakan di masa mendatang:
   ```python
   import joblib
   joblib.dump(model, 'rdf_model.joblib')
   ```

6. **Prototype Web atau API**
   Prototype dapat diakses melalui Streamlit Cloud. Jalankan aplikasi dengan perintah berikut:
   ```bash
   streamlit run app.py
   ```

7. **Akses Prototype**
   Prototype dapat diakses melalui Streamlit Cloud melalui alamat berikut `https://edutech-jaya-institut.streamlit.app/`.

## Conclusion
Proyek ini berhasil memberikan solusi berbasis data untuk mengetahui permasalahan tingginya tingkat dropout mahasiswa di Jaya Jaya Institut. Dengan memanfaatkan analisis data, model prediksi machine learning, dan dashboard interaktif, institusi kini memiliki alat yang efektif untuk memantau, menganalisis, dan mengantisipasi risiko dropout mahasiswa. Hasil proyek ini tidak hanya membantu dalam memahami faktor-faktor utama yang memengaruhi dropout, tetapi juga memberikan rekomendasi actionable untuk meningkatkan kualitas layanan akademik, efisiensi operasional, dan reputasi institusi secara keseluruhan. Berdasarkan business dashboard yang diberikan dan machine learning yang dibentuk kita juga dapat mengetahui karakteristik dari siswa yang terkena dropout antara lain:
1. Banyaknya kurikulum per-semester yang di setujui berbanding dengan kurikulum  yang di tolak
   Semakin kecil kurikulum yang disetujui dibadningkan dengan kurikulum yang di tolak per semester menadakan mahasiswa kemungkinan bakal dropout
2. Penurunan jarak antara nilai admission dengan nilai semester
   Semakin menurun antara nilai admission dengan nilai semesternya maka kemungkinan mahasiswa akan dropout
3. Nilai admission <120
   Mahasiswa dropout rata rata memiliki nilai admission yang kurang bagus dimana dibawah 120
4. Mahasiswa yang terkategori debtor (meminjam)
   Mahasiswa yang dropout didonimasi yang memiliki pinjaman
5. Jurusan dan waktu belajar
   Dropout paling banyak berasal dari Management dan yang mengambil kuliah di waktu malam

### Rekomendasi Action Items
- **Meningkatkan Dukungan Akademik**: Menyediakan program bimbingan belajar, mentoring, atau workshop untuk membantu mahasiswa yang kesulitan dalam akademik.
- **Peningkatan Sistem Monitoring**: Menggunakan dashboard untuk memantau performa mahasiswa secara real-time dan mengidentifikasi mahasiswa yang berisiko dropout lebih awal.
- **Pemberian Beasiswa atau Bantuan Keuangan**: Memberikan insentif finansial kepada mahasiswa yang membutuhkan untuk mengurangi beban ekonomi yang dapat menyebabkan dropout.
- **Peningkatan Keterlibatan Mahasiswa**: Mengadakan kegiatan ekstrakurikuler atau program pengembangan diri untuk meningkatkan keterlibatan dan kepuasan mahasiswa.
- **Optimalisasi Proses Penerimaan Mahasiswa**: Memperbaiki proses seleksi masuk untuk memastikan mahasiswa yang diterima memiliki kesiapan akademik dan motivasi yang cukup.
- **Evaluasi dan Perbaikan Kurikulum**: Menyesuaikan kurikulum agar lebih relevan dengan kebutuhan mahasiswa dan pasar kerja.
- **Peningkatan Komunikasi dengan Orang Tua/Wali**: Melibatkan orang tua/wali dalam memantau perkembangan akademik mahasiswa untuk memberikan dukungan tambahan.
- **Pengembangan Sistem Prediksi Risiko**: Menggunakan model machine learning untuk memprediksi risiko dropout dan mengambil tindakan preventif berdasarkan hasil prediksi.
- **Peningkatan Pelatihan untuk Dosen dan Staf**: Memberikan pelatihan kepada dosen dan staf untuk mengenali tanda-tanda mahasiswa yang berisiko dropout dan memberikan dukungan yang diperlukan.
- **Survei Kepuasan Mahasiswa**: Melakukan survei berkala untuk memahami kebutuhan dan tantangan yang dihadapi mahasiswa, serta menindaklanjuti hasil survei dengan tindakan konkret.
