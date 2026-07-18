"""
DG AI Version 1
Permission Management System

Purpose:
- Manage user permissions
- Control module access
- Provide security foundation

Version: 1.0
"""


class PermissionManager:
    """
    Handles DG AI access permissions.
    """



    def __init__(self):

        self.permissions = {

            "admin": [
                "system_control",
                "file_access",
                "memory_access",
                "settings_access"
            ],

            "user": [
                "chat",
                "basic_commands"
            ]

        }



    def add_role(self, role, permissions):
        """
        Create a new user role.
        """

        self.permissions[role] = permissions


        return True



    def check_permission(self, role, permission):
        """
        Check if role has permission.
        """

        if role in self.permissions:

            return permission in self.permissions[role]


        return False



    def get_permissions(self, role):
        """
        Return role permissions.
        """

        return self.permissions.get(
            role,
            []
        )



    def remove_permission(self, role, permission):
        """
        Remove permission from role.
        """

        if role in self.permissions:

            if permission in self.permissions[role]:

                self.permissions[role].remove(
                    permission
                )

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = PermissionManager()


    print(
        "Admin Permissions:"
    )


    print(
        manager.get_permissions(
            "admin"
        )
    )


    print(
        "\nAccess Check:"
    )


    print(
        manager.check_permission(
            "admin",
            "file_access"
        )
    )
