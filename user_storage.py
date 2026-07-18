"""
DG AI Version 1
User Storage

Purpose:
- Store user information
- Manage user records
- Provide user data access

Version: 1.0
"""

import logging
from datetime import datetime


class UserStorage:

    def __init__(self):

        self.users = {}

        logging.basicConfig(
            level=logging.INFO
        )


    def add_user(
        self,
        user_id,
        data
    ):

        self.users[user_id] = {

            "data": data,

            "created":
            str(datetime.now())

        }

        return True


    def get_user(
        self,
        user_id
    ):

        return self.users.get(
            user_id
        )


    def update_user(
        self,
        user_id,
        data
    ):

        if user_id in self.users:

            self.users[user_id]["data"] = data

            self.users[user_id]["updated"] = str(
                datetime.now()
            )

            return True

        return False


    def delete_user(
        self,
        user_id
    ):

        if user_id in self.users:

            del self.users[user_id]

            return True

        return False


    def get_all_users(self):

        return self.users


    def clear_storage(self):

        self.users.clear()

        return True



if __name__ == "__main__":

    storage = UserStorage()

    storage.add_user(
        1,
        {
            "name": "Himanshu"
        }
    )

    print(
        storage.get_user(1)
    )
