"""
DG AI Version 1
AI Core Controller

Purpose:
- Connect all DG AI modules
- Manage command workflow
- Control AI processing pipeline

Version: 1.0
"""


from command_processor import CommandProcessor
from response_engine import ResponseEngine
from memory_manager import MemoryManager
from analytics import AnalyticsManager



class DGCoreAI:
    """
    Main DG AI Brain Controller.
    """


    def __init__(self):

        self.name = "DG AI Version 1"


        # Initialize modules

        self.command_processor = CommandProcessor()

        self.response_engine = ResponseEngine()

        self.memory = MemoryManager()

        self.analytics = AnalyticsManager()



    def process_input(self, user_input):
        """
        Main AI processing pipeline.

        Flow:

        User Input
              |
        Command Processor
              |
        Response Engine
              |
        Analytics Memory

        """


        # Command analysis

        command_data = (
            self.command_processor
            .receive_command(user_input)
        )


        # Generate response

        response = (
            self.response_engine
            .generate_response(command_data)
        )


        # Save analytics

        self.analytics.add_event(
            "Command Processed",
            {
                "command": user_input
            }
        )


        return response



    def remember(self, key, value):
        """
        Store information in AI memory.
        """

        self.memory.save_memory(
            key,
            value
        )



    def get_memory(self, key):
        """
        Retrieve stored memory.
        """

        return self.memory.get_memory(key)




# Testing

if __name__ == "__main__":


    dg_ai = DGCoreAI()


    result = dg_ai.process_input(
        "Hello DG AI"
    )


    print("\nDG AI Core Output")

    print("------------------")


    print(result)



    dg_ai.remember(
        "Project",
        "DG AI Version 1"
    )


    print(
        "\nMemory:",
        dg_ai.get_memory("Project")
    )
