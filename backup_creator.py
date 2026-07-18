"""
DG AI Version 1
Backup Creator

Purpose:
- Create backup files
- Store backup information

Version: 1.0
"""

import os
import shutil
import datetime


class BackupCreator:
    """
    Handles backup creation.
    """

    def __init__(self, source_folder, backup_folder="backups"):

        self.source_folder = source_folder
        self.backup_folder = backup_folder

        os.makedirs(self.backup_folder, exist_ok=True)


    def create_backup(self):
        """
        Create a backup of the source folder.
        """

        timestamp = datetime.datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        destination = os.path.join(
            self.backup_folder,
            f"backup_{timestamp}"
        )

        shutil.copytree(
            self.source_folder,
            destination
        )

        return destination


# Testing

if __name__ == "__main__":

    creator = BackupCreator("DG_AI")

    print(
        creator.create_backup()
    )
