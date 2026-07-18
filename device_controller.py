"""
DG AI Version 1
Device Controller

Purpose:
- Control device operations
- Manage device status
- Enable/Disable device actions foundation

Version: 1.0
"""

import logging
from datetime import datetime


class DeviceController:
    """
    Professional Device Controller
    """

    def __init__(self):

        self.control_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # -----------------------------------------

    def connect_device(self, device_name):
        """
        Register device connection.
        """

        record = {

            "device": device_name,

            "action": "connect",

            "status": "connected",

            "time": str(datetime.now())

        }

        self.control_history.append(record)

        logging.info(
            f"{device_name} connected"
        )

        return record


    # -----------------------------------------

    def disconnect_device(self, device_name):
        """
        Register device disconnection.
        """

        record = {

            "device": device_name,

            "action": "disconnect",

            "status": "disconnected",

            "time": str(datetime.now())

        }

        self.control_history.append(record)

        logging.info(
            f"{device_name} disconnected"
        )

        return record


    # -----------------------------------------

    def restart_device(self, device_name):
        """
        Device restart foundation.
        """

        record = {

            "device": device_name,

            "action": "restart",

            "status": "restarted",

            "time": str(datetime.now())

        }

        self.control_history.append(record)

        return record


    # -----------------------------------------

    def get_status(self, device_name):
        """
        Return current device status.
        """

        return {

            "device": device_name,

            "status": "available",

            "checked_at": str(datetime.now())

        }


    # -----------------------------------------

    def get_history(self):
        """
        Return control history.
        """

        return self.control_history
    # -----------------------------------------

    def validate_action(self, action):
        """
        Validate supported device actions.
        """

        allowed_actions = [
            "connect",
            "disconnect",
            "restart"
        ]

        return action in allowed_actions


    # -----------------------------------------

    def execute_action(self, device_name, action):
        """
        Execute device action foundation.
        """

        if not self.validate_action(action):

            return {
                "success": False,
                "message": "Invalid action"
            }


        record = {

            "device": device_name,

            "action": action,

            "success": True,

            "time": str(datetime.now())

        }


        self.control_history.append(record)


        logging.info(
            f"Action {action} executed on {device_name}"
        )


        return record



    # -----------------------------------------

    def clear_history(self):
        """
        Clear controller history.
        """

        self.control_history.clear()

        return True



    # -----------------------------------------

    def export_history(self):
        """
        Export device control report.
        """

        return {

            "total_actions": len(
                self.control_history
            ),

            "records": self.control_history

        }



# -----------------------------------------
# Testing
# -----------------------------------------

if __name__ == "__main__":

    controller = DeviceController()


    print(
        controller.connect_device(
            "USB Device"
        )
    )


    print(
        controller.execute_action(
            "USB Device",
            "restart"
        )
    )


    print(
        controller.export_history()
    )
