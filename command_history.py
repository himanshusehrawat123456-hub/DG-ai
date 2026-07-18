"""
DG AI Version 1
Command History Management System

Purpose:
- Store user commands
- Retrieve previous commands
- Provide conversation history foundation

Version: 1.0
"""


import datetime
import json
import os



class CommandHistory:
    """
    Handles DG AI command history.
    """



    def __init__(self, file_path="data/command_history.json"):

        self.file_path = file_path

        self.history = []

        self._create_storage()

        self._load_history()



    def _create_storage(self):
        """
        Create storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def add_command(self, command):
        """
        Store a new command.
        """

        record = {

            "command":
            command,

            "time":
            str(datetime.datetime.now())

        }


        self.history.append(record)

        self._save_history()



    def get_history(self):
        """
        Return all commands.
        """

        return self.history



    def clear_history(self):
        """
        Remove command history.
        """

        self.history.clear()

        self._save_history()



    def _save_history(self):
        """
        Save history data.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.history,
                file,
                indent=4
            )



    def _load_history(self):
        """
        Load previous history.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.history = json.load(file)




# Testing

if __name__ == "__main__":


    history = CommandHistory()


    history.add_command(
        "Hello DG AI"
    )


    history.add_command(
        "Open application"
    )


    print(
        "DG AI Command History:"
    )


    print(
        history.get_history()
    )
