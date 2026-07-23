import os
import sys
import importlib
import time

class DGAIController:
    def __init__(self):
        self.modules = {}
        self.project_root = os.path.dirname(os.path.abspath(__file__))

    def load_all_modules(self):
        """Directory से सभी Python मॉड्यूल को लोड करता है"""
        print("=" * 45)
        print("          INITIALIZING DG-AI SYSTEM          ")
        print("=" * 45)

        files = os.listdir(self.project_root)
        
        # जिन फ़ाइलों को ऑटो-लोड नहीं करना है उनकी लिस्ट
        ignore_list = ['main.py', '__init__.py', 'config.json', 'user.json']

        for file_name in sorted(files):
            if file_name.endswith('.py') and file_name not in ignore_list:
                module_name = file_name[:-3]
                
                # 'test_' फ़ाइलों को Skip करें
                if module_name.startswith('test_'):
                    continue

                try:
                    # Dynamic import
                    module = importlib.import_module(module_name)
                    self.modules[module_name] = module
                    
                    display_name = module_name.replace('_', ' ').title()
                    print(f"Loading {display_name}...")
                    time.sleep(0.02)
                except Exception as e:
                    print(f"[!] Error loading {module_name}: {e}")

        print("\n[✓] All Systems Loaded Successfully")
        print("=" * 45)

    def process_command(self, user_command):
        """यूजर के इनपुट को प्रोसेस करना"""
        cmd = user_command.strip().lower()

        if not cmd:
            return

        if cmd in ['exit', 'quit', 'shutdown']:
            print("DG-AI shutting down... Goodbye!")
            sys.exit(0)

        elif cmd == 'help':
            print("\nAvailable Core Commands:")
            print(" - status : दिखाता है कितने मॉड्यूल एक्टिव हैं")
            print(" - list   : सभी लोड हुए मॉड्यूल्स की सूची")
            print(" - exit   : AI सिस्टम बंद करने के लिए\n")

        elif cmd == 'status':
            print(f"\n[System Status] Active Modules: {len(self.modules)}\n")

        elif cmd == 'list':
            print("\nLoaded Modules:")
            for mod in sorted(self.modules.keys()):
                print(f" - {mod}")
            print()

        else:
            print(f"\n[DG-AI Core] Processing instruction: '{user_command}'...")
            if 'brain' in self.modules and hasattr(self.modules['brain'], 'process'):
                self.modules['brain'].process(user_command)
            else:
                print("Execution complete.\n")

    def start_cli(self):
        """Terminal User Interface (CLI) Loop"""
        self.load_all_modules()
        print("\nWelcome to DG-AI Interface! Type 'help' for options, 'exit' to quit.\n")
        
        while True:
            try:
                user_input = input("DG-AI > ")
                self.process_command(user_input)
            except KeyboardInterrupt:
                print("\nShutting down DG-AI...")
                break

if __name__ == "__main__":
    app = DGAIController()
    app.start_cli()
    self.modules
