"""
DG AI Version 1
Disk Manager

Purpose:
- Monitor disk usage
- Store disk information

Version: 1.0
"""

import shutil
import datetime


class DiskManager:
    """
    Handles disk monitoring.
    """

    def __init__(self):
        self.history = []

    def get_disk_info(self, path="."):

        usage = shutil.disk_usage(path)

        info = {
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
            "checked_at": str(datetime.datetime.now())
        }

        self.history.append(info)

        return info

    def get_history(self):

        return self.history

    def clear_history(self):

        self.history.clear()

        return True


# Testing

if __name__ == "__main__":

    disk = DiskManager()

    print(disk.get_disk_info())
