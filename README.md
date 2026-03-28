# 🎓 Proyek Akhir: Prediksi Risiko Dropout Mahasiswa

## 📌 Business Understanding

Dropout mahasiswa merupakan salah satu permasalahan utama dalam institusi pendidikan tinggi karena dapat memengaruhi kualitas lulusan, akreditasi, serta reputasi institusi. Oleh karena itu, diperlukan sistem yang mampu mengidentifikasi mahasiswa yang berisiko dropout sejak dini.

Dengan memanfaatkan machine learning, institusi dapat melakukan intervensi lebih awal untuk meningkatkan tingkat kelulusan mahasiswa.

---

## ❗ Permasalahan Bisnis

* Bagaimana mengidentifikasi mahasiswa yang berisiko dropout sejak dini?
* Faktor apa saja yang memengaruhi risiko dropout mahasiswa?
* Bagaimana membantu institusi dalam pengambilan keputusan berbasis data?

---

## 🎯 Tujuan Proyek

* Membangun model machine learning untuk memprediksi risiko dropout mahasiswa
* Mengidentifikasi faktor-faktor utama yang memengaruhi dropout
* Menyediakan dashboard analisis untuk membantu pengambilan keputusan

---

## 📊 Cakupan Proyek

Proyek ini mencakup:

* Data preprocessing dan eksplorasi data (EDA)
* Feature selection dan training model
* Evaluasi model machine learning
* Pembuatan dashboard interaktif (Tableau)
* Pembuatan prototype aplikasi (Streamlit)

---

## 📁 Sumber Data

Dataset berisi informasi mahasiswa yang mencakup:

* Performa akademik
* Demografi
* Faktor finansial

Dataset:
https://raw.githubusercontent.com/haramainr/prediksi-mahasiswa/refs/heads/main/data.csv

---

## ⚙️ Persiapan

### 1. Clone Repository

```bash
git clone https://github.com/username/repo.git
cd repo
```

### 2. Membuat Virtual Environment

```bash
python -m venv venv
```

### 3. Mengaktifkan Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Menjalankan Aplikasi

```bash
streamlit run app.py
```

---

## 🤖 Machine Learning

### 🎯 Target

Model dikembangkan untuk mengklasifikasikan mahasiswa menjadi dua kategori:

* Dropout
* Graduate

> Data dengan status **Enrolled tidak digunakan dalam training**, karena belum memiliki label akhir.

---

### 🧠 Fitur yang Digunakan

* Nilai saat masuk
* Nilai pendidikan sebelumnya
* IPK semester 1
* Jumlah mata kuliah lulus
* Jumlah mata kuliah diambil
* Jumlah evaluasi
* Umur mahasiswa
* Status pembayaran UKT
* Status beasiswa

---

## 📊 Analisis Data

Hasil eksplorasi data menunjukkan beberapa pola penting:

* Mahasiswa dengan IPK semester 1 rendah memiliki risiko dropout yang lebih tinggi
* Rata-rata IPK mahasiswa dropout lebih rendah dibandingkan mahasiswa yang lulus
* Mahasiswa dengan tunggakan pembayaran memiliki proporsi dropout yang lebih tinggi
* Penerima beasiswa cenderung memiliki tingkat kelulusan yang lebih baik
* Usia yang lebih tinggi saat masuk kuliah cenderung memiliki risiko dropout lebih besar

---

## 📊 Business Dashboard

Tableau:
https://public.tableau.com/app/profile/haramain.rabbany/viz/StudentPerformanceDashboard_17745517906740/Dashboard1?publish=yes

---

### 📈 Insight Utama

* Performa akademik semester pertama menjadi indikator paling kuat terhadap kelulusan mahasiswa
* Faktor finansial seperti status pembayaran memiliki pengaruh signifikan terhadap risiko dropout
* Beasiswa berkontribusi dalam meningkatkan peluang kelulusan
* Faktor demografis seperti usia dan gender turut memengaruhi risiko dropout

---

## 🚀 Prototype Machine Learning

Streamlit:
https://prediksi-mahasiswa-wrzknxdrdmakq7spc9vbgr.streamlit.app/

---

### 🧪 Cara Menggunakan

1. Input data mahasiswa
2. Klik tombol **Prediksi**
3. Sistem akan menampilkan:

   * Status prediksi (Dropout / Graduate)
   * Tingkat keyakinan model
   * Interpretasi hasil

---

## 📌 Conclusion

Berdasarkan hasil pemodelan yang telah dilakukan, model machine learning mampu memprediksi status mahasiswa (Dropout dan Graduate) dengan akurasi sebesar **87%**.

Hasil evaluasi model menunjukkan:

* Precision dan recall pada kedua kelas sudah cukup baik
* Recall untuk kelas Dropout sebesar **76%**, menunjukkan model cukup mampu mengidentifikasi mahasiswa yang berisiko dropout
* Recall untuk kelas Graduate sebesar **95%**, menunjukkan model sangat baik dalam mengenali mahasiswa yang akan lulus

Insight utama yang diperoleh:

* Performa akademik di semester pertama menjadi faktor paling berpengaruh terhadap kelulusan mahasiswa
* Mahasiswa dengan tunggakan pembayaran memiliki risiko dropout lebih tinggi
* Faktor akademik dan finansial merupakan indikator utama dalam menentukan status mahasiswa

Model ini dapat digunakan sebagai sistem **early warning** untuk membantu institusi pendidikan dalam melakukan intervensi lebih dini guna menekan angka dropout.

---

## 💡 Rekomendasi Action Items

Berdasarkan hasil analisis data dan performa model machine learning, berikut rekomendasi yang dapat dilakukan oleh institusi:

1. **Monitoring Mahasiswa Berisiko Tinggi**

   * Gunakan model machine learning untuk mengidentifikasi mahasiswa dengan probabilitas dropout tinggi sejak semester awal

2. **Intervensi Akademik Dini**

   * Fokus pada mahasiswa dengan performa akademik rendah di semester pertama
   * Sediakan program mentoring dan bimbingan belajar tambahan

3. **Dukungan Finansial**

   * Prioritaskan bantuan kepada mahasiswa dengan status pembayaran tertunggak
   * Perluas akses beasiswa untuk menekan risiko dropout

4. **Sistem Early Warning Terintegrasi**

   * Integrasikan model ke dalam dashboard monitoring untuk pemantauan real-time
   * Gunakan hasil prediksi sebagai dasar pengambilan keputusan

5. **Evaluasi dan Pengembangan Model**

   * Lakukan retraining model secara berkala dengan data terbaru
   * Tingkatkan performa model terutama dalam mendeteksi mahasiswa dropout
