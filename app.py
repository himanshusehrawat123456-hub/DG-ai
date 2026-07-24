import streamlit as st
from google import genai
from google.genai import types

# पेज की सेटिंग और लेआउट
st.set_page_config(
    page_title="प्रोफेशनल एआई चैटबॉट", page_icon="🤖", layout="centered"
)

# --- साइडबार: सारे एडवांस कंट्रोल्स और मॉड्यूल्स ---
with st.sidebar:
  st.title("⚙️ AI सेटिंग्स")

  # 1. मॉडल सिलेक्शन
  selected_model = st.selectbox(
      "मॉडल चुनें:",
      [
          "gemini-2.5-flash",
          "gemini-2.0-flash",
          "gemini-1.5-flash",
          "gemini-1.5-pro",
      ],
      help="अपने पसंदीदा जेमिनी मॉडल का चयन करें।",
  )

  # 2. क्रिएटिविटी (Temperature) कंट्रोल
  temperature = st.slider(
      "क्रिएटिविटी (Temperature):",
      min_value=0.0,
      max_value=1.0,
      value=0.7,
      step=0.1,
      help="कम वैल्यू = सटीक/तथ्यपरक जवाब; ज्यादा वैल्यू = रचनात्मक जवाब।",
  )

  # 3. मैक्स टोकन्स (जवाब की अधिकतम लंबाई) कंट्रोल
  max_output_tokens = st.slider(
      "जवाब की अधिकतम लंबाई (Max Tokens):",
      min_value=256,
      max_value=8192,
      value=2048,
      step=256,
      help="एक बार में मिलने वाले जवाब की अधिकतम सीमा।",
  )

  # 4. सिस्टम प्रॉम्प्ट (AI का रोल/स्वभाव)
  system_prompt = st.text_area(
      "सिस्टम प्रॉम्प्ट (AI का स्वभाव):",
      value=(
          "आप शैलेंद्र के एक बेहद मददगार, स्मार्ट और प्रोफेशनल एआई असिस्टेंट हैं।"
          " हर सवाल का जवाब सटीक, साफ, व्यवस्थित और कोडिंग/तकनीकी मामलों में"
          " बेहतरीन तरीके से दें।"
      ),
      height=120,
  )

  st.markdown("---")

  # 5. चैट को डाउनलोड करने का फीचर (Export Chat)
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

  # 6. चैट साफ़ करने का बटन
  if st.button("🧹 नई चैट शुरू करें (Clear Chat)"):
    st.session_state.messages = []
    st.rerun()

# --- मुख्य स्क्रीन ---
st.title("🤖 मेरा प्रोफेशनल AI चैटबॉट")
st.caption(
    "यह ऐप Google Gemini SDK, चैट हिस्ट्री और एडवांस कंट्रोल्स से लैस है।"
)

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
  st.warning(
      "कृपया Streamlit Secrets में अपनी 'GEMINI_API_KEY' सेट करें (Settings ->"
      " Secrets)।"
  )
else:
  client = genai.Client(api_key=api_key)

  # चैट सेशन हिस्ट्री को सुरक्षित रखना
  if "messages" not in st.session_state:
    st.session_state.messages = []

  # पुरानी सारी बातचीत को स्क्रीन पर रेंडर करना
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # यूजर का इनपुट चैट बॉक्स
  if user_input := st.chat_input("यहाँ अपना मैसेज टाइप करें..."):
    # यूजर के मैसेज को जोड़ें और स्क्रीन पर दिखाएं
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
      st.markdown(user_input)

    # AI का रिस्पॉन्स जनरेट करना (फॉलबैक और पूरी चैट हिस्ट्री के साथ)
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
        success = False
        last_error = None

        # जेमिनी के इतिहास (History) के अनुसार पुराने मैसेज तैयार करना
        chat_history = []
        for msg in st.session_state.messages[:-1]:
          role_val = "user" if msg["role"] == "user" else "model"
          chat_history.append(
              types.Content(
                  role=role_val, parts=[types.Part.from_text(text=msg["content"])]
              )
          )

        # एडवांस कॉन्फ़िगरेशन (System Instructions, Temperature, Max Tokens)
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
          # असिस्टेंट के जवाब को भी हिस्ट्री में सुरक्षित करना
          st.session_state.messages.append(
              {"role": "assistant", "content": bot_reply}
          )
        else:
          st.error(f"सभी मॉडल विफल हो गए। अंतिम त्रुटि: {last_error}")
          
