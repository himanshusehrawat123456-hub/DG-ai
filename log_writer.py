"""
DG AI Version 1
Log Writer

Purpose:
- Write log entries to a file

Version: 1.0
"""

import datetime


class LogWriter:
    """
    Handles writing logs to a file.
    """

    def __init__(self, file_name="dg_ai.log"):
        self.file_name = file_name

    def write_log(self, level, message):
        """
        Write a log entry.
        """

        log = (
            f"[{datetime.datetime.now()}] "
            f"{level}: {message}\n"
        )

        with open(self.file_name, "a", encoding="utf-8") as file:
            file.write(log)

        return True

    def get_log_file(self):
        """
        Return log file name.
        """

        return self.file_name


# Testing

if __name__ == "__main__":

    writer = LogWriter()

    writer.write_log(
        "INFO",
        "DG AI Log Writer Started"
    )

    print("Log written successfully.")
