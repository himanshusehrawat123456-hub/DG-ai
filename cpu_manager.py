"""
DG AI Version 1
CPU Manager

Purpose:
- Monitor CPU information
- Store CPU usage history

Version: 1.0
"""

import os
import datetime


class CPUManager:
    """
    Handles CPU monitoring.
    """

    def __init__(self):
        self.history = []

    def get_cpu_info(self):

        info = {
            "cpu_count": os.cpu_count(),
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

    cpu = CPUManager()

    print(cpu.get_cpu_info())
