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

   * Status prediksi (Dropout / Lulus)
   * Tingkat keyakinan model
   * Interpretasi hasil

---

## 📌 Conclusion

Berdasarkan hasil analisis dan pemodelan, ditemukan bahwa faktor akademik dan finansial memiliki pengaruh paling signifikan terhadap risiko dropout mahasiswa.

Mahasiswa dengan performa akademik rendah pada semester pertama, seperti IPK rendah dan jumlah mata kuliah lulus yang sedikit, memiliki kecenderungan lebih tinggi untuk mengalami dropout. Selain itu, faktor finansial seperti status pembayaran UKT juga menjadi indikator penting, di mana mahasiswa dengan tunggakan lebih berisiko tidak melanjutkan studi.

Model machine learning yang dibangun menunjukkan performa yang cukup baik dengan hasil sebagai berikut:

* Accuracy: **87%**
* Precision: **88%**
* Recall: **87%**

Hal ini menunjukkan bahwa model mampu mengidentifikasi mahasiswa berisiko dropout dengan cukup akurat.

Dengan adanya model ini, institusi dapat menerapkan sistem **early warning** untuk mendeteksi mahasiswa berisiko sejak dini dan melakukan intervensi yang lebih tepat sasaran.

---

## 💡 Rekomendasi Action Items

Berdasarkan hasil analisis dan model yang telah dibuat, berikut beberapa rekomendasi:

1. **Monitoring Akademik**

   * Identifikasi mahasiswa dengan IPK rendah sejak semester pertama
   * Berikan program mentoring atau bimbingan tambahan

2. **Intervensi Finansial**

   * Prioritaskan bantuan bagi mahasiswa dengan tunggakan pembayaran
   * Perluas program beasiswa

3. **Early Warning System**

   * Implementasikan model machine learning sebagai sistem deteksi dini
   * Integrasikan dengan dashboard monitoring

4. **Pendekatan Personal**

   * Lakukan pendekatan khusus pada mahasiswa berisiko tinggi
   * Pertimbangkan faktor demografis

5. **Evaluasi Berkala**

   * Lakukan monitoring performa mahasiswa secara rutin
   * Perbarui model secara berkala
