# streamlit_app.py

import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load('radiation_dose_model.pkl')

# Title
st.title("🩻 AI Radiation Dose Estimator")

st.markdown("Estimate the radiation dose (DAP in mGy·cm²) from X-ray parameters using AI.")

# Input sliders
kvp = st.slider("Tube Voltage (kVp)", 60, 120, 80)
mas = st.slider("Tube Current-Time Product (mAs)", 1, 100, 10)
time = st.slider("Exposure Time (ms)", 5.0, 100.0, 20.0)
thickness = st.slider("Patient Thickness (cm)", 10.0, 35.0, 20.0)
projection = st.selectbox("Projection Type", ['AP', 'PA', 'LAT'])

# Encode projection type
proj_PA = 1 if projection == 'PA' else 0
proj_LAT = 1 if projection == 'LAT' else 0

# Input data
input_data = pd.DataFrame([[
    kvp, mas, time, thickness, proj_PA, proj_LAT
]], columns=['kVp', 'mAs', 'ExposureTime', 'Thickness', 'Projection_PA', 'Projection_LAT'])

# Predict button
if st.button("Estimate Dose"):
    dose_prediction = model.predict(input_data)[0]
    st.success(f"📟 Estimated Radiation Dose: **{dose_prediction:.2f} mGy·cm²**")
