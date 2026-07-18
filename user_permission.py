"""
DG AI Version 1
User Permission

Purpose:
- Manage user roles
- Control user permissions
- Provide access checking

Version: 1.0
"""

import logging
from datetime import datetime


class UserPermission:
    """
    Professional User Permission Manager
    """

    def __init__(self):

        self.roles = {}

        self.permission_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_role(
        self,
        user_id,
        role="user"
    ):
        """
        Create user role.
        """

        self.roles[user_id] = {

            "role": role,

            "permissions": [],

            "created":
            str(datetime.now())

        }


        self.log_action(
            user_id,
            "Role Created"
        )


        return self.roles[user_id]


    # ---------------------------------

    def add_permission(
        self,
        user_id,
        permission
    ):
        """
        Add permission to user.
        """

        if user_id not in self.roles:

            return False


        self.roles[user_id]["permissions"].append(
            permission
        )


        self.log_action(
            user_id,
            f"Permission Added: {permission}"
        )


        return True


    # ---------------------------------

    def remove_permission(
        self,
        user_id,
        permission
    ):
        """
        Remove permission.
        """

        if user_id in self.roles:

            if permission in self.roles[user_id]["permissions"]:

                self.roles[user_id]["permissions"].remove(
                    permission
                )

                return True


        return False


    # ---------------------------------

    def check_permission(
        self,
        user_id,
        permission
    ):
        """
        Check user access.
        """

        if user_id not in self.roles:

            return False


        return permission in self.roles[user_id]["permissions"]


    # ---------------------------------

    def get_user_role(
        self,
        user_id
    ):
        """
        Return user role.
        """

        return self.roles.get(
            user_id
        )


    # ---------------------------------

    def log_action(
        self,
        user_id,
        action
    ):

        self.permission_history.append({

            "user_id": user_id,

            "action": action,

            "time": str(datetime.now())

        })


    # ---------------------------------

    def get_history(self):

        return self.permission_history


    # ---------------------------------

    def clear_history(self):

        self.permission_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    permission = UserPermission()


    permission.create_role(
        1,
        "admin"
    )


    permission.add_permission(
        1,
        "manage_system"
    )


    print(
        permission.get_user_role(1)
    )
