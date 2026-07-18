"""
DG AI Version 1
Logging Manager

Purpose:
- Manage DG AI logs
- Store log records

Version: 1.0
"""

import datetime


class LoggingManager:
    """
    Handles logging operations.
    """

    def __init__(self):
        self.logs = []

    def add_log(self, level, message):
        """
        Add a log entry.
        """

        log = {
            "id": len(self.logs) + 1,
            "level": level,
            "message": message,
            "time": str(datetime.datetime.now())
        }

        self.logs.append(log)

        return log

    def get_logs(self):
        """
        Return all logs.
        """

        return self.logs

    def clear_logs(self):
        """
        Clear all logs.
        """

        self.logs.clear()

        return True


# Testing

if __name__ == "__main__":

    manager = LoggingManager()

    print(
        manager.add_log(
            "INFO",
            "DG AI started successfully."
        )
    )
