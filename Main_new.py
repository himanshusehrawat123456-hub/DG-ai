# main.py

import sys
from config import APP_NAME, VERSION
from brain import AIBrain
from utils import print_welcome_banner, format_bot_response

def main():
    # 1. बैनर प्रिंट करें
    print_welcome_banner(APP_NAME, VERSION)
    
    # 2. AI Brain को इनिशियलाइज़ करें
    ai = AIBrain(name=APP_NAME)
    
    # 3. मेन यूज़र लूप (While Loop)
    while True:
        try:
            # यूज़र से इनपुट लेना
            user_input = input("👤 You: ")
            
            # ऐप बंद करने की कमांड
            if user_input.lower().strip() in ["exit", "quit", "बाय"]:
                print(f"\n👋 {APP_NAME} बंद हो रहा है। आपका दिन शुभ हो!")
                break
            
            # Brain से रिस्पॉन्स पाना
            response = ai.process_query(user_input)
            
            # रिस्पॉन्स दिखाना
            print(format_bot_response(APP_NAME, response))
            print("-" * 40)

        except KeyboardInterrupt:
            # Ctrl+C दबाने पर सेफ़ एग्ज़िट
            print(f"\n\n👋 {APP_NAME} बंद कर दिया गया है।")
            sys.exit()
        except Exception as e:
            print(f"⚠️ एक एरर आया: {e}")

if __name__ == "__main__":
    main()
  
