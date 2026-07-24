import streamlit as st
from google import genai

st.set_page_config(
    page_title="मेरा AI चैटबॉट", page_icon="🤖", layout="centered"
)

st.title("🤖 मेरा जेमिनी चैटबॉट")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
  st.warning(
      "कृपया Streamlit Secrets में अपनी 'GEMINI_API_KEY' सेट करें (Settings ->"
      " Secrets)।"
  )
else:
  try:
    client = genai.Client(api_key=api_key)

    user_input = st.text_input("अपना सवाल यहाँ पूछें:")

    if user_input:
      with st.spinner("सोच रहा हूँ..."):
        # सभी संभावित और लेटेस्ट मॉडल्स की पूरी सूची
        models_to_try = [
            "gemini-3.5-flash",
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-pro",
        ]

        response = None
        success = False
        last_error = None

        for model_name in models_to_try:
          try:
            response = client.models.generate_content(
                model=model_name, contents=user_input
            )
            success = True
            break
          except Exception as err:
            last_error = err
            continue

        if success and response:
          st.write("### उत्तर:")
          st.write(response.text)
        else:
          st.error(f"सभी मॉडल विफल हो गए। अंतिम त्रुटि: {last_error}")

  except Exception as e:
    st.error(f"त्रुटि (Error): {e}")
    
