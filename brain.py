# DG AI Brain

def process_command(command):

    command = command.lower()


    if "calculator" in command:
        return "OPEN_CALCULATOR"


    elif "todo" in command or "task" in command:
        return "OPEN_TODO"


    elif "note" in command:
        return "OPEN_NOTES"


    elif "memory" in command:
        return "OPEN_MEMORY"


    elif "hello" in command or "hi" in command:
        return "Hello, I am DG AI"


    elif "exit" in command:
        return "EXIT"


    else:
        return "UNKNOWN"
