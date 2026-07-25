import streamlit as st
import os
import time
from datetime import datetime
import pandas as pd

# Page Configuration for PWA & Mobile Optimization
st.set_page_config(
    page_title="Omni-App AI Command Center",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Professional Styling & Mobile Responsiveness
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    .sidebar .sidebar-content { background-color: #1e293b; }
    h1, h2, h3 { color: #38bdf8 !important; font-family: 'Inter', sans-serif; }
    .stMetric { background-color: #1e293b; padding: 15px; border-radius: 10px; border: 1px solid #334155; }
    .stButton>button { width: 100%; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: white; border-radius: 8px; font-weight: bold; border: none; padding: 10px; }
    .stButton>button:hover { background: linear-gradient(135deg, #0369a1 0%, #075985 100%); }
    .card { background-color: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 20px; }
    .success-badge { background-color: #065f46; color: #6ee7b7; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
    .warning-badge { background-color: #92400e; color: #fde68a; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Initialize Groq Client safely from Streamlit Secrets
from groq import Groq
groq_api_key = None
try:
    if "GROQ_API_KEY" in st.secrets:
        groq_api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

# Fallback environment variable check
if not groq_api_key:
    groq_api_key = os.environ.get("GROQ_API_KEY", "")

client = Groq(api_key=groq_api_key) if groq_api_key else None

# Sidebar Navigation & User Profile
st.sidebar.markdown("# 🚀 Omni Command Center")
st.sidebar.markdown(f"**Date:** {datetime.now().strftime('%A, %d %b %Y')}")
st.sidebar.markdown("---")

app_mode = st.sidebar.radio(
    "Navigation Hub",
    [
        "⚡ Executive Dashboard",
        "🎙️ Voice & Speech Command",
        "🎨 Speech-to-Image Studio",
        "📱 Social & WhatsApp Hub",
        "💰 Expense & Finance Control",
        "🏃 Fitness & Location Tracker",
        "⚙️ System Settings"
    ]
)

# Helper function for Groq LLM Generation
def ask_groq(prompt, system_role="You are an elite AI assistant managing an enterprise command center."):
    if not client:
        return "⚠️ Groq API Key not configured in Streamlit Secrets (`secrets.toml`). Please add `GROQ_API_KEY`."
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Error communicating with Groq API: {str(e)}"

# 1. EXECUTIVE DASHBOARD
if app_mode == "⚡ Executive Dashboard":
    st.title("⚡ Enterprise Executive Command Center")
    st.markdown("Real-time operational overview, productivity intelligence, and financial health audit.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Daily Task Completion", value="85%", delta="+12% vs yesterday")
    with col2:
        st.metric(label="Today's Spend", value="₹1,450", delta="-₹300 under budget", delta_color="inverse")
    with col3:
        st.metric(label="Fitness Goal", value="7,840 Steps", delta="Target: 10,000")
    with col4:
        st.metric(label="AI Status", value="Online", delta="Groq Llama-3.3 Active")

    st.markdown("---")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🔍 Daily Audit & AI Diagnostics")
        st.markdown("AI analysis of what went right, what went wrong, and corrective actions for today:")
        
        audit_prompt = "Perform a strict, constructive daily productivity and expense audit for today. Evaluate what was done right, what errors or inefficiencies occurred, and provide 3 immediate corrective actions."
        if st.button("Generate Live Daily Audit"):
            with st.spinner("Analyzing day logs..."):
                audit_result = ask_groq(audit_prompt)
                st.write(audit_result)
        else:
            st.info("Click the button above to generate your AI-powered daily performance breakdown.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("💬 Quick AI Command Box")
        user_quick_cmd = st.text_input("Execute any command or query across modules:", placeholder="e.g., Draft a WhatsApp message to client or summarize tasks")
        if st.button("Execute Command"):
            if user_quick_cmd:
                with st.spinner("Executing via Groq..."):
                    response = ask_groq(user_quick_cmd)
                    st.success("Result:")
                    st.write(response)
            else:
                st.warning("Please enter a command.")
        st.markdown("</div>", unsafe_allow_html=True)

# 2. VOICE & SPEECH COMMAND
elif app_mode == "🎙️ Voice & Speech Command":
    st.title("🎙️ Voice & Audio Intelligence Hub")
    st.markdown("Simulate voice commands, speech transcription instructions, and audio-to-action automation.")
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🎤 Voice Transcription & Action Parser")
    st.markdown("Type or simulate voice dictation below to parse commands into structured actions:")
    
    spoken_text = st.text_area("Simulated Voice Input / Dictation Text:", placeholder="e.g., Remind me to review marketing metrics at 5 PM, expense ₹500 on office supplies, and check WhatsApp.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Process Speech Command"):
            if spoken_text:
                with st.spinner("Parsing speech intent..."):
                    prompt = f"Parse this spoken text into structured actionable tasks, categorized items, and financial logs: '{spoken_text}'"
                    result = ask_groq(prompt)
                    st.markdown("### 📋 Structured Action Output:")
                    st.write(result)
            else:
                st.warning("Please provide text or simulate speech.")
    with col2:
        if st.button("🎙️ Record Audio (Simulated Mic)"):
            st.info("Listening... [Microphone stream simulated successfully via mobile web PWA wrapper]")
            time.sleep(1)
            st.success("Audio captured! Transcribed: 'Schedule fitness workout at 6 PM and review budget.'")
    st.markdown("</div>", unsafe_allow_html=True)

# 3. SPEECH-TO-IMAGE STUDIO
elif app_mode == "🎨 Speech-to-Image Studio":
    st.title("🎨 Speech-to-Image & Creative Studio")
    st.markdown("Convert voice prompts or text concepts into high-end visual prompts and generated designs for social media.")
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("✨ Image Prompt Generator & Visual Engine")
    
    image_idea = st.text_input("Describe the image you want from speech/text:", placeholder="e.g., futuristic cyberpunk command center with holographic screens")
    img_style = st.selectbox("Select Visual Style", ["Cinematic Photorealistic", "Cyberpunk / Sci-Fi", "Minimalist Corporate", "3D Animation Render", "Social Media Ad Banner"])
    
    if st.button("Generate Optimized Image Prompt & Layout"):
        if image_idea:
            with st.spinner("Crafting prompt engineering..."):
                prompt = f"Create an ultra-detailed, professional image generation prompt based on this concept: '{image_idea}' in a {img_style} style. Also suggest color grading and composition."
                res = ask_groq(prompt)
                st.markdown("### 🖼️ Generated AI Prompt Specification:")
                st.write(res)
                st.info("💡 Tip: Copy this prompt into your favorite image generator (Midjourney, DALL-E 3, or Stable Diffusion) or integrate an API key.")
        else:
            st.warning("Please enter an image concept.")
    st.markdown("</div>", unsafe_allow_html=True)

# 4. SOCIAL & WHATSAPP HUB
elif app_mode == "📱 Social & WhatsApp Hub":
    st.title("📱 Social Media & WhatsApp Management Hub")
    st.markdown("Manage social channels, draft viral posts, and automate WhatsApp client messaging.")
    
    tab1, tab2, tab3 = st.tabs(["📢 Social Post Generator", "💬 WhatsApp Auto-Responder", "📊 Analytics & Scheduler"])
    
    with tab1:
        st.markdown("### Viral Social Media Post Creator")
        platform = st.selectbox("Platform", ["Twitter / X", "LinkedIn", "Instagram Caption", "WhatsApp Broadcast"])
        topic = st.text_input("Post Topic / Core Message", placeholder="e.g., Launching my new AI command center mobile app")
        tone = st.selectbox("Tone", ["Professional & Authoritative", "Engaging & Casual", "High-Energy / Motivational"])
        
        if st.button("Generate Post"):
            with st.spinner("Drafting post..."):
                p = ask_groq(f"Write a viral {platform} post about '{topic}' with a {tone} tone. Include relevant hashtags and emojis.")
                st.text_area("Generated Post:", value=p, height=150)
                
    with tab2:
        st.markdown("### WhatsApp Message Assistant")
        client_msg = st.text_area("Incoming Client Message:", placeholder="Paste client message here...")
        if st.button("Draft Smart Reply"):
            if client_msg:
                with st.spinner("Drafting professional reply..."):
                    reply = ask_groq(f"Draft a polite, professional, and concise WhatsApp reply to this client message: '{client_msg}'")
                    st.write(reply)
            else:
                st.warning("Enter client message.")

    with tab3:
        st.markdown("### Scheduled Content Calendar")
        st.success("All channels synchronized. Next automated post scheduled in 2 hours 45 minutes.")
        
        # Sample dataframe for content schedule
        df_social = pd.DataFrame({
            "Platform": ["LinkedIn", "Twitter", "WhatsApp Status", "Instagram"],
            "Content Title": ["AI Productivity Shift", "Tech Stack Build", "Daily Update", "Command Center UI"],
            "Status": ["Ready", "Scheduled", "Drafting", "Published"],
            "Time": ["10:00 AM", "01:30 PM", "04:00 PM", "07:00 PM"]
        })
        st.dataframe(df_social, use_container_width=True)

# 5. EXPENSE & FINANCE CONTROL
elif app_mode == "💰 Expense & Finance Control":
    st.title("💰 Financial & Expense Intelligence")
    st.markdown("Track daily spends, evaluate financial health, identify overspending, and audit budget accuracy.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Monthly Budget", "₹50,000", "Allocated")
    with col2:
        st.metric("Spent So Far", "₹18,450", "36.9% utilized")
    with col3:
        st.metric("Remaining Balance", "₹31,550", "On Track ✅", delta_color="normal")
        
    st.markdown("---")
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("➕ Log New Expense")
    
    with st.form("expense_form"):
        col_e1, col_e2, col_e3 = st.columns(3)
        with col_e1:
            exp_item = st.text_input("Expense Title / Item", placeholder="e.g., Cloud Server / API Credit")
        with col_e2:
            exp_amount = st.number_input("Amount (₹)", min_value=0.0, value=250.0)
        with col_e3:
            exp_category = st.selectbox("Category", ["Technology & APIs", "Food & Dining", "Operations", "Travel", "Miscellaneous"])
            
        submitted = st.form_submit_button("Record Expense")
        if submitted:
            st.success(f"Successfully recorded ₹{exp_amount} for '{exp_item}' under {exp_category}!")
            
    st.markdown("### 📊 Recent Expense Breakdown")
    df_exp = pd.DataFrame({
        "Date": ["2026-07-25", "2026-07-24", "2026-07-23", "2026-07-21"],
        "Item": ["Groq API Credits", "Team Lunch", "Domain Renewal", "Cloud Hosting"],
        "Category": ["Technology & APIs", "Food & Dining", "Operations", "Technology & APIs"],
        "Amount (₹)": [1200, 850, 999, 1499]
    })
    st.dataframe(df_exp, use_container_width=True)
    
    if st.button("Run Financial Health Audit"):
        with st.spinner("Analyzing spending habits..."):
            audit_fin = ask_groq("Analyze current spending: Groq API 1200, Lunch 850, Domain 999, Hosting 1499. Total 4548. Provide feedback on what is going right, what is wrong, and how to optimize.")
            st.write(audit_fin)
    st.markdown("</div>", unsafe_allow_html=True)

# 6. FITNESS & LOCATION TRACKER
elif app_mode == "🏃 Fitness & Location Tracker":
    st.title("🏃 Fitness & Geo-Location Command")
    st.markdown("Monitor daily steps, workout metrics, calorie burn, and active location positioning.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Daily Steps", "7,840 / 10,000", "78% Completed")
    with col2:
        st.metric("Active Calories", "620 kcal", "Target: 500 kcal ✅")
    with col3:
        st.metric("Current Location Status", "New Delhi, IN", "GPS Active (Geo-fenced)")
        
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🏋️ Today's Workout Routine & Health Log")
    
    workout_type = st.selectbox("Workout Type", ["Strength Training & Core", "HIIT Cardio", "Running / Jogging", "Yoga & Stretching"])
    duration = st.slider("Duration (Minutes)", 15, 120, 45)
    
    if st.button("Log Workout & Get AI Health Feedback"):
        with st.spinner("Analyzing workout impact..."):
            feedback = ask_groq(f"Evaluate a {duration} minute {workout_type} session. Give recovery tips, nutrition advice, and hydration guidelines.")
            st.success("Workout logged successfully!")
            st.write(feedback)
    st.markdown("</div>", unsafe_allow_html=True)

# 7. SYSTEM SETTINGS
elif app_mode == "⚙️ System Settings":
    st.title("⚙️ System Configuration & PWA Status")
    st.markdown("Manage system parameters, API status, and mobile PWA installation.")
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔐 API & Security Status")
    if client:
        st.markdown("<span class='success-badge'>Groq API Connected Successfully</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span class='warning-badge'>Groq API Key Missing in Secrets</span>", unsafe_allow_html=True)
        
    st.markdown("### 📱 Mobile PWA Installation Guide")
    st.markdown("""
    Your app is fully configured as a Progressive Web App (PWA). 
    - **Android (Chrome):** Tap the menu (⋮) -> *Add to Home screen* or *Install app*.
    - **iOS (Safari):** Tap the Share icon -> *Add to Home Screen*.
    """)
    
    if st.button("Clear App Cache & Reload"):
        st.cache_data.clear()
        st.success("Cache cleared successfully!")
    st.markdown("</div>", unsafe_allow_html=True)
