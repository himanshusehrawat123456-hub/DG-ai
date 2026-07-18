"""
DG AI Version 1
File Permission Checker

Purpose:
- Check file access permissions
- Validate user access
- Provide permission status

Version: 1.0
"""

import logging
from datetime import datetime


class FilePermissionChecker:
    """
    Professional File Permission Checker
    """

    def __init__(self):

        self.permissions = {}

        self.check_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def set_permission(
        self,
        user_id,
        file_name,
        permission
    ):
        """
        Set user file permission.
        """

        if user_id not in self.permissions:

            self.permissions[user_id] = {}


        self.permissions[user_id][file_name] = permission


        return True


    # ---------------------------------

    def check_permission(
        self,
        user_id,
        file_name,
        required_permission
    ):
        """
        Check access permission.
        """

        user_permissions = self.permissions.get(
            user_id,
            {}
        )


        current_permission = user_permissions.get(
            file_name
        )


        result = current_permission == required_permission


        self.check_history.append({

            "user":
            user_id,

            "file":
            file_name,

            "permission":
            required_permission,

            "result":
            result,

            "time":
            str(datetime.now())

        })


        return result


    # ---------------------------------

    def get_user_permissions(
        self,
        user_id
    ):

        return self.permissions.get(
            user_id,
            {}
        )


    # ---------------------------------

    def remove_permission(
        self,
        user_id,
        file_name
    ):

        if user_id in self.permissions:

            if file_name in self.permissions[user_id]:

                del self.permissions[user_id][file_name]

                return True


        return False


    # ---------------------------------

    def get_check_history(self):

        return self.check_history


    # ---------------------------------

    def clear_history(self):

        self.check_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    checker = FilePermissionChecker()


    checker.set_permission(
        1,
        "report.pdf",
        "read"
    )


    print(
        checker.check_permission(
            1,
            "report.pdf",
            "read"
        )
    )
