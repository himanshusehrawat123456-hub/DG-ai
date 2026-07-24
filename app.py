import os
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="Gemini Advanced Studio & Automation Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for Sleek Dark Mode & Chat Styling
st.markdown("""
<style>
    .main { background-color: #0e1117; color: #fafafa; }
    .stChatMessage { border-radius: 14px; padding: 12px; margin-bottom: 12px; }
    h1 { background: linear-gradient(90deg, #4285F4, #9B72CF, #D96570); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .stButton button { border-radius: 8px; width: 100%; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Control Hub
st.sidebar.title("⚡ AI Command Center")
api_key = st.sidebar.text_input("Gemini API Key", type="password", value=os.environ.get("GEMINI_API_KEY", ""))

# Comprehensive Model Suite including latest Gemini 3.6, 3.5 & 2.x
model_name = st.sidebar.selectbox(
    "Select AI Model",
    [
        "gemini-3.6-flash",
        "gemini-3.5-flash",
        "gemini-3.1-pro-preview",
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-2.0-flash",
        "gemini-1.5-pro"
    ],
    index=0
)

# Mode Selection: Text/Multimodal Chat vs. Image Generation Studio
app_mode = st.sidebar.radio("Select Workspace Mode", ["💬 Advanced Chat & Automation", "🎨 AI Image Generator"])

temperature = st.sidebar.slider("Temperature (Creativity)", 0.0, 2.0, 0.7, 0.1)
max_tokens = st.sidebar.slider("Max Output Tokens", 256, 8192, 2048, 256)
system_prompt = st.sidebar.text_area("System Persona / Automation Rules", "You are Shailendra's elite AI automation assistant capable of handling smart tasks, tool integration, coding, and general queries.")

if st.sidebar.button("🗑️ Reset Workspace"):
    st.session_state.messages = []
    st.rerun()

# 4. Main Interface Header
st.title("⚡ Gemini Advanced & Automation Studio")
st.caption("Production-grade multi-modal workspace for Chat, Image Creation, and Workflow Automation.")

# 5. Initialize Session Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MODE 1: IMAGE GENERATION STUDIO ---
if app_mode == "🎨 AI Image Generator":
    st.subheader("🎨 Native Image Studio (Nano Banana / Imagen)")
    img_prompt = st.text_input("Describe the image you want to create:", placeholder="e.g., A futuristic cyberpunk delivery drone flying over Delhi...")
    
    col1, col2 = st.columns(2)
    with col1:
        aspect_ratio = st.selectbox("Aspect Ratio", ["1:1", "3:4", "4:3", "16:9", "9:16"])
    with col2:
        num_images = st.slider("Number of Images", 1, 4, 1)

    if st.button("✨ Generate Images"):
        if not api_key:
            st.error("Please enter your Gemini API Key in the sidebar.")
        else:
            with st.spinner("Generating your images with AI..."):
                try:
                    client = genai.Client(api_key=api_key)
                    # Using Imagen / Native Image Generation capability
                    result = client.models.generate_images(
                        model='imagen-3.0-generate-002',
                        prompt=img_prompt,
                        config=types.GenerateImagesConfig(
                            number_of_images=num_images,
                            aspect_ratio=aspect_ratio,
                            output_mime_type="image/jpeg"
                        )
                    )
                    st.success("Images generated successfully!")
                    cols = st.columns(num_images)
                    for idx, generated_image in enumerate(result.generated_images):
                        image_bytes = generated_image.image.image_bytes
                        import io
                        image = Image.open(io.BytesIO(image_bytes))
                        with cols[idx]:
                            st.image(image, caption=f"Creation {idx+1}", use_column_width=True)
                except Exception as e:
                    st.error(f"Image generation error: {e}")

# --- MODE 2: ADVANCED CHAT & AUTOMATION ---
else:
    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "media" in message and message["media"]:
                st.image(message["media"], width=300)

    # Optional Multi-modal File Uploader
    uploaded_file = st.file_uploader("Upload Image/Document for analysis", type=["png", "jpg", "jpeg", "pdf", "txt"])

    # Define Dummy Automation Tools (Function Calling Simulation for Porter, YouTube, App Management)
    def book_porter(pickup: str, drop: str, item_type: str):
        return f"🚚 **Porter Automation Triggered!** Successfully booked transport for '{item_type}' from *{pickup}* to *{drop}*. Driver assigned shortly."

    def control_youtube(action: str, query: str = ""):
        if action == "search":
            return f"📺 **YouTube Automation:** Searched and opened playlist for '{query}'. [Click here to watch on YouTube](https://www.youtube.com/results?search_query={query.replace(' ', '+')})"
        return "📺 **YouTube Automation:** Player status updated."

    def manage_app_system(command: str):
        return f"⚙️ **App Management System:** Executed system command/routine: `{command}` successfully."

    # User Input Handling
    if prompt := st.chat_input("Ask anything, command automation (e.g., 'Book Porter from Connaught Place to Noida')..."):
        if not api_key:
            st.error("Please enter your Gemini API Key in the sidebar.")
        else:
            # Append User Message
            user_msg = {"role": "user", "content": prompt, "media": uploaded_file}
            st.session_state.messages.append(user_msg)
            
            with st.chat_message("user"):
                st.markdown(prompt)
                if uploaded_file:
                    st.image(uploaded_file, width=300)

            # Generate AI Response with Agentic Logic
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                message_placeholder.markdown("Thinking & processing automation...")
                
                try:
                    # Smart Automation Keyword Interception (Agentic shortcuts)
                    bot_response = ""
                    lower_prompt = prompt.lower()
                    
                    if "porter" in lower_prompt or "delivery" in lower_prompt or "book truck" in lower_prompt:
                        # Simulated intelligent tool handler
                        bot_response = book_porter("Current Location", "Destination Hub", "General Goods / Packages")
                    elif "youtube" in lower_prompt or "video" in lower_prompt:
                        q_term = prompt.replace("youtube", "").replace("play", "").strip()
                        bot_response = control_youtube("search", q_term if q_term else "latest tech")
                    elif "app" in lower_prompt or "system" in lower_prompt or "manage" in lower_prompt:
                        bot_response = manage_app_system(prompt)
                    else:
                        # Standard Gemini Model Call
                        client = genai.Client(api_key=api_key)
                        contents = [prompt]
                        pil_image = None
                        if uploaded_file and uploaded_file.type.startswith("image/"):
                            pil_image = Image.open(uploaded_file)
                            contents = [prompt, pil_image]

                        config = types.GenerateContentConfig(
                            temperature=temperature,
                            max_output_tokens=max_tokens,
                            system_instruction=system_prompt
                        )

                        response = client.models.generate_content(
                            model=model_name,
                            contents=contents,
                            config=config
                        )
                        bot_response = response.text

                    message_placeholder.markdown(bot_response)
                    st.session_state.messages.append({"role": "assistant", "content": bot_response, "media": None})
                    
                except Exception as e:
                    message_placeholder.error(f"Execution Error: {e}")

# 6. Export Chat Option in Sidebar
if st.session_state.messages:
    chat_transcript = "\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
    st.sidebar.download_button(
        label="📥 Download Session (.txt)",
        data=chat_transcript,
        file_name="gemini_automation_export.txt",
        mime="text/plain"
  )
  
