"""
DG AI Version 1
Version Management System

Purpose:
- Manage DG AI versions
- Track updates
- Maintain version history

Version: 1.0
"""



import datetime



class VersionManager:
    """
    Handles DG AI version operations.
    """



    def __init__(self):

        self.current_version = "1.0"

        self.history = []



    def get_current_version(self):
        """
        Return current DG AI version.
        """

        return self.current_version



    def add_version(self, version, description):
        """
        Add new version record.
        """

        data = {

            "version":
            version,

            "description":
            description,

            "date":
            str(datetime.datetime.now())

        }


        self.history.append(data)


        self.current_version = version


        return True



    def get_history(self):
        """
        Return version history.
        """

        return self.history



    def compare_version(self, version):
        """
        Compare version.
        """

        if version == self.current_version:

            return "Current Version"


        return "Different Version"




# Testing

if __name__ == "__main__":


    manager = VersionManager()


    print(
        "Current:",
        manager.get_current_version()
    )


    manager.add_version(
        "1.1",
        "Added security updates"
    )


    print(
        manager.get_history()
    )
