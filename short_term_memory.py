"""
DG AI Version 1
Short Term Memory System

Purpose:
- Store temporary conversation data
- Manage current session memory

Version: 1.0
"""


import datetime



class ShortTermMemory:
    """
    Handles temporary memory operations.
    """



    def __init__(self):

        self.memory = []



    def add_memory(self, user, message):
        """
        Add new conversation memory.
        """

        data = {

            "user":
            user,

            "message":
            message,

            "time":
            str(datetime.datetime.now())

        }


        self.memory.append(data)


        return True



    def get_memory(self):
        """
        Return current session memory.
        """

        return self.memory



    def search_memory(self, keyword):
        """
        Search memory by keyword.
        """

        results = []


        for item in self.memory:

            if keyword.lower() in item["message"].lower():

                results.append(item)


        return results



    def clear_memory(self):
        """
        Clear temporary memory.
        """

        self.memory.clear()

        return True




# Testing

if __name__ == "__main__":


    memory = ShortTermMemory()


    memory.add_memory(
        "User",
        "My name is Himanshu"
    )


    memory.add_memory(
        "AI",
        "Hello Himanshu"
    )


    print(
        memory.get_memory()
    )


    print(
        memory.search_memory(
            "Himanshu"
        )
    )
