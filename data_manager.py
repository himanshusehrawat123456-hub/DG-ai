"""
DG AI Version 1
Data Management System

Purpose:
- Manage DG AI data
- Store and retrieve information
- Provide data layer foundation

Version: 1.0
"""


import json
import os



class DataManager:
    """
    Handles DG AI data operations.
    """



    def __init__(self, folder="data"):

        self.folder = folder

        self._create_folder()



    def _create_folder(self):
        """
        Create data folder.
        """

        if not os.path.exists(self.folder):

            os.makedirs(self.folder)



    def save_data(self, filename, data):
        """
        Save data into JSON file.
        """

        path = os.path.join(
            self.folder,
            filename
        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )


        return True



    def load_data(self, filename):
        """
        Load data from JSON file.
        """

        path = os.path.join(
            self.folder,
            filename
        )


        if not os.path.exists(path):

            return None



        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)



    def delete_data(self, filename):
        """
        Delete data file.
        """

        path = os.path.join(
            self.folder,
            filename
        )


        if os.path.exists(path):

            os.remove(path)

            return True


        return False




# Testing

if __name__ == "__main__":


    manager = DataManager()


    user_data = {

        "name":
        "Himanshu",

        "project":
        "DG AI"

    }


    manager.save_data(
        "user.json",
        user_data
    )


    print(
        manager.load_data(
            "user.json"
        )
    )
