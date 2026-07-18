"""
DG AI Version 1
Memory Management System

Purpose:
- Store DG AI data
- Retrieve saved information
- Manage AI memory foundation

Version: 1.0
"""


import json
import os
from datetime import datetime



class MemoryManager:
    """
    Handles DG AI memory operations.
    """


    def __init__(self, file_path="data/memory.json"):

        self.file_path = file_path
        self.memory = {}

        self._create_storage()
        self._load_memory()



    def _create_storage(self):
        """
        Create memory storage directory.
        """

        folder = os.path.dirname(self.file_path)

        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def save_memory(self, key, value):
        """
        Save information into memory.

        Parameters:
            key (str): Memory name
            value: Stored information
        """

        self.memory[key] = {

            "value": value,

            "created_at":
            str(datetime.now())

        }


        self._save_memory()



    def get_memory(self, key):
        """
        Retrieve stored information.
        """

        return self.memory.get(
            key,
            "Memory not found"
        )



    def delete_memory(self, key):
        """
        Delete stored information.
        """

        if key in self.memory:

            del self.memory[key]

            self._save_memory()

            return True


        return False



    def get_all_memory(self):
        """
        Return complete memory.
        """

        return self.memory



    def _save_memory(self):
        """
        Save memory permanently.
        """

        with open(
            self.file_path,
            "w"
        ) as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )



    def _load_memory(self):
        """
        Load existing memory.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r"
            ) as file:

                self.memory = json.load(file)



# Testing

if __name__ == "__main__":


    memory = MemoryManager()


    memory.save_memory(
        "AI_Name",
        "DG AI"
    )


    memory.save_memory(
        "Creator",
        "Himanshu"
    )


    print("\nDG AI Memory")

    print("----------------")


    print(
        memory.get_all_memory()
    )


    print(
        "\nAI Name:",
        memory.get_memory("AI_Name")
    )
