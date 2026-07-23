import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY नहीं मिला!")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello! DG-AI system initialized successfully.",
)

print("\n--- DG-AI Output ---")
print(response.text)
print("--------------------\n")
