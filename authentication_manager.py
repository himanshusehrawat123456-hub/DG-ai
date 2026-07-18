"""
DG AI Version 1
Authentication Management System

Purpose:
- Manage user authentication
- Verify user credentials
- Provide security foundation

Version: 1.0
"""


import json
import os
import hashlib



class AuthenticationManager:
    """
    Handles DG AI authentication.
    """



    def __init__(self, file_path="data/users.json"):

        self.file_path = file_path

        self.users = {}

        self._create_storage()

        self._load_users()



    def _create_storage(self):
        """
        Create user storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def _hash_password(self, password):
        """
        Convert password into secure hash.
        """

        return hashlib.sha256(
            password.encode()
        ).hexdigest()



    def register_user(self, username, password):
        """
        Register new user.
        """

        if username in self.users:

            return False


        self.users[username] = {

            "password":
            self._hash_password(password)

        }


        self._save_users()


        return True



    def login(self, username, password):
        """
        Verify user login.
        """

        if username not in self.users:

            return False


        stored_password = (
            self.users[username]["password"]
        )


        return (
            stored_password ==
            self._hash_password(password)
        )



    def remove_user(self, username):
        """
        Remove user account.
        """

        if username in self.users:

            del self.users[username]

            self._save_users()

            return True


        return False



    def _save_users(self):
        """
        Save user data.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.users,
                file,
                indent=4
            )



    def _load_users(self):
        """
        Load users.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.users = json.load(file)




# Testing

if __name__ == "__main__":


    auth = AuthenticationManager()


    auth.register_user(
        "DG_User",
        "password123"
    )


    print(
        auth.login(
            "DG_User",
            "password123"
        )
    )
