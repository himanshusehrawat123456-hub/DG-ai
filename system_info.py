"""
DG AI Version 1
System Information Module

Purpose:
- Collect system information
- Provide environment details
- Create hardware awareness foundation

Version: 1.0
"""


import platform
import sys
import datetime



class SystemInfo:
    """
    Handles DG AI system information.
    """



    def __init__(self):

        self.name = "DG AI"



    def get_info(self):
        """
        Return system information.
        """

        info = {

            "AI_Name":
            self.name,

            "Operating_System":
            platform.system(),

            "OS_Version":
            platform.version(),

            "Machine":
            platform.machine(),

            "Processor":
            platform.processor(),

            "Python_Version":
            sys.version,

            "Time":
            str(datetime.datetime.now())

        }


        return info



    def get_platform(self):
        """
        Return platform name.
        """

        return platform.system()



    def get_python_version(self):
        """
        Return Python version.
        """

        return sys.version




# Testing

if __name__ == "__main__":


    system = SystemInfo()


    print(
        "DG AI System Information:"
    )


    print(
        system.get_info()
    )
