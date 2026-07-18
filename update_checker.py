"""
DG AI Version 1
Update Checker System

Purpose:
- Check for available updates
- Compare current and latest versions

Version: 1.0
"""


import datetime



class UpdateChecker:
    """
    Handles update checking.
    """



    def __init__(self):

        self.current_version = "1.0.0"

        self.latest_version = "1.0.0"



    def set_latest_version(self, version):
        """
        Set latest available version.
        """

        self.latest_version = version



    def check_for_updates(self):
        """
        Check if update is available.
        """

        return {

            "current_version": self.current_version,

            "latest_version": self.latest_version,

            "update_available":
            self.current_version != self.latest_version,

            "checked_at":
            str(datetime.datetime.now())

        }



# Testing

if __name__ == "__main__":

    checker = UpdateChecker()

    checker.set_latest_version("1.1.0")

    print(checker.check_for_updates())
