import streamlit as st
import google.generativeai as genai

st.title("मेरा AI चैटबॉट 🤖")

# Streamlit secrets से API key लें
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.error("कृपया Streamlit Secrets में GEMINI_API_KEY सेट करें।")

# चैट इतिहास (Chat history) संभालना
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुराने मैसेज दिखाना
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# यूजर से इनपुट लेना
if prompt := st.chat_input("यहाँ अपना सवाल लिखें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini से जवाब मंगाना
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            ai_response = response.text
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
        except Exception as e:
            st.error(f"एरर आ गया: {e}")
  
