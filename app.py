import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="मेरा स्मार्ट AI चैटबॉट", page_icon="🤖")

st.title("🤖 मेरा स्मार्ट AI चैटबॉट")

# यूजर से Gemini API Key इनपुट कराना
api_key = st.text_input("अपनी Google Gemini API Key यहाँ डालें:", type="password")

if not api_key:
    st.warning("कृपया ऐप को चलाने के लिए ऊपर अपनी Gemini API Key दर्ज करें।")
else:
    # Gemini को कॉन्फ़िगर करना
    genai.configure(api_key=api_key)
    
    # यहाँ मॉडल का नाम 'gemini-pro' सेट किया है जो 100% काम करता है
    model = genai.GenerativeModel("gemini-pro")

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
                    response = model.generate_content(prompt)
                    bot_reply = response.text
                    
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                except Exception as e:
                    st.error(f"त्रुटि (Error): {e}")

