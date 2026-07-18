"""
DG AI Version 1
File Tools System

Purpose:
- Manage file operations
- Provide file handling foundation

Version: 1.0
"""


import os
import datetime



class FileTools:
    """
    Handles DG AI file operations.
    """



    def __init__(self):

        self.history = []



    def create_file(self, filename, content=""):
        """
        Create a new file.
        """

        with open(filename, "w") as file:

            file.write(content)


        self.history.append({

            "action": "create",

            "file": filename,

            "time":
            str(datetime.datetime.now())

        })


        return True



    def read_file(self, filename):
        """
        Read file content.
        """

        if os.path.exists(filename):

            with open(filename, "r") as file:

                return file.read()


        return None



    def write_file(self, filename, content):
        """
        Write content to file.
        """

        with open(filename, "w") as file:

            file.write(content)


        return True



    def delete_file(self, filename):
        """
        Delete file.
        """

        if os.path.exists(filename):

            os.remove(filename)

            return True


        return False



    def get_history(self):
        """
        Return file operation history.
        """

        return self.history




# Testing

if __name__ == "__main__":


    tools = FileTools()


    tools.create_file(
        "test.txt",
        "Hello DG AI"
    )


    print(
        tools.read_file(
            "test.txt"
        )
    )
