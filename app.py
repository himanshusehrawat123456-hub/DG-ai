from groq import Groq
import streamlit as st

# पेज की सेटिंग
st.set_page_config(
    page_title="Omni-App AI Command Center", page_icon="⚡", layout="wide"
)

st.title("⚡ Omni-App AI Command Center (Groq Engine)")
st.markdown(
    "Welcome to your high-speed multi-engine command hub, powered by Groq"
    " LPU."
)

# Groq क्लाइंट सेट अप करना (Secrets या डायरेक्ट की से)
try:
  # अगर secrets.toml में है तो वहाँ से उठाएगा, वरना आपकी दी गई की इस्तेमाल होगी
  api_key = (
      st.secrets["GROQ_API_KEY"]
      if "GROQ_API_KEY" in st.secrets
      else "Gsk_TSydW5PzuEqLizkJl6esWGdyb3FYwZREZ3sOBY8Wko27lnRG5DF5"
  )
  client = Groq(api_key=api_key)
except Exception as e:
  st.error(f"API Key initialization error: {e}")
  client = None

# मॉडल सिलेक्शन का हब
model_choice = st.selectbox(
    "Select AI Engine",
    ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"],
)

# यूजर इनपुट कमांड
user_prompt = st.text_input(
    "Command your Omni-App (e.g., 'Generate logistics report...')"
)

if st.button("Execute Command") and client:
  if user_prompt:
    with st.spinner("Processing command at ultra-high speed..."):
      try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an advanced Omni-App AI Command Center assistant"
                        " managing logistics, automation, and multi-modal tasks."
                    ),
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            model=model_choice,
        )

        st.success("Execution Successful:")
        st.write(chat_completion.choices[0].message.content)

      except Exception as e:
        st.error(
            f"An error occurred while communicating with Groq API: {e}"
        )
  else:
    st.warning("Please enter a command to execute.")
    
