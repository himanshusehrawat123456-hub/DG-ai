import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="मेरा AI चैटबॉट", page_icon="🤖")

st.title("मेरा AI चैटबॉट 🤖")

# Configure Gemini API using Streamlit Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Gemini API Key not found in Streamlit Secrets!")

# Initialize the Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize chat history in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages from history when app reruns
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input via chat input box
if prompt := st.chat_input("यहाँ अपना सवाल लिखें..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from Gemini AI
    with st.chat_message("assistant"):
        with st.spinner("सोच रहा हूँ..."):
            try:
                response = model.generate_content(prompt)
                ai_response = response.text
                st.markdown(ai_response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            except Exception as e:
                st.error(f"त्रुटि (Error): {e}")
              
