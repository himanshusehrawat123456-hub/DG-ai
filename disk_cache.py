"""
DG AI Version 1
Disk Cache System

Purpose:
- Store cache data on disk
- Read and remove cached files

Version: 1.0
"""


import os
import json
import datetime



class DiskCache:
    """
    Handles disk cache operations.
    """



    def __init__(self, folder="cache_data"):

        self.folder = folder

        os.makedirs(self.folder, exist_ok=True)



    def set(self, key, value):
        """
        Save cache to disk.
        """

        file_path = os.path.join(
            self.folder,
            f"{key}.json"
        )


        data = {

            "value": value,

            "time": str(datetime.datetime.now())

        }


        with open(file_path, "w") as file:

            json.dump(data, file)


        return True



    def get(self, key):
        """
        Read cache from disk.
        """

        file_path = os.path.join(
            self.folder,
            f"{key}.json"
        )


        if not os.path.exists(file_path):

            return None


        with open(file_path, "r") as file:

            return json.load(file)



    def delete(self, key):
        """
        Delete cache file.
        """

        file_path = os.path.join(
            self.folder,
            f"{key}.json"
        )


        if os.path.exists(file_path):

            os.remove(file_path)

            return True


        return False



# Testing

if __name__ == "__main__":

    cache = DiskCache()

    cache.set("user", "Himanshu")

    print(cache.get("user"))
