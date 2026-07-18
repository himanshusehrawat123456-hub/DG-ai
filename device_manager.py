"""
DG AI Version 1
Device Manager

Purpose:
- Manage connected devices
- Store device records

Version: 1.0
"""

import datetime


class DeviceManager:
    """
    Handles device management.
    """

    def __init__(self):
        self.devices = []

    def add_device(self, name, device_type):

        device = {
            "id": len(self.devices) + 1,
            "name": name,
            "type": device_type,
            "status": "Connected",
            "added_at": str(datetime.datetime.now())
        }

        self.devices.append(device)

        return device

    def get_devices(self):

        return self.devices

    def remove_device(self, device_id):

        for device in self.devices:

            if device["id"] == device_id:

                self.devices.remove(device)

                return True

        return False


if __name__ == "__main__":

    manager = DeviceManager()

    print(
        manager.add_device(
            "USB Drive",
            "Storage"
        )
    )
