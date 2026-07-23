import os
from google import genai

# Environment Variable से API key उठाएगा
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY नहीं मिला! कृपया GitHub Secrets चेक करें।")

# नया Google GenAI Client
client = genai.Client(api_key=api_key)

# लेटेस्ट सपोर्टेड मॉडल नाम
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello! DG-AI system initialized successfully.",
)

print("\n--- DG-AI Output ---")
print(response.text)
print("--------------------\n")

