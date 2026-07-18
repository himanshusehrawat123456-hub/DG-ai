"""
DG AI Version 1
Password Management System

Purpose:
- Manage passwords securely
- Hash passwords
- Verify passwords

Version: 1.0
"""


import hashlib
import json
import os



class PasswordManager:
    """
    Handles DG AI password operations.
    """



    def __init__(self, file_path="data/passwords.json"):

        self.file_path = file_path

        self.passwords = {}

        self._create_storage()

        self._load_passwords()



    def _create_storage(self):
        """
        Create storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def _hash_password(self, password):
        """
        Convert password into hash.
        """

        return hashlib.sha256(
            password.encode()
        ).hexdigest()



    def save_password(self, username, password):
        """
        Save user password securely.
        """

        self.passwords[username] = (
            self._hash_password(password)
        )

        self._save_passwords()


        return True



    def verify_password(self, username, password):
        """
        Verify password.
        """

        if username not in self.passwords:

            return False


        return (
            self.passwords[username]
            ==
            self._hash_password(password)
        )



    def remove_password(self, username):
        """
        Remove password record.
        """

        if username in self.passwords:

            del self.passwords[username]

            self._save_passwords()

            return True


        return False



    def _save_passwords(self):
        """
        Save password data.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.passwords,
                file,
                indent=4
            )



    def _load_passwords(self):
        """
        Load password data.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.passwords = json.load(file)




# Testing

if __name__ == "__main__":


    manager = PasswordManager()


    manager.save_password(
        "DG_User",
        "secure123"
    )


    print(
        manager.verify_password(
            "DG_User",
            "secure123"
        )
    )
