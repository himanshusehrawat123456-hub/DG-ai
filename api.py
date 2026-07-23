import streamlit as st

# ऐप का टाइटल
st.title("मेरा AI चैटबॉट 🤖")

# चैट की हिस्ट्री (history) को सेव रखने के लिए
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुरानी चैट को स्क्रीन पर दिखाना
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# यूजर से इनपुट लेना (नीचे चैट बॉक्स)
if prompt := st.chat_input("यहाँ अपना सवाल लिखें..."):
    # यूजर का मैसेज जोड़ें और दिखाएं
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # बॉट का जवाब (आप यहाँ अपनी AI मॉडल या API का इस्तेमाल कर सकते हैं)
    response = f"आपने कहा: {prompt}"
    
    # बॉट का जवाब जोड़ें और दिखाएं
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
        
