# utils.py

def print_welcome_banner(app_name, version):
    """प्रोजेक्ट स्टार्ट होने पर वेलकम मैसेज दिखाना"""
    print("=" * 40)
    print(f"       WELCOME TO {app_name} (v{version})")
    print("=" * 40)
    print("टाइप करें 'exit' या 'quit' बाहर निकलने के लिए।\n")

def format_bot_response(bot_name, response):
    """AI के रिस्पॉन्स को सही फॉर्मेट में दिखाना"""
    return f"🤖 [{bot_name}]: {response}"
  
