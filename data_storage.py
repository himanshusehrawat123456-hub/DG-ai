"""
DG AI Version 1
Data Storage System

Purpose:
- Store DG AI data
- Manage stored records

Version: 1.0
"""


import datetime



class DataStorage:
    """
    Handles data storage operations.
    """



    def __init__(self):

        self.data = []



    def store_data(self, key, value):
        """
        Store new data.
        """

        record = {

            "id":
            len(self.data) + 1,

            "key":
            key,

            "value":
            value,

            "time":
            str(datetime.datetime.now())

        }


        self.data.append(record)


        return record



    def get_data(self, key):
        """
        Retrieve data by key.
        """

        result = []


        for item in self.data:

            if item["key"] == key:

                result.append(item)


        return result



    def get_all_data(self):
        """
        Return all stored data.
        """

        return self.data



    def clear_data(self):
        """
        Clear storage.
        """

        self.data.clear()

        return True




# Testing

if __name__ == "__main__":


    storage = DataStorage()


    storage.store_data(
        "User",
        "Himanshu"
    )


    print(
        storage.get_all_data()
    )
