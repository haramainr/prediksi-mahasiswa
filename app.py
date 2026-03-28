# ========================
# IMPORT LIBRARY
# ========================
import streamlit as st
import pandas as pd
import joblib

# ========================
# LOAD MODEL
# ========================
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# ========================
# CONFIG
# ========================
st.set_page_config(
    page_title="Prediksi Risiko Dropout Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

# ========================
# HEADER
# ========================
st.markdown("""
<h1 style='text-align: center; color: #2E86C1;'>🎓 Sistem Prediksi Risiko Dropout Mahasiswa</h1>
<p style='text-align: center; font-size: 16px; color: gray;'>
Membantu institusi pendidikan mengidentifikasi mahasiswa berisiko dropout sejak dini
</p>
""", unsafe_allow_html=True)

st.divider()

# ========================
# INPUT DATA
# ========================
st.subheader("📥 Input Data Mahasiswa")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Umur Mahasiswa", 15, 60, 20)
    admission_grade = st.number_input("Nilai Saat Masuk (0 - 10)", 0.0, 10.0, 6.0, step=0.5)
    prev_grade = st.number_input("Nilai Pendidikan Sebelumnya (0 - 10)", 0.0, 10.0, 6.0, step=0.5)
    approved_units = st.number_input("Jumlah Mata Kuliah Lulus (Semester 1)", 0, 10, 5)
    sem_grade = st.number_input("IPK Semester 1 (0 - 4)", 0.0, 4.0, 2.5, step=0.1)

with col2:
    enrolled_units = st.number_input("Jumlah Mata Kuliah Diambil (Semester 1)", 0, 15, 6)
    evaluations = st.number_input("Jumlah Evaluasi/Ujian (Semester 1)", 0, 20, 8)
    scholarship_input = st.selectbox("Penerima Beasiswa", ["Tidak", "Ya"])
    scholarship = 1 if scholarship_input == "Ya" else 0
    tuition_input = st.selectbox("Status Pembayaran UKT", ["Menunggak", "Lunas"])
    tuition = 1 if tuition_input == "Lunas" else 0

st.divider()

# ========================
# PREDIKSI
# ========================
if st.button("🔍 Prediksi Sekarang"):

    input_data = pd.DataFrame({
        'Curricular_units_1st_sem_approved': [approved_units],
        'Curricular_units_1st_sem_grade': [sem_grade],
        'Curricular_units_1st_sem_enrolled': [enrolled_units],
        'Curricular_units_1st_sem_evaluations': [evaluations],
        'Admission_grade': [admission_grade],
        'Previous_qualification_grade': [prev_grade],
        'Age_at_enrollment': [age],
        'Tuition_fees_up_to_date': [tuition],
        'Scholarship_holder': [scholarship]
    })

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0]

    # ========================
    # HANDLE HASIL
    # ========================
    if prediction == 0 or prediction == "Dropout":
        result = "Dropout"
    else:
        result = "Lulus"

    # ========================
    # CONFIDENCE
    # ========================
    if len(proba) == 2:
        confidence = max(proba)
    else:
        confidence = 1.0

    # ========================
    # RISK LEVEL
    # ========================
    if result == "Dropout":
        if confidence > 0.8:
            risk = "Tinggi 🔴"
        elif confidence > 0.6:
            risk = "Sedang 🟡"
        else:
            risk = "Rendah 🟢"
    else:
        risk = "Rendah 🟢"

    st.divider()

    # ========================
    # HASIL UTAMA
    # ========================
    st.subheader("📊 Hasil Prediksi")

    if result == "Dropout":
        st.error("⚠️ Risiko Tinggi Dropout")
    else:
        st.success("🎓 Berpotensi Lulus")

    st.markdown(f"## Status: **{result}**")

    # ========================
    # SUMMARY
    # ========================
    st.markdown("### 📌 Ringkasan")
    st.write(f"""
    - Status: **{result}**
    - Tingkat Risiko: **{risk}**
    - Confidence: **{confidence*100:.1f}%**
    """)

    # ========================
    # PROGRESS BAR
    # ========================
    st.subheader("📊 Tingkat Keyakinan Visual")
    st.progress(int(confidence * 100))

    # ========================
    # INTERPRETASI
    # ========================
    st.subheader("🧠 Interpretasi")

    if result == "Dropout":
        st.write("Mahasiswa memiliki indikasi risiko dropout dan memerlukan perhatian khusus.")
    else:
        st.write("Mahasiswa menunjukkan performa yang baik dan berpotensi lulus.")

    # ========================
    # FAKTOR RISIKO
    # ========================
    st.subheader("🔍 Faktor Risiko")

    if sem_grade < 2.5:
        st.write("- IPK rendah meningkatkan risiko dropout")

    if approved_units < 4:
        st.write("- Jumlah mata kuliah lulus rendah")

    if tuition == 0:
        st.write("- Terdapat masalah pembayaran UKT")

    if scholarship == 0:
        st.write("- Tidak menerima beasiswa")

    # ========================
    # REKOMENDASI
    # ========================
    st.subheader("💡 Rekomendasi")

    if result == "Dropout":
        st.write("""
        - Berikan bimbingan akademik tambahan  
        - Monitoring rutin performa mahasiswa  
        - Evaluasi kondisi finansial mahasiswa  
        """)
    else:
        st.write("""
        - Pertahankan performa akademik  
        - Monitoring berkala  
        """)

    st.info("Gunakan hasil ini sebagai indikator awal, bukan keputusan final.")

    st.divider()

    # ========================
    # RINGKASAN DATA
    # ========================
    st.subheader("📋 Ringkasan Data")

    summary_df = pd.DataFrame({
        "Fitur": ["IPK", "MK Lulus", "UKT", "Beasiswa"],
        "Nilai": [
            sem_grade,
            approved_units,
            "Lunas" if tuition == 1 else "Menunggak",
            "Ya" if scholarship == 1 else "Tidak"
        ]
    })

    st.table(summary_df)

# ========================
# FOOTER
# ========================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Designed by Haramain Rabbany</p>",
    unsafe_allow_html=True
)