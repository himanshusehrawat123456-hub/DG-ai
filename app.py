import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="मेरा स्मार्ट AI चैटबॉट", page_icon="🤖")

st.title("🤖 मेरा स्मार्ट AI चैटबॉट")

# यूजर से Gemini API Key इनपुट कराना
api_key = st.text_input("अपनी Google Gemini API Key यहाँ डालें:", type="password")

if not api_key:
    st.warning("कृपया ऐप को चलाने के लिए ऊपर अपनी Gemini API Key दर्ज करें। (आप इसे Google AI Studio से मुफ़्त ले सकते हैं)")
else:
    # Gemini को कॉन्फ़िगर करना
    genai.configure(api_key=api_key)
    
    # मॉडल सेट करना (सबसे बेहतरीन और फ्री gemini-1.5-flash मॉडल)
    model = genai.GenerativeModel("gemini-1.5-flash")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # पुरानी चैट दिखाना
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # यूजर का नया सवाल
    if prompt := st.chat_input("अपना सवाल यहाँ पूछें..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI से जवाब मंगाना
        with st.chat_message("assistant"):
            with st.spinner("AI सोच रहा है..."):
                try:
                    # पुरानी चैट हिस्ट्री को साथ भेजना ताकि बातचीत सही से हो सके
                    chat_history = [
                        {"role": m["role"] if m["role"] == "user" else "model", "parts": [m["content"]]}
                        for m in st.session_state.messages[:-1]
                    ]
                    
                    chat = model.start_chat(history=chat_history)
                    response = chat.send_message(prompt)
                    
                    bot_reply = response.text
                    st.markdown(bot_reply)
                    
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                except Exception as e:
                    st.error(f"त्रुटि (Error): {e}")
                    
