import streamlit as st
from google import genai

st.set_page_config(
    page_title="प्रोफेशनल जेमिनी चैटबॉट", page_icon="🤖", layout="centered"
)

# साइडबार सेटिंग्स और मॉडल लिस्ट
with st.sidebar:
  st.title("⚙️ सेटिंग्स")
  selected_model = st.selectbox(
      "मॉडल चुनें:",
      [
          "gemini-3.5-flash",
          "gemini-2.5-flash",
          "gemini-2.0-flash",
          "gemini-1.5-flash",
          "gemini-1.5-pro",
      ],
  )
  if st.button("🧹 चैट साफ़ करें"):
    st.session_state.messages = []
    st.rerun()

st.title("🤖 मेरा प्रोफेशनल जेमिनी चैटबॉट")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
  st.warning(
      "कृपया Streamlit Secrets में अपनी 'GEMINI_API_KEY' सेट करें (Settings ->"
      " Secrets)।"
  )
else:
  client = genai.Client(api_key=api_key)

  # चैट हिस्ट्री इनिशियलाइज करें
  if "messages" not in st.session_state:
    st.session_state.messages = []

  # पुरानी बातचीत को स्क्रीन पर रेंडर करें
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # यूजर का इनपुट चैट बॉक्स के जरिए लें
  if user_input := st.chat_input("अपना सवाल यहाँ पूछें..."):
    # यूजर का मैसेज सेव करें और दिखाएं
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
      st.markdown(user_input)

    # जेमिनी से रिस्पॉन्स मँगवाएं (फॉलबैक लूप के साथ ताकि कोई भी मॉडल मिस न हो)
    with st.chat_message("assistant"):
      with st.spinner("सोच रहा हूँ..."):
        models_to_try = [
            selected_model,
            "gemini-3.5-flash",
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-pro",
        ]

        response = None
        success = False
        last_error = None

        # डुप्लीकेट मॉडल्स हटाने के लिए
        models_to_try = list(dict.fromkeys(models_to_try))

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
          bot_reply = response.text
          st.markdown(bot_reply)
          # असिस्टेंट का जवाब हिस्ट्री में सेव करें
          st.session_state.messages.append(
              {"role": "assistant", "content": bot_reply}
          )
        else:
          st.error(f"सभी मॉडल विफल हो गए। अंतिम त्रुटि: {last_error}")
          
