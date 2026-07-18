# DG AI Brain System


def process_command(command):

    command = command.lower()


    # Calculator
    if "calculator" in command or "calculate" in command:
        return "OPEN_CALCULATOR"


    # Todo
    elif "todo" in command or "task" in command:
        return "OPEN_TODO"


    # Chat
    elif "chat" in command or "talk" in command:
        return "OPEN_CHAT"


    # Command
    elif "command" in command:
        return "OPEN_COMMAND"


    # Memory
    elif "memory" in command or "remember" in command:
        return "OPEN_MEMORY"


    # Notes
    elif "note" in command or "notes" in command:
        return "OPEN_NOTES"


    # Greeting
    elif "hello" in command or "hi" in command:
        return "Hello, I am DG AI"


    # Exit
    elif "exit" in command or "close" in command:
        return "EXIT"


    # Unknown
    else:
        return "I am still learning this command"
