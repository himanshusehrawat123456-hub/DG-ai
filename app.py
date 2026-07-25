import os
import streamlit as st
from groq import Groq

# पेज कॉन्फ़िगरेशन
st.set_page_config(
    page_title="Omni-App AI Command Center",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded"
)

# कस्टम स्टाइलिंग (प्रोफेशनल लुक के लिए)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0rem; }
    .subtitle { font-size: 1rem; color: #64748B; margin-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">Omni-App AI Command Center</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enterprise-grade command hub, powered by Groq LPU.</p>', unsafe_allow_html=True)

# सुरक्षित तरीके से API Key लोड करना (Secrets प्राथमिकता, फिर Environment Variables)
def get_groq_api_key():
    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass
    return os.environ.get("GROQ_API_KEY", "")

api_key = get_groq_api_key()

# साइडबार कॉन्फ़िगरेशन
with st.sidebar:
    st.header("⚙️ Configuration")
    ai_engine = st.selectbox(
        "Select AI Engine",
        ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"],
        help="चुनें कि आप कौन सा AI मॉडल इस्तेमाल करना चाहते हैं।"
    )
    
    st.markdown("---")
    st.markdown("### 🔒 Security Status")
    if api_key:
        st.success("API Key Loaded Securely")
    else:
        st.error("API Key Missing!")

# मुख्य इंटरफेस
user_command = st.text_area(
    "Command your Omni-App",
    placeholder="Enter your instructions or query here (e.g., 'Generate logistics report...')...",
    height=120
)

col1, col2 = st.columns([1, 4])
with col1:
    execute_btn = st.button("Execute", type="primary", use_container_width=True)

# चैट हिस्ट्री बनाए रखने के लिए सेशन स्टेट
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if execute_btn:
    if not api_key:
        st.error("Groq API Key कॉन्फ़िगर नहीं है। कृपया Streamlit Secrets में `GROQ_API_KEY` सेट करें।")
    elif not user_command.strip():
        st.warning("कृपया पहले कोई कमांड दर्ज करें।")
    else:
        with st.spinner("Processing your command via Groq LPU..."):
            try:
                # Groq क्लाइंट इनिशियलाइज करना
                client = Groq(api_key=api_key)
                
                # API कॉल
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": user_command,
                        }
                    ],
                    model=ai_engine,
                    temperature=0.7,
                )
                
                response_text = chat_completion.choices[0].message.content
                
                # इतिहास में जोड़ना
                st.session_state.chat_history.insert(0, {"command": user_command, "response": response_text})
                
            except Exception as e:
                st.error(f"Groq API komunikation mein truti aayi: {e}")

# आउटपुट / इतिहास दिखाना
if st.session_state.chat_history:
    st.markdown("### 📊 Execution Results")
    for idx, item in enumerate(st.session_state.chat_history):
        with st.container():
            st.markdown(f"**Command:** {item['command']}")
            st.info(item['response'])
            st.markdown("---")
          
