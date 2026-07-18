"""
DG AI Version 1
Update Installer System

Purpose:
- Install DG AI updates
- Keep installation history

Version: 1.0
"""


import datetime



class UpdateInstaller:
    """
    Handles update installation.
    """



    def __init__(self):

        self.install_history = []



    def install_update(self, version):
        """
        Install update.
        """

        record = {

            "id":
            len(self.install_history) + 1,

            "version":
            version,

            "status":
            "Installed",

            "installed_at":
            str(datetime.datetime.now())

        }


        self.install_history.append(record)

        return record



    def get_install_history(self):
        """
        Return installation history.
        """

        return self.install_history



    def rollback_update(self, version):
        """
        Roll back an installed update.
        """

        return {

            "version":
            version,

            "status":
            "Rolled Back",

            "time":
            str(datetime.datetime.now())

        }



# Testing

if __name__ == "__main__":

    installer = UpdateInstaller()

    print(
        installer.install_update(
            "1.1.0"
        )
    )

    print(
        installer.get_install_history()
    )
