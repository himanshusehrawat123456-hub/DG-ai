"""
DG AI Version 1
Assistant Memory System

Purpose:
- Store assistant memories
- Retrieve previous information

Version: 1.0
"""


import datetime



class AssistantMemory:
    """
    Handles assistant memory operations.
    """



    def __init__(self):

        self.memory = []



    def save_memory(self, key, value):
        """
        Save new memory.
        """

        data = {

            "id":
            len(self.memory) + 1,

            "key":
            key,

            "value":
            value,

            "time":
            str(datetime.datetime.now())

        }


        self.memory.append(data)


        return True



    def search_memory(self, key):
        """
        Search memory by key.
        """

        results = []


        for item in self.memory:

            if item["key"].lower() == key.lower():

                results.append(item)


        return results



    def get_all_memory(self):
        """
        Return all memories.
        """

        return self.memory



    def clear_memory(self):
        """
        Clear memory.
        """

        self.memory.clear()

        return True




# Testing

if __name__ == "__main__":


    memory = AssistantMemory()


    memory.save_memory(
        "name",
        "Himanshu"
    )


    print(
        memory.get_all_memory()
    )
