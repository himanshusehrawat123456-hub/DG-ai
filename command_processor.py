"""
DG AI Version 1
Command Processing Engine

Purpose:
- Process user commands
- Identify command type
- Prepare communication layer for AI Brain

Version: 1.0
"""


class CommandProcessor:
    """
    Handles command receiving and processing.
    """


    def __init__(self):

        self.command_history = []



    def receive_command(self, command):
        """
        Receive user command.

        Parameters:
            command (str): User input command

        Returns:
            dict: Processed command data
        """

        if not isinstance(command, str):

            raise TypeError(
                "Command must be a string"
            )


        command = command.strip()


        self.command_history.append(command)


        return self.analyze_command(command)



    def analyze_command(self, command):
        """
        Analyze command and identify category.
        """


        command_lower = command.lower()


        if "open" in command_lower:

            category = "system_action"


        elif "hello" in command_lower or "hi" in command_lower:

            category = "conversation"


        elif "search" in command_lower:

            category = "web_action"


        else:

            category = "unknown"



        return {

            "original_command": command,

            "category": category,

            "status": "processed"

        }



    def get_history(self):
        """
        Return previous commands.
        """

        return self.command_history



# Testing

if __name__ == "__main__":


    processor = CommandProcessor()


    commands = [

        "Hello DG AI",

        "Open Chrome",

        "Search Python Tutorial",

        "Play Music"

    ]


    for cmd in commands:

        result = processor.receive_command(cmd)

        print(result)



    print("\nCommand History:")

    print(
        processor.get_history()
    )
