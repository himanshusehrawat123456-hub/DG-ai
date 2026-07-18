"""
DG AI Version 1
Cache Cleaner System

Purpose:
- Remove expired cache
- Clean memory and disk cache

Version: 1.0
"""


import os
import datetime



class CacheCleaner:
    """
    Handles cache cleaning operations.
    """



    def __init__(self):

        self.clean_history = []



    def clean_folder(self, folder_path):
        """
        Delete all files in a cache folder.
        """

        removed = 0


        if os.path.exists(folder_path):

            for file_name in os.listdir(folder_path):

                file_path = os.path.join(folder_path, file_name)

                if os.path.isfile(file_path):

                    os.remove(file_path)

                    removed += 1


        record = {

            "removed_files": removed,

            "time": str(datetime.datetime.now())

        }


        self.clean_history.append(record)


        return record



    def get_history(self):
        """
        Return cleaning history.
        """

        return self.clean_history



    def clear_history(self):
        """
        Clear cleaning history.
        """

        self.clean_history.clear()

        return True




# Testing

if __name__ == "__main__":

    cleaner = CacheCleaner()

    print(
        cleaner.clean_folder(
            "cache_data"
        )
    )
