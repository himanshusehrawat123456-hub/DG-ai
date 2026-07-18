"""
DG AI - Backup Manager
Version: 1.0
"""

import os
import shutil
import logging
from datetime import datetime


class BackupManager:

    def __init__(self):
        self.backup_folder = "backups"

        if not os.path.exists(self.backup_folder):
            os.makedirs(self.backup_folder)

    def create_backup(self, source_file):

        if not os.path.exists(source_file):
            print("Source file not found.")
            return

        filename = os.path.basename(source_file)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        destination = os.path.join(
            self.backup_folder,
            f"{timestamp}_{filename}"
        )

        shutil.copy2(source_file, destination)

        logging.info(f"Backup Created: {destination}")

        print("Backup Created Successfully")

    def list_backups(self):

        print("\n===== Available Backups =====")

        files = os.listdir(self.backup_folder)

        if not files:
            print("No backups found.")
            return

        for file in files:
            print(file)

    def delete_backup(self, backup_name):

        path = os.path.join(self.backup_folder, backup_name)

        if os.path.exists(path):
            os.remove(path)
            print("Backup Deleted")

    def status(self):

        print("DG AI Backup Manager Ready")


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    backup = BackupManager()

    backup.status()
