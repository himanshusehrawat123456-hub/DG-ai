import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env फ़ाइल या Environment Variables (GitHub Secrets) से Key लोड करें
load_dotenv()

# API Key प्राप्त करें
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API Key नहीं मिली! कृपया GitHub Secrets या .env फ़ाइल चेक करें।")

# Gemini AI सेटअप
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# DG-AI टेस्ट
response = model.generate_content("Hello! DG-AI system initialized.")
print(response.text)
