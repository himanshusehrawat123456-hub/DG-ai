# brain.py - DG-AI Logic Engine

def process(command):
    cmd = command.strip().lower()

    # 1. Voice संबंधित बात समझने के लिए
    if "voice" in cmd or "बोल" in cmd or "आवाज" in cmd:
        print("[Brain] Voice System चालू हो रहा है...")

    # 2. Save/Memory संबंधित बात समझने के लिए
    elif "remember" in cmd or "याद" in cmd or "save" in cmd:
        print("[Brain] Memory System को डेटा भेजा गया...")

    # 3. Search संबंधित बात समझने के लिए
    elif "search" in cmd or "khojo" in cmd or "गूगल" in cmd:
        print("[Brain] Web Search Engine शुरू हो रहा है...")

    # 4. अगर कोई मैच न मिले
    else:
        print(f"[Brain] '{command}' कमांड पर काम चल रहा है...")
        
