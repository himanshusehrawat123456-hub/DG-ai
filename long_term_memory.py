"""
DG AI Version 1
Long Term Memory System

Purpose:
- Store permanent memory data
- Retrieve saved information

Version: 1.0
"""


import json
import os
import datetime



class LongTermMemory:
    """
    Handles permanent memory operations.
    """



    def __init__(self, file_name="long_memory.json"):

        self.file_name = file_name

        self.memory = self.load_memory()



    def load_memory(self):
        """
        Load saved memory from file.
        """

        if os.path.exists(self.file_name):

            with open(self.file_name, "r") as file:

                return json.load(file)


        return []



    def save_memory(self):
        """
        Save memory to file.
        """

        with open(self.file_name, "w") as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )


        return True



    def add_memory(self, key, value):
        """
        Add permanent memory.
        """

        data = {

            "key":
            key,

            "value":
            value,

            "time":
            str(datetime.datetime.now())

        }


        self.memory.append(data)

        self.save_memory()


        return True



    def search_memory(self, key):
        """
        Search saved memory.
        """

        for item in self.memory:

            if item["key"] == key:

                return item


        return None



    def get_all_memory(self):
        """
        Return all memories.
        """

        return self.memory




# Testing

if __name__ == "__main__":


    memory = LongTermMemory()


    memory.add_memory(
        "AI_Name",
        "DG AI"
    )


    print(
        memory.get_all_memory()
    )
