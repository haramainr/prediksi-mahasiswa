# 🎓 Proyek Akhir: Prediksi Risiko Dropout Mahasiswa

## 📌 Business Understanding

Dropout mahasiswa merupakan salah satu permasalahan utama dalam institusi pendidikan tinggi karena dapat memengaruhi kualitas lulusan, akreditasi, serta reputasi institusi. Oleh karena itu, diperlukan sistem yang mampu mengidentifikasi mahasiswa yang berisiko dropout sejak dini.

Dengan memanfaatkan machine learning, institusi dapat melakukan intervensi lebih awal untuk meningkatkan tingkat kelulusan mahasiswa.

---

## ❗ Permasalahan Bisnis

* Bagaimana mengidentifikasi mahasiswa yang berisiko dropout sejak dini?
* Faktor apa saja yang memengaruhi risiko dropout mahasiswa?
* Bagaimana membantu institusi dalam mengambil keputusan berbasis data?

---

## 🎯 Tujuan Proyek

* Membangun model machine learning untuk memprediksi risiko dropout mahasiswa
* Mengidentifikasi faktor-faktor utama yang memengaruhi dropout
* Menyediakan dashboard analisis untuk membantu pengambilan keputusan

---

## 📊 Cakupan Proyek

Proyek ini mencakup:

* Data preprocessing dan eksplorasi data
* Feature selection dan training model
* Evaluasi model machine learning
* Pembuatan dashboard interaktif (Tableau)
* Pembuatan prototype aplikasi (Streamlit)

---

## 📁 Sumber Data

Dataset berisi informasi mahasiswa seperti performa akademik, demografi, dan finansial.

📌 Dataset:
https://raw.githubusercontent.com/haramainr/prediksi-mahasiswa/refs/heads/main/data.csv

---

## ⚙️ Persiapan

### 🔧 Setup Environment

pip install -r requirements.txt

### ▶️ Menjalankan Aplikasi

streamlit run app.py

---

## 🤖 Machine Learning

### 🎯 Target

Prediksi status mahasiswa:

* Dropout
* Graduate

> Data Enrolled tidak digunakan dalam training karena belum memiliki label akhir.

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

## 📊 Business Dashboard

👉 Tableau:
https://public.tableau.com/app/profile/haramain.rabbany/viz/StudentPerformanceDashboard_17745517906740/Dashboard1?publish=yes

---

### 📈 Insight Utama

* Performa akademik semester 1 sangat memengaruhi kelulusan mahasiswa
* Mahasiswa dengan tunggakan pembayaran memiliki risiko dropout lebih tinggi
* Penerima beasiswa cenderung memiliki tingkat kelulusan lebih baik
* Faktor demografi seperti usia dan gender juga berpengaruh

---

## 🚀 Prototype Machine Learning

👉 Streamlit:
https://prediksi-mahasiswa-wrzknxdrdmakq7spc9vbgr.streamlit.app/

---

### 🧪 Cara Menggunakan

1. Input data mahasiswa
2. Klik tombol Prediksi
3. Lihat hasil prediksi dan tingkat keyakinan model

---

## 📌 Conclusion

Model machine learning dapat membantu mengidentifikasi mahasiswa berisiko dropout. Faktor akademik dan finansial menjadi indikator utama.

---

## 💡 Rekomendasi

* Intervensi akademik untuk mahasiswa berisiko
* Bantuan finansial bagi mahasiswa yang mengalami kesulitan
* Monitoring performa secara berkala menggunakan dashboard
