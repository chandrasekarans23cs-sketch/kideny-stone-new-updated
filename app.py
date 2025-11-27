# app.py
import streamlit as st

st.set_page_config(page_title="Kidney Stone Predictor", page_icon="🧠")

st.title("🧠 Kidney Stone Prediction System")
st.write("### Developed by CHANDRASEKARAN S & Team")

st.markdown("""
Welcome to the **Kidney Stone Prediction Web Application**.

This mini-project uses **Machine Learning Algorithms** to predict the
risk of kidney stone formation based on urine test parameters.

### ✔️ Pages Included:
1. **Entry Page** — You are here  
2. **Input Page** — Enter urine sample values  
3. **Result Page** — Get ML prediction output  

Use the sidebar to navigate!
""")
