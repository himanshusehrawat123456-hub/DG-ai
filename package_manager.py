"""
DG AI Version 1
Package Management System

Purpose:
- Manage DG AI packages
- Register installed packages
- Track package status

Version: 1.0
"""


import datetime



class PackageManager:
    """
    Handles DG AI package operations.
    """



    def __init__(self):

        self.packages = []



    def install_package(self, name, version):
        """
        Register a package.
        """

        package = {

            "id":
            len(self.packages) + 1,

            "name":
            name,

            "version":
            version,

            "status":
            "Installed",

            "installed_time":
            str(datetime.datetime.now())

        }


        self.packages.append(package)


        return package



    def remove_package(self, package_id):
        """
        Remove package.
        """

        for package in self.packages:

            if package["id"] == package_id:

                self.packages.remove(package)

                return True


        return False



    def get_packages(self):
        """
        Return all packages.
        """

        return self.packages



    def check_package(self, name):
        """
        Check package availability.
        """

        for package in self.packages:

            if package["name"] == name:

                return package


        return None




# Testing

if __name__ == "__main__":


    manager = PackageManager()


    manager.install_package(
        "Python",
        "3.x"
    )


    manager.install_package(
        "AI Engine",
        "1.0"
    )


    print(
        "DG AI Packages:"
    )


    print(
        manager.get_packages()
    )
