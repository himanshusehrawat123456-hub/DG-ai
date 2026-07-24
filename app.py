import os
import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(page_title="मेरा AI चैटबॉट", page_icon="🤖")

st.title("🤖 मेरा AI चैटबॉट")
st.write("नमस्ते! पूछिए आप क्या जानना चाहते हैं।")

# Fetch API key from Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("त्रुटी: Streamlit Secrets में 'GEMINI_API_KEY' नहीं मिली। कृपया इसे सेट करें।")
else:
    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Initialize chat history in session state if not already present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display prior chat messages when app reruns
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("यहाँ अपना सवाल लिखें..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response from Gemini
        with st.chat_message("assistant"):
            with st.status("सोच रहा हूँ...", expanded=False):
                try:
                    # Using gemini-pro for stable API compatibility
                    model = genai.GenerativeModel("gemini-pro")
                    
                    # Format history for Gemini chat if needed, or send direct message
                    chat = model.start_chat(history=[])
                    response = chat.send_message(prompt)
                    bot_response = response.text
                except Exception as e:
                    bot_response = f"त्रुटी (Error): {e}"
            
            st.markdown(bot_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
      
