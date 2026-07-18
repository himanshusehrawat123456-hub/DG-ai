"""
DG AI Version 1
Network Monitor
"""

import datetime


class NetworkMonitor:

    def __init__(self):
        self.history = []

    def monitor(self, speed):

        data = {
            "speed": speed,
            "checked_at": str(datetime.datetime.now())
        }

        self.history.append(data)

        return data

    def get_history(self):
        return self.history
