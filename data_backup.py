"""
DG AI Version 1
Data Backup System

Purpose:
- Create data backups
- Manage backup records

Version: 1.0
"""


import datetime



class DataBackup:
    """
    Handles backup operations.
    """



    def __init__(self):

        self.backups = []



    def create_backup(self, data_name, data):
        """
        Create backup record.
        """

        backup = {

            "id":
            len(self.backups) + 1,

            "name":
            data_name,

            "data":
            data,

            "status":
            "Completed",

            "time":
            str(datetime.datetime.now())

        }


        self.backups.append(backup)


        return backup



    def get_backups(self):
        """
        Return backup history.
        """

        return self.backups



    def delete_backup(self, backup_id):
        """
        Delete backup.
        """

        for backup in self.backups:

            if backup["id"] == backup_id:

                self.backups.remove(backup)

                return True


        return False




# Testing

if __name__ == "__main__":


    backup = DataBackup()


    print(
        backup.create_backup(
            "Memory Data",
            {
                "user": "Himanshu"
            }
        )
    )
