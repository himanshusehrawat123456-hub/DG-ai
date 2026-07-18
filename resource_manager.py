"""
DG AI Version 1
Resource Management System

Purpose:
- Manage DG AI resources
- Track available modules and files
- Provide resource control foundation

Version: 1.0
"""


import datetime



class ResourceManager:
    """
    Handles DG AI resource operations.
    """



    def __init__(self):

        self.resources = []



    def add_resource(self, name, resource_type):
        """
        Register a new resource.
        """

        resource = {

            "id":
            len(self.resources) + 1,

            "name":
            name,

            "type":
            resource_type,

            "status":
            "Available",

            "created":
            str(datetime.datetime.now())

        }


        self.resources.append(resource)


        return resource



    def get_resources(self):
        """
        Return all resources.
        """

        return self.resources



    def find_resource(self, name):
        """
        Search resource by name.
        """

        for resource in self.resources:

            if resource["name"] == name:

                return resource


        return None



    def remove_resource(self, resource_id):
        """
        Remove a resource.
        """

        for resource in self.resources:

            if resource["id"] == resource_id:

                self.resources.remove(resource)

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = ResourceManager()


    manager.add_resource(
        "AI Core",
        "Module"
    )


    manager.add_resource(
        "Memory Database",
        "Storage"
    )


    print(
        "DG AI Resources:"
    )


    print(
        manager.get_resources()
    )
