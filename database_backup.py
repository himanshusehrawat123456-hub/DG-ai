"""
DG AI Version 1
Database Backup

Purpose:
- Create database backup
- Restore saved data
- Maintain backup history

Version: 1.0
"""

import json
import os
from datetime import datetime


class DatabaseBackup:


    def __init__(self):

        self.backup_history = []


    def create_backup(
        self,
        data,
        file_name="backup.json"
    ):

        try:

            with open(
                file_name,
                "w"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4
                )


            record = {

                "file": file_name,

                "action": "backup",

                "time": str(datetime.now())

            }


            self.backup_history.append(record)

            return record


        except Exception as error:

            return {

                "success": False,

                "error": str(error)

            }


    def restore_backup(
        self,
        file_name
    ):

        if not os.path.exists(file_name):

            return None


        with open(
            file_name,
            "r"
        ) as file:

            data = json.load(file)


        return data


    def get_history(self):

        return self.backup_history
