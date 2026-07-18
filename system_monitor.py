"""
DG AI Version 1
System Monitor

Purpose:
- Monitor basic system information
- Store system status

Version: 1.0
"""

import datetime
import platform


class SystemMonitor:
    """
    Handles system monitoring.
    """

    def __init__(self):
        self.history = []

    def get_system_info(self):
        """
        Get basic system information.
        """

        info = {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "time": str(datetime.datetime.now())
        }

        self.history.append(info)

        return info

    def get_history(self):
        """
        Return monitoring history.
        """

        return self.history

    def clear_history(self):
        """
        Clear monitoring history.
        """

        self.history.clear()

        return True


# Testing

if __name__ == "__main__":

    monitor = SystemMonitor()

    print(
        monitor.get_system_info()
    )
