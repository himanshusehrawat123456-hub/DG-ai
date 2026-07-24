from google import genai
from google.genai import types
import streamlit as st

# पेज की प्रीमियम कॉन्फ़िगरेशन
st.set_page_config(
    page_title="Shailendra AI Studio Advanced", page_icon="✨", layout="wide"
)

# --- प्रीमियम चैटजीपीटी / जेमिनी जैसी मॉडर्न CSS स्टाइलिंग ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #131314;
        color: #e3e3e3;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    .chat-header {
        background: linear-gradient(135deg, #1f1f23 0%, #2d2d35 100%);
        padding: 24px;
        border-radius: 16px;
        text-align: center;
        color: #ffffff;
        margin-bottom: 25px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
        border: 1px solid #3f3f46;
    }
    .chat-header h1 {
        margin: 0;
        font-size: 28px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .chat-header p {
        margin: 8px 0 0 0;
        font-size: 14px;
        color: #9aa0a6;
    }
    [data-testid="stSidebar"] {
        background-color: #1e1f22;
        border-right: 1px solid #3c4043;
    }
    .stChatMessage {
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        border: 1px solid #3c4043;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- साइडबार: एडवांस कंट्रोल हब (सभी फीचर्स और मॉडल्स) ---
with st.sidebar:
  st.markdown("### ⚙️ AI Studio Pro Control Hub")

  # 1. मॉडल सिलेक्शन (सभी वर्तमान और फ्यूचर वर्जन्स)
  selected_model = st.selectbox(
      "मॉडल इंजन चुनें (Model Engine):",
      [
          "gemini-2.0-flash",
          "gemini-1.5-pro",
          "gemini-3.6-flash",
          "gemini-3.5-flash",
          "gemini-3.1-pro-preview",
          "gemini-2.5-flash",
          "gemini-1.5-flash",
      ],
      help="सभी प्रमुख और उन्नत वर्जन्स यहाँ उपलब्ध हैं।",
  )

  st.markdown("---")
  st.markdown("#### 🎛️ क्रिएटिविटी और पैरामीटर्स")

  # 2. टेम्परेचर (Creativity Control)
  temperature = st.slider(
      "क्रिएटिविटी (Temperature):",
      min_value=0.0,
      max_value=1.0,
      value=0.7,
      step=0.05,
      help="0.0 = सटीक और तथ्यपरक; 1.0 = अत्यधिक रचनात्मक।",
  )

  # 3. Top-P (डाइवर्सिटी कंट्रोल)
  top_p = st.slider(
      "Top-P (सैंपलिंग डाइवर्सिटी):",
      min_value=0.0,
      max_value=1.0,
      value=0.95,
      step=0.05,
      help="शब्द चयन की विविधता को नियंत्रित करता है।",
  )

  # 4. Max Tokens (मैक्सिमम रिस्पॉन्स लंबाई)
  max_output_tokens = st.slider(
      "मैक्सिमम टोकन्स (Max Length):",
      min_value=256,
      max_value=8192,
      value=4096,
      step=256,
  )

  st.markdown("---")

  # 5. सिस्टम प्रॉम्प्ट (AI Persona Configuration)
  system_prompt = st.text_area(
      "सिस्टम प्रॉम्प्ट / AI पर्सना:",
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
        label="📥 चैट डाउनलोड करें (.txt)",
        data=chat_transcript,
        file_name="shailendra_ai_workspace_chat.txt",
        mime="text/plain",
        use_container_width=True,
    )

  # 7. नई चैट रीसेट बटन
  if st.button(
      "🧹 नई चैट शुरू करें (Clear History)", use_container_width=True
  ):
    st.session_state.messages = []
    st.rerun()

# --- मुख्य इंटरफ़ेस हेडर ---
st.markdown(
    """
    <div class="chat-header">
        <h1>✨ Shailendra AI Workspace Pro</h1>
        <p>Enterprise-grade Multi-Model AI Assistant powered by Google Gemini SDK</p>
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
  try:
    client = genai.Client(api_key=api_key)

    # चैट सेशन स्टेट इनिशियलाइजेशन
    if "messages" not in st.session_state:
      st.session_state.messages = []

    # चैट हिस्ट्री रेंडर करना
    for message in st.session_state.messages:
      with st.chat_message(message["role"]):
        st.markdown(message["content"])

    # यूजर चैट इनपुट बॉक्स
    if user_input := st.chat_input("अपना सवाल या कोडिंग समस्या यहाँ टाइप करें..."):
      # यूजर मैसेज सेव और डिस्प्ले
      st.session_state.messages.append({"role": "user", "content": user_input})
      with st.chat_message("user"):
        st.markdown(user_input)

      # AI रिस्पॉन्स जनरेशन विथ इंटेलिजेंट ऑटो-फॉलबैक और सारे एडवांस मॉड्यूल्स
      with st.chat_message("assistant"):
        with st.spinner("AI गहन विचार कर रहा है..."):
          models_to_try = [
              selected_model,
              "gemini-2.0-flash",
              "gemini-1.5-pro",
              "gemini-3.6-flash",
              "gemini-3.5-flash",
              "gemini-3.1-pro-preview",
              "gemini-2.5-flash",
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
                    role=role_val,
                    parts=[types.Part.from_text(text=msg["content"])],
                )
            )

          # एडवांस्ड कॉन्फ़िगरेशन (System Instructions, Temperature, Top-P, Tokens)
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

  except Exception as e:
    st.error(f"त्रुटि (Error): {e}")
    
