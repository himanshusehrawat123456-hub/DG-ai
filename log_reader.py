"""
DG AI Version 1
Log Reader

Purpose:
- Read log entries from a log file

Version: 1.0
"""


import os


class LogReader:
    """
    Handles reading log files.
    """


    def __init__(self, file_name="dg_ai.log"):

        self.file_name = file_name



    def read_logs(self):
        """
        Read all logs.
        """

        if not os.path.exists(self.file_name):

            return []


        with open(
            self.file_name,
            "r",
            encoding="utf-8"
        ) as file:

            return file.readlines()



    def print_logs(self):
        """
        Print all logs.
        """

        logs = self.read_logs()

        for log in logs:

            print(log.strip())



# Testing

if __name__ == "__main__":

    reader = LogReader()

    reader.print_logs()
