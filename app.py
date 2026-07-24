import streamlit as st
from google import genai
from google.genai import types

# पेज की सेटिंग (layout='wide' या 'centered' रख सकते हैं)
st.set_page_config(
    page_title="Professional AI Chatbot", page_icon="✨", layout="centered"
)

# --- प्रीमियम कस्टम CSS (UI & Styling) ---
st.markdown(
    """
    <style>
    /* मुख्य बैकग्राउंड और फॉन्ट */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* हेडर स्टाइल */
    .main-header {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .main-header h1 {
        margin: 0;
        font-size: 28px;
        font-weight: 700;
    }
    .main-header p {
        margin: 5px 0 0 0;
        font-size: 14px;
        opacity: 0.8;
    }

    /* चैट मैसेज का लुक */
    .stChatMessage {
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 10px;
    }
    
    /* साइडबार का लुक सुधारना */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- साइडबार: सारे कंट्रोल्स ---
with st.sidebar:
  st.markdown("### ⚙️ AI सेटिंग्स")

  selected_model = st.selectbox(
      "मॉडल चुनें:",
      [
          "gemini-2.5-flash",
          "gemini-2.0-flash",
          "gemini-1.5-flash",
          "gemini-1.5-pro",
      ],
  )

  temperature = st.slider(
      "क्रिएटिविटी (Temperature):",
      min_value=0.0,
      max_value=1.0,
      value=0.7,
      step=0.1,
  )

  max_output_tokens = st.slider(
      "अधिकतम लंबाई (Max Tokens):",
      min_value=256,
      max_value=8192,
      value=2048,
      step=256,
  )

  system_prompt = st.text_area(
      "सिस्टम प्रॉम्प्ट (AI का स्वभाव):",
      value=(
          "आप शैलेंद्र के एक बेहद मददगार, स्मार्ट और प्रोफेशनल एआई असिस्टेंट हैं।"
          " हर सवाल का जवाब सटीक और बेहतरीन तरीके से दें।"
      ),
      height=100,
  )

  st.markdown("---")

  # चैट डाउनलोड बटन
  if "messages" in st.session_state and st.session_state.messages:
    chat_transcript = ""
    for msg in st.session_state.messages:
      role_label = "यूजर" if msg["role"] == "user" else "एआई"
      chat_transcript += f"{role_label}: {msg['content']}\n\n"

    st.download_button(
        label="📥 चैट डाउनलोड करें (.txt)",
        data=chat_transcript,
        file_name="ai_chat_history.txt",
        mime="text/plain",
    )

  if st.button("🧹 नई चैट शुरू करें (Clear Chat)"):
    st.session_state.messages = []
    st.rerun()

# --- स्टाइलिश हेडर ---
st.markdown(
    """
    <div class="main-header">
        <h1>🚀 Professional AI Assistant</h1>
        <p>Powered by Google Gemini SDK & Streamlit</p>
    </div>
""",
    unsafe_allow_html=True,
)

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
  st.warning(
      "कृपया Streamlit Secrets में अपनी 'GEMINI_API_KEY' सेट करें (Settings ->"
      " Secrets)।"
  )
else:
  client = genai.Client(api_key=api_key)

  if "messages" not in st.session_state:
    st.session_state.messages = []

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  if user_input := st.chat_input("यहाँ अपना मैसेज टाइप करें..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
      st.markdown(user_input)

    with st.chat_message("assistant"):
      with st.spinner("AI सोच रहा है..."):
        models_to_try = [
            selected_model,
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-pro",
        ]
        models_to_try = list(dict.fromkeys(models_to_try))

        response = None
        success = false_flag = False
        last_error = None

        chat_history = []
        for msg in st.session_state.messages[:-1]:
          role_val = "user" if msg["role"] == "user" else "model"
          chat_history.append(
              types.Content(
                  role=role_val, parts=[types.Part.from_text(text=msg["content"])]
              )
          )

        config = types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=temperature,
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
          st.error(f"सभी मॉडल विफल हो गए। अंतिम त्रुटि: {last_error}")
          
