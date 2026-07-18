"""
DG AI Version 1
Access Control System

Purpose:
- Manage user access
- Control module permissions

Version: 1.0
"""


import datetime



class AccessControl:
    """
    Handles access control operations.
    """



    def __init__(self):

        self.permissions = {}



    def create_role(self, role_name, permissions):
        """
        Create new role.
        """

        self.permissions[role_name] = {

            "permissions":
            permissions,

            "created":
            str(datetime.datetime.now())

        }


        return True



    def check_permission(self, role_name, permission):
        """
        Check role permission.
        """

        if role_name in self.permissions:

            if permission in self.permissions[role_name]["permissions"]:

                return True


        return False



    def get_roles(self):
        """
        Return all roles.
        """

        return self.permissions




# Testing

if __name__ == "__main__":


    access = AccessControl()


    access.create_role(
        "Admin",
        [
            "AI Core",
            "Database",
            "Tools"
        ]
    )


    print(
        access.check_permission(
            "Admin",
            "AI Core"
        )
    )


    print(
        access.get_roles()
    )
