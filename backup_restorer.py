"""
DG AI Version 1
Backup Restorer

Purpose:
- Restore backup data
- Recover project files

Version: 1.0
"""

import os
import shutil


class BackupRestorer:
    """
    Handles backup restoration.
    """

    def restore_backup(self, backup_path, destination):
        """
        Restore backup to destination.
        """

        if not os.path.exists(backup_path):

            return False


        if os.path.exists(destination):

            shutil.rmtree(destination)


        shutil.copytree(
            backup_path,
            destination
        )

        return True


# Testing

if __name__ == "__main__":

    restorer = BackupRestorer()

    print(
        restorer.restore_backup(
            "backups/backup_example",
            "DG_AI"
        )
    )
