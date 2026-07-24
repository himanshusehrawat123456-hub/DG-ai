import google.generativeai as genai

def configure_gemini(api_key):
    """Configures and returns the Gemini model."""
    genai.configure(api_key=api_key)
    # Using gemini-pro for stable API compatibility
    model = genai.GenerativeModel("gemini-pro")
    return model

def get_gemini_response(model, prompt):
    """Sends a prompt to the chat model and returns the response text."""
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    return response.text
  
