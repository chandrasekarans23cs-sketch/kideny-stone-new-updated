# pages/2_Result_Page.py
import streamlit as st
import numpy as np
import joblib

st.title("📊 Prediction Results")

if "input_data" not in st.session_state:
    st.error("⚠️ No input found! Go to the Input Page first.")
    st.stop()

gravity, ph, osmo, cond, urea, calc = st.session_state["input_data"]
input_array = np.array([[gravity, ph, osmo, cond, urea, calc]])

# Load models
rf_model = joblib.load("rf_model.pkl")
svm_model = joblib.load("svm_model.pkl")
scaler = joblib.load("scaler.pkl")

# Scale input
scaled_input = scaler.transform(input_array)

# Predictions
rf_pred = rf_model.predict(scaled_input)[0]
svm_pred = svm_model.predict(scaled_input)[0]

rf_result = "High Risk" if rf_pred == 1 else "Low Risk"
svm_result = "High Risk" if svm_pred == 1 else "Low Risk"

st.subheader("🔍 Results from Machine Learning Models")

st.write(f"### 🌳 Random Forest Prediction: **{rf_result}**")
st.write(f"### ⚙️ SVM Prediction: **{svm_result}**")

# Final combined decision
if rf_pred + svm_pred >= 1:
    final = "🔴 FINAL: High Risk of Kidney Stone"
else:
    final = "🟢 FINAL: Low Risk of Kidney Stone"

st.markdown(f"## {final}")
