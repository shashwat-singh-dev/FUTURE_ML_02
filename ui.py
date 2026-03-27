import streamlit as st
import requests

API_URL = "https://nlp-ticket-classifier.onrender.com/predict"

st.title("🎫 Ticket Classifier")

def clear_text():
    st.session_state.text = ""
def set_sample(sample):
    st.session_state.text = sample

if "text" not in st.session_state:
    st.session_state.text = ""

text = st.text_input("Enter your issue:", key="text")
st.markdown("### 💡 Try sample issues:")

samples = [
"Payment issue"
"App crash"
"Reset password"
"Account hacked"
"Slow app"
]

cols = st.columns(len(samples))

for i, sample in enumerate(samples):
    cols[i].button(
        sample,
        on_click=set_sample,
        args=(sample,)
    )

st.button("Clear", on_click=clear_text)

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

            except Exception as e:
                st.error(f"Error: {e}")
