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
    client = genai.Client(api_key=api_key)

    user_input = st.text_input("अपना सवाल यहाँ पूछें:")

    if user_input:
      with st.spinner("सोच रहा हूँ..."):
        selected_model = None

        # आपके अकाउंट के लिए जो मॉडल उपलब्ध होगा, यह कोड उसे अपने आप ढूंढ लेगा
        try:
          for m in client.models.list():
            if "generateContent" in m.supported_generation_methods:
              # किसी भी एक सही फ्लैश या प्रो मॉडल का चयन कर लें
              if "flash" in m.name or "pro" in m.name:
                selected_model = m.name
                break
        except Exception:
          pass

        # यदि आटोमेटिक फेच न हो तो पहले से मौजूद सुरक्षित विकल्पों का उपयोग करें
        models_to_try = (
            [selected_model]
            if selected_model
            else []
            + [
                "gemini-2.5-flash",
                "gemini-2.0-flash",
                "gemini-1.5-flash",
                "gemini-1.5-pro",
                "gemini-pro",
            ]
        )

        response = None
        success = False
        last_error = None

        for model_name in models_to_try:
          if not model_name:
            continue
          try:
            # यदि मॉडल के नाम में 'models/' पहले से नहीं है तो जोड़ लें
            full_model_name = (
                model_name
                if model_name.startswith("models/")
                else f"models/{model_name}"
            )
            response = client.models.generate_content(
                model=full_model_name, contents=user_input
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
      
    
