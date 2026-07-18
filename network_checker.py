"""
DG AI Version 1
Network Checker
"""

import socket
import datetime


class NetworkChecker:

    def check_connection(self):

        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)

            return {
                "connected": True,
                "time": str(datetime.datetime.now())
            }

        except OSError:

            return {
                "connected": False,
                "time": str(datetime.datetime.now())
            }
