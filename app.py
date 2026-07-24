import streamlit as st
from google import genai

st.set_page_config(
    page_title="मेरा AI चैटबॉट", page_icon="🤖", layout="centered"
)

st.title("🤖 मेरा जेमिनी चैटबॉट")

# Streamlit secrets से API Key लेना
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
  st.warning(
      "कृपया Streamlit Secrets में अपनी 'GEMINI_API_KEY' सेट करें (Settings ->"
      " Secrets)।"
  )
else:
  try:
    # genai क्लाइंट इनिशियलाइज करें
    client = genai.Client(api_key=api_key)

    # यूजर का इनपुट लें
    user_input = st.text_input("अपना सवाल यहाँ पूछें:")

    if user_input:
      with st.spinner("सोच रहा हूँ..."):
        # यहाँ मॉडल का नाम बदलकर gemini-1.5-flash कर दिया गया है
        response = client.models.generate_content(
            model="gemini-1.5-flash", contents=user_input
        )
        st.write("### उत्तर:")
        st.write(response.text)

  except Exception as e:
    st.error(f"त्रुटि (Error): {e}")
    
