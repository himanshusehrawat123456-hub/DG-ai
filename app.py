import streamlit as st
import requests

st.title("मेरा स्मार्ट AI चैटबॉट 🤖")

# Hugging Face API सेटिंग्स (यहाँ आप अपना HF टोकन डाल सकते हैं)
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

# अगर आपके पास Hugging Face का टोकन है, तो यहाँ डालें या Streamlit secrets से लें
# सुरक्षा के लिए आप इसे सीधे यहाँ लिख सकते हैं या st.secrets का इस्तेमाल कर सकते हैं
HF_TOKEN = st.text_input("अपना Hugging Face Token (API Key) यहाँ डालें:", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("अब अपना असली सवाल पूछें..."):
    if not HF_TOKEN:
        st.warning("कृपया पहले ऊपर दिए गए बॉक्स में अपना Hugging Face Token दर्ज करें!")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Hugging Face API को रिक्वेस्ट भेजना
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        payload = {"inputs": prompt}

        with st.chat_message("assistant"):
            with st.spinner("सोच रहा हूँ..."):
                try:
                    response = requests.post(API_URL, headers=headers, json=payload)
                    result = response.json()
                    
                    if isinstance(result, list) and len(result) > 0:
                        bot_reply = result[0].get("generated_text", "क्षमा करें, मैं समझ नहीं पाया।")
                        # कभी-कभी मॉडल पूरा प्रॉम्प्ट भी साथ में लौटा देता है, उसे साफ़ कर सकते हैं
                        if bot_reply.startswith(prompt):
                            bot_reply = bot_reply[len(prompt):].strip()
                    elif isinstance(result, dict) and "error" in result:
                        bot_reply = f"एरर: {result['error']}"
                    else:
                        bot_reply = "सर्वर से सही जवाब नहीं मिला।"
                    
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                except Exception as e:
                    st.error(f"कनेक्शन में दिक्कत आई: {e}")
                    
        
  
