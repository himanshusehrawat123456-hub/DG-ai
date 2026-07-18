"""
DG AI Version 1
File Organizer

Purpose:
- Organize files by extension
- Create folders automatically
- Move files into categories

Version: 1.0
"""

import os
import shutil
from datetime import datetime


class FileOrganizer:
    """
    Handles basic file organization.
    """

    def __init__(self):

        self.history = []


    def get_category(self, extension):
        """
        Decide folder category by file extension.
        """

        categories = {

            ".jpg": "Images",
            ".png": "Images",
            ".jpeg": "Images",

            ".mp4": "Videos",

            ".mp3": "Audio",

            ".pdf": "Documents",
            ".docx": "Documents",
            ".txt": "Documents",

            ".py": "Code",
            ".js": "Code"

        }

        return categories.get(
            extension.lower(),
            "Others"
        )


    def create_folder(self, folder_path):
        """
        Create folder if not exists.
        """

        if not os.path.exists(folder_path):

            os.makedirs(folder_path)


    def organize_file(self, file_path, destination):

        if not os.path.exists(file_path):

            return {
                "success": False,
                "message": "File not found"
            }


        extension = os.path.splitext(
            file_path
        )[1]


        category = self.get_category(
            extension
        )


        folder = os.path.join(
            destination,
            category
        )


        self.create_folder(folder)


        new_path = os.path.join(
            folder,
            os.path.basename(file_path)
        )


        shutil.move(
            file_path,
            new_path
        )


        record = {

            "file": file_path,

            "moved_to": new_path,

            "time": str(datetime.now())

        }


        self.history.append(record)


        return record


    def get_history(self):

        return self.history



if __name__ == "__main__":

    organizer = FileOrganizer()

    print(
        organizer.get_category(".pdf")
    )
