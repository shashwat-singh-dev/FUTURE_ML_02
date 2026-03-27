import streamlit as st
import requests

API_URL = "https://nlp-ticket-classifier.onrender.com/predict"

st.title("🎫 Ticket Classifier")

text = st.text_input("Enter your issue:")

if st.button("Predict"):
    if text:
        try:
            response = requests.post(
                API_URL,
                json={"text": text},
                timeout=60
            )

            response.raise_for_status()
            data = response.json()

            st.success(f"Category: {data['category']}")
            st.info(f"Priority: {data['priority']}")

        except Exception as e:
            st.error(f"Error: {e}")
