
                
import streamlit as st
from api import configure_gemini, get_gemini_response

st.set_page_config(page_title="मेरा AI चैटबॉट", page_icon="🤖")
st.title("🤖 मेरा AI चैटबॉट")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("त्रुटी: Streamlit Secrets में 'GEMINI_API_KEY' नहीं मिली।")
else:
    model = configure_gemini(api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("यहाँ अपना सवाल लिखें..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.status("सोच रहा हूँ...", expanded=False):
                try:
                    bot_response = get_gemini_response(model, prompt)
                except Exception as e:
                    bot_response = f"त्रुटी (Error): {e}"
            
            st.markdown(bot_response)
        
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
