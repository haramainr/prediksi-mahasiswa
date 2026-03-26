# 🎓 Prediksi Dropout Mahasiswa - Jaya Jaya Institut

## 📌 Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan yang memiliki permasalahan tingginya angka mahasiswa dropout. Hal ini dapat berdampak pada reputasi dan kualitas institusi.

### 🎯 Tujuan Proyek
Membangun sistem prediksi untuk mengidentifikasi mahasiswa yang berpotensi dropout sehingga dapat dilakukan tindakan preventif lebih awal.

---

## 📊 Data Understanding

Dataset yang digunakan berisi informasi terkait performa mahasiswa, termasuk data akademik dan demografis.

### 🔍 Insight:
- Tidak terdapat missing values pada dataset.
- Distribusi status mahasiswa terdiri dari dropout, enrolled, dan graduate.
- Admission grade dan umur memiliki pengaruh terhadap status mahasiswa.
- Mahasiswa dengan nilai rendah cenderung memiliki risiko dropout lebih tinggi.

---

## 🧹 Data Preparation

Tahapan preprocessing yang dilakukan:
- Encoding data kategorikal menjadi numerik
- Pemisahan fitur dan target
- Pembagian data training dan testing
- Normalisasi data menggunakan StandardScaler

---

## 🤖 Modeling

Model yang digunakan:
- Random Forest Classifier

Alasan pemilihan:
- Cocok untuk data tabular
- Mampu menangani kompleksitas data
- Memiliki performa yang stabil

---

## 📈 Evaluation

Model dievaluasi menggunakan:
- Classification Report
- Confusion Matrix
- Accuracy Score

### 📊 Hasil:
Model mampu memprediksi status mahasiswa dengan performa yang cukup baik, meskipun masih terdapat beberapa kesalahan prediksi.

---

## 💡 Conclusion

Model machine learning yang dibangun dapat digunakan untuk memprediksi kemungkinan mahasiswa mengalami dropout.

Dengan adanya sistem ini, institusi dapat melakukan intervensi lebih awal untuk mengurangi angka dropout.

---

## 🚀 Deployment (Streamlit)

Aplikasi dapat dijalankan menggunakan Streamlit.

### ▶️ Cara Menjalankan:
```bash
streamlit run app.py