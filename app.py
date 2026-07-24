import streamlit as st
from google import genai
from google.genai import types

# पेज की सेटिंग
st.set_page_config(
    page_title="Professional AI Chatbot Studio", page_icon="⚡", layout="centered"
)

# --- प्रीमियम कस्टम CSS (Ultimate UI & Styling) ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main-header {
        background: linear-gradient(135deg, #1f4068 0%, #162447 100%);
        padding: 22px;
        border-radius: 14px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        border: 1px solid #1f4068;
    }
    .main-header h1 {
        margin: 0;
        font-size: 30px;
        font-weight: 800;
        letter-spacing: 0.5px;
    }
    .main-header p {
        margin: 6px 0 0 0;
        font-size: 14px;
        opacity: 0.85;
    }
    .stChatMessage {
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 12px;
    }
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- साइडबार: अल्टीमेट एडवांस कंट्रोल्स (ChatGPT & Gemini Pro Suite) ---
with st.sidebar:
  st.markdown("### ⚙️ AI Studio Control Hub")

  # 1. मॉडल सिलेक्शन (Pro & Flash)
  selected_model = st.selectbox(
      "मॉडल चुनें (Model Engine):",
      [
          "gemini-2.5-flash",
          "gemini-1.5-pro",
          "gemini-2.0-flash",
          "gemini-1.5-flash",
      ],
      help=(
          "Pro मॉडल गहरी कोडिंग/रीज़निंग के लिए और Flash सुपर-फास्ट रिस्पॉन्स के"
          " लिए है।"
      ),
  )

  st.markdown("---")
  st.markdown("#### 🎛️ क्रिएटिविटी और पैरामीटर्स")

  # 2. टेम्परेचर (Creativity)
  temperature = st.slider(
      "क्रिएटिविटी (Temperature):",
      min_value=0.0,
      max_value=1.0,
      value=0.7,
      step=0.05,
      help="0.0 = अत्यंत सटीक और तार्किक; 1.0 = अत्यधिक रचनात्मक और अनोखा।",
  )

  # 3. Top-P (Nucleus Sampling) - एडवांस्ड डाइवर्सिटी कंट्रोल
  top_p = st.slider(
      "Top-P (सैंपलिंग डाइवर्सिटी):",
      min_value=0.0,
      max_value=1.0,
      value=0.95,
      step=0.05,
      help="शब्दों के चयन की विविधता को नियंत्रित करता है।",
  )

  # 4. Max Tokens (जवाब की लंबाई)
  max_output_tokens = st.slider(
      "अधिकतम लंबाई (Max Tokens):",
      min_value=256,
      max_value=8192,
      value=4096,
      step=256,
  )

  st.markdown("---")

  # 5. सिस्टम प्रॉम्प्ट (AI का स्वभाव और Persona)
  system_prompt = st.text_area(
      "सिस्टम प्रॉम्प्ट (AI Persona):",
      value=(
          "आप शैलेंद्र के एक बेहद मददगार, उन्नत, कोडिंग एक्सपर्ट और प्रोफेशनल एआई"
          " असिस्टेंट हैं। हर सवाल का जवाब तकनीकी गहराई, साफ-सुथरे कोड उदाहरणों और"
          " सटीक तर्कों के साथ दें।"
      ),
      height=120,
  )

  st.markdown("---")

  # 6. चैट एक्सपोर्ट और डाउनलोड (TXT)
  if "messages" in st.session_state and st.session_state.messages:
    st.markdown("#### 💾 सेशन मैनेजमेंट")
    chat_transcript = ""
    for msg in st.session_state.messages:
      role_label = "User" if msg["role"] == "user" else "AI Assistant"
      chat_transcript += f"{role_label}: {msg['content']}\n\n"

    st.download_button(
        label="📥 पूरी चैट डाउनलोड करें (.txt)",
        data=chat_transcript,
        file_name="shailendra_ai_chat_history.txt",
        mime="text/plain",
    )

  # 7. नई चैट रीसेट बटन
  if st.button("🧹 नई चैट शुरू करें (Clear Session)", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

# --- स्टाइलिश हेडर ---
st.markdown(
    """
    <div class="main-header">
        <h1>⚡ Shailendra AI Studio Pro</h1>
        <p>Enterprise-grade Multi-Model AI Assistant powered by Google Gemini SDK & Streamlit</p>
    </div>
""",
    unsafe_allow_html=True,
)

# API Key वेरिफिकेशन
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
  st.warning(
      "⚠️ कृपया Streamlit Secrets में अपनी 'GEMINI_API_KEY' सेट करें (Settings"
      " -> Secrets)।"
  )
else:
  client = genai.Client(api_key=api_key)

  # सेशन स्टेट इनिशियलाइजेशन
  if "messages" not in st.session_state:
    st.session_state.messages = []

  # संदेशों को स्क्रीन पर रेंडर करना
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # यूजर का इनपुट चैट बॉक्स
  if user_input := st.chat_input("अपना मैसेज या कोडिंग सवाल यहाँ पूछें..."):
    # यूजर मैसेज सेव और डिस्प्ले
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
      st.markdown(user_input)

    # AI रिस्पॉन्स जनरेशन विथ एडवांस्ड फॉलबैक
    with st.chat_message("assistant"):
      with st.spinner("AI गहन विचार कर रहा है..."):
        models_to_try = [
            selected_model,
            "gemini-2.5-flash",
            "gemini-1.5-pro",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
        ]
        models_to_try = list(dict.fromkeys(models_to_try))

        response = None
        success = False
        last_error = None

        # चैट हिस्ट्री मैपिंग (Gemini SDK Content format)
        chat_history = []
        for msg in st.session_state.messages[:-1]:
          role_val = "user" if msg["role"] == "user" else "model"
          chat_history.append(
              types.Content(
                  role=role_val, parts=[types.Part.from_text(text=msg["content"])]
              )
          )

        # एडवांस्ड कॉन्फ़िगरेशन (Temperature, Top-P, System Instructions, Max Tokens)
        config = types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=temperature,
            top_p=top_p,
            max_output_tokens=max_output_tokens,
        )

        for model_name in models_to_try:
          try:
            chat = client.chats.create(
                model=model_name, history=chat_history, config=config
            )
            response = chat.send_message(user_input)
            success = True
            break
          except Exception as err:
            last_error = err
            continue

        if success and response:
          bot_reply = response.text
          st.markdown(bot_reply)
          st.session_state.messages.append(
              {"role": "assistant", "content": bot_reply}
          )
        else:
          st.error(
              f"सभी मॉडल्स कनेक्ट होने में विफल रहे। त्रुटि: {last_error}"
          )
          
