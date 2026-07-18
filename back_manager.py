"""
DG AI Version 1
Backup Management System

Purpose:
- Create data backups
- Restore saved backups
- Protect DG AI information

Version: 1.0
"""


import os
import shutil
import datetime



class BackupManager:
    """
    Handles DG AI backup operations.
    """



    def __init__(self, backup_folder="backup"):

        self.backup_folder = backup_folder

        self._create_backup_folder()



    def _create_backup_folder(self):
        """
        Create backup directory.
        """

        if not os.path.exists(
            self.backup_folder
        ):

            os.makedirs(
                self.backup_folder
            )



    def create_backup(self, source_folder):
        """
        Create backup of DG AI data.

        Parameters:
            source_folder: folder to backup
        """

        try:

            timestamp = (
                datetime.datetime.now()
                .strftime("%Y%m%d_%H%M%S")
            )


            backup_name = (
                f"DG_AI_Backup_{timestamp}"
            )


            destination = os.path.join(
                self.backup_folder,
                backup_name
            )


            shutil.copytree(
                source_folder,
                destination
            )


            return destination



        except Exception as error:


            return str(error)



    def list_backups(self):
        """
        Show available backups.
        """

        return os.listdir(
            self.backup_folder
        )



    def delete_backup(self, backup_name):
        """
        Delete old backup.
        """

        path = os.path.join(
            self.backup_folder,
            backup_name
        )


        if os.path.exists(path):

            shutil.rmtree(path)

            return True


        return False




# Testing

if __name__ == "__main__":


    backup = BackupManager()


    print(
        "DG AI Backup System Ready"
    )


    print(
        backup.list_backups()
    )
