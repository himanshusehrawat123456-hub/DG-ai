import os
import gradio as gr
from huggingface_hub import InferenceClient

# GitHub Environment Secret / Space Variable से सुरक्षित रूप से टोकन पढ़ना
HF_TOKEN = os.getenv("HF_TOKEN")

# Hugging Face API Client चालू करना
client = InferenceClient(token=HF_TOKEN)

def chat_with_qwen(message, history):
    messages = []
    
    # पुरानी बात याद रखने के लिए (Chat History)
    for user_msg, ai_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": ai_msg})
    
    # नया मैसेज जोड़ना
    messages.append({"role": "user", "content": message})

    try:
        # Qwen 2.5 72B Instruct मॉडल को कॉल करना
        response = client.chat_completion(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Chatbot Interface
demo = gr.ChatInterface(
    fn=chat_with_qwen,
    title="🤖 Qwen 2.5 AI Assistant",
    description="GitHub और Hugging Face Spaces पर कनेक्टेड Qwen2.5-72B AI मॉडल",
)

if __name__ == "__main__":
    demo.launch()
  
