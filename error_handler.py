"""
DG AI Version 1
Error Handling System

Purpose:
- Handle system errors
- Store error logs
- Provide debugging foundation

Version: 1.0
"""


import datetime
import json
import os



class ErrorHandler:
    """
    Handles DG AI errors.
    """



    def __init__(self, file_path="data/errors.json"):

        self.file_path = file_path

        self.errors = []

        self._create_storage()

        self._load_errors()



    def _create_storage(self):
        """
        Create error storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def add_error(self, error_type, message):
        """
        Store new error.
        """

        error = {

            "type":
            error_type,

            "message":
            message,

            "time":
            str(datetime.datetime.now())

        }


        self.errors.append(error)

        self._save_errors()


        return error



    def get_errors(self):
        """
        Return all errors.
        """

        return self.errors



    def clear_errors(self):
        """
        Clear error history.
        """

        self.errors.clear()

        self._save_errors()



    def _save_errors(self):
        """
        Save errors.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.errors,
                file,
                indent=4
            )



    def _load_errors(self):
        """
        Load previous errors.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.errors = json.load(file)




# Testing

if __name__ == "__main__":


    handler = ErrorHandler()


    handler.add_error(
        "Test Error",
        "DG AI testing error"
    )


    print(
        "DG AI Error Logs:"
    )


    print(
        handler.get_errors()
    )
