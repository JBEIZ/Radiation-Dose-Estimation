import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load all models
xray_model = joblib.load('radiation_dose_model.pkl')
ct_model = joblib.load('ct_dose_model.pkl')
mammo_model = joblib.load('mammo_dose_model.pkl')

st.title("📟 AI Radiation Dose Estimator")
st.markdown("Select an imaging modality to estimate radiation dose using an AI model.")

# ------------------------
# Select Modality
# ------------------------
exam_type = st.selectbox("Select Exam Type", ["X-ray", "CT", "Mammogram"])

# ------------------------
# X-RAY
# ------------------------
if exam_type == "X-ray":
    st.subheader("🩻 X-ray Dose Estimation")

    kvp = st.slider("Tube Voltage (kVp)", 60, 120, 80)
    mas = st.slider("Tube Current-Time Product (mAs)", 1, 100, 10)
    time = st.slider("Exposure Time (ms)", 5.0, 100.0, 20.0)
    thickness = st.slider("Patient Thickness (cm)", 10.0, 35.0, 20.0)
    projection = st.selectbox("Projection Type", ["AP", "PA", "LAT"])

    proj_PA = 1 if projection == 'PA' else 0
    proj_LAT = 1 if projection == 'LAT' else 0

    # Ensure correct column order
    xray_input = pd.DataFrame([[
        kvp, mas, time, thickness, proj_PA, proj_LAT
    ]], columns=xray_model.feature_names_in_)

    if st.button("Estimate X-ray Dose"):
        xray_dose = xray_model.predict(xray_input)[0]
        st.success(f"Estimated X-ray Dose (DAP): **{xray_dose:.2f} mGy·cm²**")

# ------------------------
# CT
# ------------------------
elif exam_type == "CT":
    st.subheader("🖥️ CT Dose Estimation")

    ctdi = st.slider("CTDIvol (mGy)", 2.0, 30.0, 10.0)
    scan_length = st.slider("Scan Length (cm)", 10.0, 100.0, 50.0)
    phases = st.selectbox("Number of Phases", [1, 2, 3])

    ct_input = pd.DataFrame([[
        ctdi, scan_length, phases
    ]], columns=ct_model.feature_names_in_)

    if st.button("Estimate CT Dose"):
        dlp = ct_model.predict(ct_input)[0]
        st.success(f"Estimated CT Dose (DLP): **{dlp:.2f} mGy·cm**")

# ------------------------
# Mammogram
# ------------------------
elif exam_type == "Mammogram":
    st.subheader("🎗️ Mammogram Dose Estimation")

    kvp_m = st.slider("Tube Voltage (kVp)", 24.0, 35.0, 28.0)
    mas_m = st.slider("Tube Current-Time Product (mAs)", 10.0, 200.0, 100.0)
    thickness_m = st.slider("Breast Thickness (cm)", 2.0, 8.0, 4.0)
    view = st.selectbox("Mammographic View", ["CC", "MLO"])

    view_MLO = 1 if view == "MLO" else 0  # only 1 dummy variable due to drop_first=True

    mammo_input = pd.DataFrame([[
        kvp_m, mas_m, thickness_m, view_MLO
    ]], columns=mammo_model.feature_names_in_)

    if st.button("Estimate Mammogram Dose"):
        agd = mammo_model.predict(mammo_input)[0]
        st.success(f"Estimated Mammogram Dose (AGD): **{agd:.2f} mGy**")

