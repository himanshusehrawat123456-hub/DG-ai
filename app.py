import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="मेरा AI चैटबॉट", page_icon="🤖")
st.title("🤖 मेरा AI चैटबॉट")

# Streamlit Secrets से API Key लें
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("त्रुटी: कृपया Streamlit Secrets में 'GEMINI_API_KEY' जोड़ें।")
else:
    # जेमिनी एपीआई कॉन्फ़िगर करें
    genai.configure(api_key=api_key)
    
    @st.cache_resource
    def load_model():
        return genai.GenerativeModel("gemini-pro")

    try:
        model = load_model()
    except Exception as e:
        st.error(f"मॉडल लोड करने में त्रुटि: {e}")
        model = None

    if model:
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
                        chat = model.start_chat(history=[])
                        response = chat.send_message(prompt)
                        bot_response = response.text
                    except Exception as e:
                        bot_response = f"त्रुटी (Error): {e}"
                
                st.markdown(bot_response)
            
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
          
