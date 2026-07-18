"""
DG AI Version 1
Machine Tools System

Purpose:
- Manage machine information
- Provide system interaction foundation

Version: 1.0
"""


import platform
import datetime



class MachineTools:
    """
    Handles DG AI machine operations.
    """



    def __init__(self):

        self.history = []



    def get_system_info(self):
        """
        Get basic system information.
        """

        info = {

            "system":
            platform.system(),

            "machine":
            platform.machine(),

            "processor":
            platform.processor(),

            "time":
            str(datetime.datetime.now())

        }


        self.history.append(info)


        return info



    def add_command_log(self, command, status):
        """
        Store machine command history.
        """

        log = {

            "command":
            command,

            "status":
            status,

            "time":
            str(datetime.datetime.now())

        }


        self.history.append(log)


        return True



    def get_history(self):
        """
        Return machine history.
        """

        return self.history




# Testing

if __name__ == "__main__":


    machine = MachineTools()


    print(
        machine.get_system_info()
    )


    machine.add_command_log(
        "System Check",
        "Completed"
    )


    print(
        machine.get_history()
    )
