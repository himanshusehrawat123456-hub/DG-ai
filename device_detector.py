"""
DG AI Version 1
Device Detector

Purpose:
- Detect connected devices
- Detect operating system
- Detect storage devices
- Detect network availability
- Provide device information

Version: 1.0
Author: DG AI
"""

import os
import platform
import socket
import shutil
import logging
from datetime import datetime


class DeviceDetector:
    """
    Professional Device Detector
    DG AI Version 1
    """

    def __init__(self):

        self.system = platform.system()
        self.machine = platform.machine()
        self.processor = platform.processor()

        self.scan_time = None
        self.devices = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

    # -----------------------------------------

    def detect_platform(self):
        """
        Detect Operating System.
        """

        return {
            "system": self.system,
            "machine": self.machine,
            "processor": self.processor,
            "python_version": platform.python_version()
        }

    # -----------------------------------------

    def detect_hostname(self):

        return socket.gethostname()

    # -----------------------------------------

    def detect_ip(self):

        try:

            ip = socket.gethostbyname(
                socket.gethostname()
            )

            return ip

        except Exception:

            return "Unknown"

    # -----------------------------------------

    def detect_disk(self):

        disk = shutil.disk_usage("/")

        return {

            "total": disk.total,

            "used": disk.used,

            "free": disk.free

        }

    # -----------------------------------------

    def detect_cpu(self):

        return {

            "cpu_count": os.cpu_count(),

            "processor": self.processor

        }

    # -----------------------------------------

    def scan(self):
        """
        Run complete device scan.
        """

        self.scan_time = datetime.now()

        report = {

            "scan_time": str(self.scan_time),

            "platform": self.detect_platform(),

            "hostname": self.detect_hostname(),

            "ip_address": self.detect_ip(),

            "disk": self.detect_disk(),

            "cpu": self.detect_cpu()

        }

        self.devices.append(report)

        logging.info("Device Scan Completed")

        return report

    # -----------------------------------------

    def get_last_scan(self):

        if len(self.devices) == 0:

            return None

        return self.devices[-1]

    # -----------------------------------------

    def get_scan_history(self):

        return self.devices
    # -----------------------------------------

    def check_network(self):
        """
        Check basic internet/network availability.
        """

        try:

            socket.create_connection(
                ("8.8.8.8", 53),
                timeout=3
            )

            return {
                "network": True,
                "status": "Connected"
            }

        except OSError:

            return {
                "network": False,
                "status": "Disconnected"
            }


    # -----------------------------------------

    def detect_storage_type(self):
        """
        Detect storage information.
        """

        storage = self.detect_disk()

        return {

            "storage_available": True,

            "total_space": storage["total"],

            "used_space": storage["used"],

            "free_space": storage["free"]

        }


    # -----------------------------------------

    def get_environment(self):
        """
        Get device environment information.
        """

        return {

            "os": self.system,

            "machine": self.machine,

            "processor": self.processor

        }


    # -----------------------------------------

    def create_summary(self):
        """
        Create complete device summary.
        """

        return {

            "device": self.detect_platform(),

            "cpu": self.detect_cpu(),

            "storage": self.detect_storage_type(),

            "network": self.check_network(),

            "hostname": self.detect_hostname(),

            "ip": self.detect_ip()

        }


    # -----------------------------------------

    def clear_history(self):
        """
        Clear previous scans.
        """

        self.devices.clear()

        return True



# -----------------------------------------
# Testing
# -----------------------------------------

if __name__ == "__main__":

    detector = DeviceDetector()

    print("\nDG AI Device Detector\n")

    report = detector.scan()

    print(report)


    print("\nDevice Summary\n")

    print(
        detector.create_summary()
    )
