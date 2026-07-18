"""
DG AI Version 1
Memory Storage

Purpose:
- Store AI memory data
- Retrieve saved memories
- Manage memory records

Version: 1.0
"""

import json
import os
import logging
from datetime import datetime


class MemoryStorage:
    """
    Professional AI Memory Storage Manager
    """

    def __init__(
        self,
        file_name="ai_memory.json"
    ):

        self.file_name = file_name

        self.memory_data = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        self.load_memory()


    # ---------------------------------

    def load_memory(self):
        """
        Load saved memory.
        """

        try:

            if os.path.exists(
                self.file_name
            ):

                with open(
                    self.file_name,
                    "r"
                ) as file:

                    self.memory_data = json.load(
                        file
                    )


        except Exception as error:

            logging.error(error)

            self.memory_data = []


    # ---------------------------------

    def save_memory(self):
        """
        Save memory to file.
        """

        try:

            with open(
                self.file_name,
                "w"
            ) as file:

                json.dump(
                    self.memory_data,
                    file,
                    indent=4
                )


            return True


        except Exception as error:

            logging.error(error)

            return False


    # ---------------------------------

    def add_memory(
        self,
        user_id,
        information,
        category="general"
    ):
        """
        Add new memory.
        """

        memory = {

            "id":
            len(self.memory_data) + 1,

            "user_id":
            user_id,

            "information":
            information,

            "category":
            category,

            "created":
            str(datetime.now())

        }


        self.memory_data.append(
            memory
        )


        self.save_memory()


        return memory


    # ---------------------------------

    def get_all_memory(self):
        """
        Return all memory.
        """

        return self.memory_data


    # ---------------------------------

    def find_memory(
        self,
        keyword
    ):
        """
        Search memory.
        """

        result = []


        for memory in self.memory_data:

            if keyword.lower() in str(memory).lower():

                result.append(memory)


        return result


    # ---------------------------------

    def delete_memory(
        self,
        memory_id
    ):
        """
        Delete memory by ID.
        """

        for memory in self.memory_data:

            if memory["id"] == memory_id:

                self.memory_data.remove(
                    memory
                )

                self.save_memory()

                return True


        return False


    # ---------------------------------

    def clear_memory(self):
        """
        Remove all memory.
        """

        self.memory_data.clear()

        self.save_memory()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    storage = MemoryStorage()


    print(
        storage.add_memory(
            1,
            "User likes DG AI project",
            "preference"
        )
    )
