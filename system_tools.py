"""
DG AI Version 1
System Tool

Purpose:
- Provide basic system information
- System operations foundation

Version: 1.0
"""


import platform
import datetime



class SystemTool:
    """
    Handles system information operations.
    """



    def get_system_info(self):
        """
        Return system details.
        """

        info = {

            "system":
            platform.system(),

            "release":
            platform.release(),

            "version":
            platform.version(),

            "processor":
            platform.processor(),

            "time":
            str(datetime.datetime.now())

        }


        return info



    def get_platform(self):
        """
        Return complete platform information.
        """

        return platform.platform()




# Testing

if __name__ == "__main__":


    system = SystemTool()


    print(
        system.get_system_info()
    )


    print(
        system.get_platform()
    )
