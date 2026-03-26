# Proyek Akhir: Prediksi Risiko Dropout Mahasiswa

## 📌 Business Understanding

### Latar Belakang

Jaya Jaya Institut merupakan institusi pendidikan yang telah menghasilkan banyak lulusan berkualitas. Namun, terdapat permasalahan tingginya jumlah mahasiswa yang tidak menyelesaikan pendidikan (dropout). Hal ini dapat berdampak pada reputasi institusi dan efektivitas sistem pendidikan.

### Permasalahan Bisnis

* Tingginya angka dropout mahasiswa
* Sulitnya mendeteksi mahasiswa yang berisiko dropout sejak dini
* Kurangnya insight berbasis data untuk mendukung pengambilan keputusan

### Cakupan Proyek

* Analisis data performa mahasiswa
* Pembuatan dashboard untuk monitoring performa
* Pengembangan model machine learning untuk prediksi status mahasiswa

---

## ⚙️ Persiapan

### Sumber Data

Dataset dapat diakses melalui link berikut:
👉 https://raw.githubusercontent.com/haramainr/prediksi-mahasiswa/refs/heads/main/data.csv

### Setup Environment

```bash
pip install -r requirements.txt
```

---

## 📊 Business Dashboard

Dashboard dibuat menggunakan Tableau untuk membantu memahami performa mahasiswa dan faktor yang mempengaruhi status mereka.

👉 Link Dashboard:
https://public.tableau.com/app/profile/haramain.rabbany/viz/StudentPerformanceDashboard_17745517906740/Dashboard1?publish=yes

### Insight Utama:

* Mahasiswa dengan performa rendah di semester pertama memiliki risiko dropout lebih tinggi
* Jumlah mahasiswa yang lulus lebih tinggi dibandingkan dropout, namun dropout tetap signifikan
* Usia saat masuk memiliki pengaruh terhadap performa akademik mahasiswa

---

## 🤖 Menjalankan Sistem Machine Learning

Prototype sistem dibuat menggunakan Streamlit.

👉 Link Aplikasi:
https://prediksi-mahasiswa-wrzknxdrdmakq7spc9vbgr.streamlit.app/

### Cara Menjalankan Secara Lokal:

```bash
streamlit run app.py
```

### Cara Menggunakan:

1. Input data mahasiswa
2. Klik tombol prediksi
3. Sistem akan menampilkan status mahasiswa:

   * Dropout
   * Enrolled
   * Graduate

---

## 📈 Conclusion

Berdasarkan analisis data dan model yang dikembangkan, performa akademik mahasiswa terutama pada semester pertama memiliki pengaruh signifikan terhadap kemungkinan kelulusan. Selain itu, faktor usia juga menunjukkan adanya hubungan terhadap risiko dropout.

Model machine learning yang dikembangkan mampu membantu dalam mengidentifikasi mahasiswa yang berpotensi dropout sehingga institusi dapat memberikan intervensi lebih awal.

---

## 🎯 Rekomendasi Action Items

* Melakukan monitoring khusus terhadap mahasiswa dengan performa rendah di semester pertama
* Memberikan program bimbingan atau mentoring untuk mahasiswa berisiko tinggi
* Mengembangkan sistem early warning berbasis data untuk deteksi dropout
* Mengoptimalkan proses evaluasi akademik untuk meningkatkan tingkat kelulusan

---
