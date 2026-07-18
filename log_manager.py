"""
DG AI Version 1
Logging Management System

Purpose:
- Store system logs
- Track DG AI activities
- Provide debugging foundation

Version: 1.0
"""


import datetime
import json
import os



class LogManager:
    """
    Handles DG AI system logs.
    """



    def __init__(self, file_path="data/logs.json"):

        self.file_path = file_path

        self.logs = []

        self._create_storage()

        self._load_logs()



    def _create_storage(self):
        """
        Create log storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def add_log(self, level, message):
        """
        Add new system log.

        Levels:
        - INFO
        - WARNING
        - ERROR
        """

        log = {

            "level":
            level,

            "message":
            message,

            "time":
            str(datetime.datetime.now())

        }


        self.logs.append(log)

        self._save_logs()


        return log



    def get_logs(self):
        """
        Return all logs.
        """

        return self.logs



    def clear_logs(self):
        """
        Remove all logs.
        """

        self.logs.clear()

        self._save_logs()



    def _save_logs(self):
        """
        Save logs to file.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.logs,
                file,
                indent=4
            )



    def _load_logs(self):
        """
        Load existing logs.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.logs = json.load(file)




# Testing

if __name__ == "__main__":


    logger = LogManager()


    logger.add_log(
        "INFO",
        "DG AI Started"
    )


    logger.add_log(
        "WARNING",
        "Testing Mode Active"
    )


    print(
        "DG AI Logs:"
    )


    print(
        logger.get_logs()
    )
