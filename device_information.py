"""
DG AI Version 1
Device Information

Purpose:
- Collect device information
- Provide hardware and system details
- Create device profile

Version: 1.0
"""

import platform
import os
import socket
import datetime
import logging


class DeviceInformation:
    """
    Professional Device Information Manager
    """

    def __init__(self):

        self.created_at = datetime.datetime.now()

        self.information_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # -----------------------------------------

    def get_system_info(self):
        """
        Get operating system information.
        """

        return {

            "system": platform.system(),

            "release": platform.release(),

            "version": platform.version(),

            "machine": platform.machine()

        }


    # -----------------------------------------

    def get_processor_info(self):
        """
        Get processor information.
        """

        return {

            "processor": platform.processor(),

            "cpu_count": os.cpu_count()

        }


    # -----------------------------------------

    def get_network_info(self):
        """
        Get basic network information.
        """

        return {

            "hostname": socket.gethostname(),

            "ip_address":
                socket.gethostbyname(
                    socket.gethostname()
                )

        }


    # -----------------------------------------

    def create_device_profile(self):
        """
        Create complete device profile.
        """

        profile = {

            "system":
                self.get_system_info(),

            "processor":
                self.get_processor_info(),

            "network":
                self.get_network_info(),

            "created":
                str(datetime.datetime.now())

        }


        self.information_history.append(
            profile
        )

        logging.info(
            "Device profile created"
        )

        return profile


    # -----------------------------------------

    def get_history(self):
        """
        Return stored profiles.
        """

        return self.information_history


    # -----------------------------------------

    def clear_history(self):
        """
        Clear information history.
        """

        self.information_history.clear()

        return True



# -----------------------------------------
# Testing
# -----------------------------------------

if __name__ == "__main__":

    info = DeviceInformation()

    print(
        info.create_device_profile()
    )
