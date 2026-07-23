import streamlit as st
from google import genai

st.set_page_config(page_title="मेरा स्मार्ट AI चैटबॉट", page_icon="🤖")
st.title("🤖 मेरा स्मार्ट AI चैटबॉट")

api_key = st.text_input("अपनी Google Gemini API Key यहाँ डालें:", type="password")

if not api_key:
    st.warning("कृपया ऐप को चलाने के लिए ऊपर अपनी Gemini API Key दर्ज करें।")
else:
    try:
        client = genai.Client(api_key=api_key)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("अपना सवाल यहाँ पूछें..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("AI सोच रहा है..."):
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                    )
                    bot_reply = response.text
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                    
    except Exception as e:
        st.error(f"त्रुटि (Error): {e}")

