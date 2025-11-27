# pages/1_Input_Page.py
import streamlit as st
import numpy as np
import joblib

st.title("🔧 Input Parameters")

st.write("Enter the patient's urine test values below:")

gravity = st.slider("Urine Specific Gravity", 1.005, 1.035, step=0.001)
ph = st.slider("Urine pH", 4.5, 8.0, step=0.1)
osmo = st.slider("Osmolality", 100, 1300)
cond = st.slider("Conductivity", 5.0, 40.0)
urea = st.slider("Urea (mg/dL)", 10, 650)
calc = st.slider("Calcium (mg/dL)", 0.1, 15.0)

# Save user input in session
if st.button("Submit"):
    st.session_state["input_data"] = [gravity, ph, osmo, cond, urea, calc]
    st.success("Input Saved! Go to the Result Page →")
