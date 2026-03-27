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

st.caption("Enter your issue or try a sample below 👇")

# INPUT
text = st.text_input("Enter your issue:", key="text")

st.markdown("### 💡 Try sample issues:")

samples = [
    "Payment issue",
    "App crash",
    "Reset password",
    "Account hacked",
    "Slow app"
]

cols = st.columns(5)

for i, sample in enumerate(samples):
    with cols[i]:
        st.button(
            sample,
            on_click=set_sample,
            args=(sample,),
            use_container_width=True
        )
# --------------------------
# BUTTONS
# --------------------------
st.markdown("")

col1, col2 = st.columns([1,1])

with col1:
    st.button("Clear", on_click=clear_text)

with col2:
    predict = st.button("Predict")

# --------------------------
# RESULT
# --------------------------
if predict:
    if not st.session_state.text.strip():
        st.warning("Please enter an issue first")
    else:
        with st.spinner("Analyzing your issue..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"text": st.session_state.text},
                    timeout=60
                )

                data = response.json()

                st.divider()
                st.markdown("### 🎯 Prediction Result")

                col1, col2 = st.columns(2)

                with col1:
                    st.success(f"📂 Category\n\n**{data['category']}**")

                with col2:
                    st.info(f"⚡ Priority\n\n**{data['priority']}**")

            except Exception as e:
                st.error(f"Error: {e}")
