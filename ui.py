import streamlit as st
import requests

API_URL = "https://nlp-ticket-classifier.onrender.com/predict"

st.title("🎫 Ticket Classifier")

text = st.text_input("Enter your issue:")

if st.button("Clear"):
    st.rerun()

if st.button("Predict"):

    if not text.strip():
        st.warning("Please enter an issue first")

    else:
        with st.spinner("Processing..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"text": text},
                    timeout=60
                )

                response.raise_for_status()
                data = response.json()

                st.markdown("### 🎯 Prediction Result")

                col1, col2 = st.columns(2)

                with col1:
                st.success(f"📂 Category\n\n**{data['category']}**")

                with col2:
                st.info(f"⚡ Priority\n\n**{data['priority']}**")
