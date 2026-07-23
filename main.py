import os
import time
from google import genai
from google.genai.errors import APIError

def main():
    # secrets/env से API KEY ले रहा है
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not found!")

    # Google GenAI Client Initialize करें
    client = genai.Client(api_key=api_key)

    # Retry Mechanism के साथ API Call
    max_retries = 3
    base_delay = 10  # 10 सेकंड का ब्रेक

    for attempt in range(1, max_retries + 1):
        try:
            print(f"Generating content (Attempt {attempt}/{max_retries})...")
            
            # API Request
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents='Explain how AI works in 2 simple sentences.'
            )
            
            # अगर Success हुआ
            print("\n--- Response Received ---")
            print(response.text)
            print("-------------------------\n")
            return  # कोड यहीं सफलतापूर्वक पूरा हो जाएगा

        except APIError as e:
            # अगर 429 Rate Limit एरर आया
            if getattr(e, 'code', None) == 429 or "429" in str(e):
                print(f"⚠️ Rate limit hit (429)! Waiting {base_delay} seconds before retrying...")
                time.sleep(base_delay)
            else:
                # कोई और एरर हुआ तो दिखाएगा
                print(f"❌ API Error occurred: {e}")
                raise e
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
            raise e

    raise Exception("❌ Exceeded max retries due to Gemini 429 Rate Limit.")

if __name__ == "__main__":
    main()
    
