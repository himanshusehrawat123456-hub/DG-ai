"""
DG AI - Network Module
Version: 1.0
"""

import socket
import urllib.request
import logging
from datetime import datetime


class NetworkManager:

    def __init__(self):
        self.status = "Offline"

    def check_internet(self):
        try:
            urllib.request.urlopen("https://www.google.com", timeout=5)
            self.status = "Online"
            return True
        except Exception:
            self.status = "Offline"
            return False

    def get_hostname(self):
        return socket.gethostname()

    def get_ip_address(self):
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "Unavailable"

    def show_network_info(self):
        print("\n===== DG AI Network =====")
        print("Status   :", self.status)
        print("Hostname :", self.get_hostname())
        print("IP       :", self.get_ip_address())
        print("Time     :", datetime.now())

    def log_status(self):
        logging.info(f"Network Status: {self.status}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    network = NetworkManager()

    network.check_internet()
    network.show_network_info()
    network.log_status()
