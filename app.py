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

app_mode = st.sidebar.radio("Select Workspace Mode", ["💬 Advanced Chat & Automation", "🎨 AI Image Generator"])

temperature = st.sidebar.slider("Temperature (Creativity)", 0.0, 2.0, 0.7, 0.1)
max_tokens = st.sidebar.slider("Max Output Tokens", 256, 8192, 2048, 256)
system_prompt = st.sidebar.text_area("System Persona / Rules", "You are Shailendra's elite AI assistant capable of advanced document analysis, image inspection, and task automation.")

if st.sidebar.button("🗑️ Reset Workspace"):
    st.session_state.messages = []
    st.rerun()

# 4. Main Interface Header
st.title("⚡ Gemini Advanced & Automation Studio")
st.caption("Multi-modal workspace supporting deep document analysis, image processing, and task workflows.")

# 5. Initialize Session Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MODE 1: IMAGE GENERATION STUDIO ---
if app_mode == "🎨 AI Image Generator":
    st.subheader("🎨 Native Image Studio")
    img_prompt = st.text_input("Describe the image you want to create:", placeholder="e.g., A futuristic dashboard...")
    
    col1, col2 = st.columns(2)
    with col1:
        aspect_ratio = st.selectbox("Aspect Ratio", ["1:1", "3:4", "4:3", "16:9", "9:16"])
    with col2:
        num_images = st.slider("Number of Images", 1, 4, 1)

    if st.button("✨ Generate Images"):
        if not api_key:
            st.error("Please enter your Gemini API Key in the sidebar.")
        else:
            with st.spinner("Generating images..."):
                try:
                    client = genai.Client(api_key=api_key)
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
            if "media_name" in message and message["media_name"]:
                st.info(f"📁 Attached File: {message['media_name']}")
            if "media_image" in message and message["media_image"]:
                st.image(message["media_image"], width=300)

    # Document & Image Uploader Widget for Analysis
    uploaded_file = st.file_uploader("📂 Upload Image or Document for Deep Analysis", type=["png", "jpg", "jpeg", "pdf", "txt", "csv"])

    # User Input Handling
    if prompt := st.chat_input("Ask anything or request document analysis..."):
        if not api_key:
            st.error("Please enter your Gemini API Key in the sidebar.")
        else:
            # Save file context if uploaded
            file_bytes = None
            file_name = None
            pil_img = None
            
            if uploaded_file is not None:
                file_name = uploaded_file.name
                file_bytes = uploaded_file.getvalue()
                if uploaded_file.type.startswith("image/"):
                    pil_img = Image.open(uploaded_file)

            # Append User Message
            user_msg = {
                "role": "user", 
                "content": prompt, 
                "media_name": file_name,
                "media_image": pil_img if pil_img else None
            }
            st.session_state.messages.append(user_msg)
            
            with st.chat_message("user"):
                st.markdown(prompt)
                if file_name:
                    st.info(f"📁 Attached File: {file_name}")
                if pil_img:
                    st.image(pil_img, width=300)

            # Generate AI Response with Full Multi-Modal and Automation Support
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                message_placeholder.markdown("Analyzing document/input...")
                
                try:
                    client = genai.Client(api_key=api_key)
                    contents = [prompt]
                    
                    # If an image is uploaded, pass it directly to Gemini model for analysis
                    if pil_img:
                        contents = [prompt if prompt else "Analyze this image in detail.", pil_img]
                    elif uploaded_file is not None and not uploaded_file.type.startswith("image/"):
                        # Handle text/document content reading
                        try:
                            doc_text = file_bytes.decode("utf-8", errors="ignore")
                            contents = [f"Here is the content of the uploaded document '{file_name}':\n\n{doc_text}\n\nUser Request: {prompt}"]
                        except Exception:
                            contents = [prompt, f"[Uploaded document: {file_name}]"]

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
                    
                    # Save Assistant Response
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": bot_response, 
                        "media_name": None,
                        "media_image": None
                    })
                    
                except Exception as e:
                    message_placeholder.error(f"Analysis/Execution Error: {e}")

# 6. Export Chat Option
if st.session_state.messages:
    chat_transcript = "\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
    st.sidebar.download_button(
        label="📥 Download Session (.txt)",
        data=chat_transcript,
        file_name="gemini_analysis_export.txt",
        mime="text/plain"
    )

