# Import library
import streamlit as st
import pandas as pd
import joblib

# Load model & scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# ========================
# PAGE CONFIG
# ========================
st.set_page_config(
    page_title="Prediksi Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

# ========================
# STYLE
# ========================
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ========================
# HEADER
# ========================
st.markdown('<div class="title">🎓 Prediksi Status Mahasiswa</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Prediksi apakah mahasiswa akan Dropout, Enrolled, atau Graduate</div>', unsafe_allow_html=True)

# ========================
# INPUT
# ========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📥 Input Data Mahasiswa")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Umur", 15, 60, 20)
    admission_grade = st.number_input("Admission Grade", 0.0, 200.0, 120.0)

with col2:
    prev_grade = st.number_input("Previous Qualification Grade", 0.0, 200.0, 120.0)
    approved_units = st.number_input("Jumlah Mata Kuliah Lulus (Semester 1)", 0, 10, 5)

predict_btn = st.button("🔍 Prediksi")

st.markdown('</div>', unsafe_allow_html=True)

# ========================
# PREDICTION
# ========================
if predict_btn:

    input_data = pd.DataFrame({
        'Age_at_enrollment': [age],
        'Admission_grade': [admission_grade],
        'Previous_qualification_grade': [prev_grade],
        'Curricular_units_1st_sem_approved': [approved_units]
    })

    input_scaled = scaler.transform(input_data)

    # Prediksi kelas
    prediction = model.predict(input_scaled)

    # Probabilitas
    proba = model.predict_proba(input_scaled)[0]

    status_map = {
        0: "Dropout",
        1: "Enrolled",
        2: "Graduate"
    }

    result = status_map.get(prediction[0], "Unknown")

    # ========================
    # OUTPUT
    # ========================
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Hasil Prediksi")

    if result == "Dropout":
        st.error("⚠️ Mahasiswa berpotensi Dropout")
        st.write("Disarankan untuk memberikan perhatian khusus dan bimbingan akademik.")
        
    elif result == "Enrolled":
        st.warning("📚 Mahasiswa masih dalam proses studi")
        st.write("Perlu monitoring lanjutan terhadap performa akademik.")
        
    else:
        st.success("🎓 Mahasiswa berpotensi Lulus")
        st.write("Mahasiswa menunjukkan performa akademik yang baik.")

    st.markdown(f"### Status: **{result}**")

    st.divider()

    # ========================
    # PROBABILITY DISPLAY 🔥
    # ========================
    st.subheader("📈 Probabilitas Prediksi")

    prob_df = pd.DataFrame({
        'Status': ['Dropout', 'Enrolled', 'Graduate'],
        'Probabilitas': proba
    })

    st.dataframe(prob_df)

    st.bar_chart(prob_df.set_index('Status'))

    st.markdown('</div>', unsafe_allow_html=True)