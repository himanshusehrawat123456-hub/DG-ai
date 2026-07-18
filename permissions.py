"""
DG AI - Permissions Manager
Version: 1.0
"""

import logging
from datetime import datetime


class PermissionManager:

    def __init__(self):
        self.permissions = {}

    def add_permission(self, user, permission):
        self.permissions.setdefault(user, []).append(permission)
        logging.info(f"Permission Added: {user} -> {permission}")

    def remove_permission(self, user, permission):
        if user in self.permissions:
            if permission in self.permissions[user]:
                self.permissions[user].remove(permission)
                logging.info(f"Permission Removed: {user} -> {permission}")

    def check_permission(self, user, permission):
        if user in self.permissions:
            return permission in self.permissions[user]
        return False

    def show_permissions(self):
        print("\n===== DG AI Permissions =====")

        if not self.permissions:
            print("No permissions assigned.")
            return

        for user, perms in self.permissions.items():
            print(f"{user} : {', '.join(perms)}")

    def status(self):
        print("DG AI Permission Manager Ready")
        print("Time:", datetime.now())


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    manager = PermissionManager()

    manager.add_permission("Admin", "Full Access")
    manager.add_permission("User", "Chat")

    manager.show_permissions()

    print(manager.check_permission("Admin", "Full Access"))

    manager.status()
