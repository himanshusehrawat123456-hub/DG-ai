import streamlit as st
import requests

st.set_page_config(page_title="मेरा स्मार्ट AI चैटबॉट", page_icon="🤖")

st.title("🤖 मेरा स्मार्ट AI चैटबॉट")

# यूजर से Gemini API Key इनपुट कराना
api_key = st.text_input("अपनी Google Gemini API Key यहाँ डालें:", type="password")

if not api_key:
    st.warning("कृपया ऐप को चलाने के लिए ऊपर अपनी Gemini API Key दर्ज करें।")
else:
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

        # AI से जवाब मंगाना (gemini-pro मॉडल के साथ)
        with st.chat_message("assistant"):
            with st.spinner("AI सोच रहा है..."):
                try:
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
                    headers = {"Content-Type": "application/json"}
                    data = {
                        "contents": [{
                            "parts": [{"text": prompt}]
                        }]
                    }
                    
                    response = requests.post(url, json=data, headers=headers)
                    result = response.json()
                    
                    if response.status_code == 200:
                        bot_reply = result["candidates"][0]["content"]["parts"][0]["text"]
                        st.markdown(bot_reply)
                        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                    else:
                        error_message = result.get("error", {}).get("message", "अज्ञात त्रुटि")
                        st.error(f"API त्रुटि: {error_message}")
                except Exception as e:
                    st.error(f"त्रुटि (Error): {e}")
                  
