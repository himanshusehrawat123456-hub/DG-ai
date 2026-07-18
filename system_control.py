"""
DG AI Version 1
System Control Module

Purpose:
- Manage basic system level operations
- Provide foundation for future OS interaction
- Handle system information

Version: 1.0
"""


import platform
import datetime


class SystemController:
    """
    Controls and manages DG AI system operations.
    """


    def __init__(self):
        """
        Initialize system controller.
        """

        self.system_name = "DG AI"



    def get_system_info(self):
        """
        Returns basic system information.
        """

        info = {

            "system": self.system_name,

            "platform":
            platform.system(),

            "processor":
            platform.processor(),

            "architecture":
            platform.architecture()[0],

            "time":
            str(datetime.datetime.now())

        }

        return info



    def check_status(self):
        """
        Check DG AI system status.
        """

        return {
            "status": "Online",
            "message": "DG AI System Running"
        }



    def shutdown_message(self):
        """
        Future shutdown control foundation.
        """

        return "System shutdown command received"



# Module Testing

if __name__ == "__main__":


    system = SystemController()


    print("\nDG AI System Information")
    print("------------------------")


    details = system.get_system_info()


    for key, value in details.items():

        print(f"{key}: {value}")



    print("\nStatus:")

    print(
        system.check_status()
    )
