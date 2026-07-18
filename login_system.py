"""
DG AI Version 1
Login System

Purpose:
- Handle user login
- Verify user credentials

Version: 1.0
"""


import datetime



class LoginSystem:
    """
    Handles login operations.
    """



    def __init__(self):

        self.users = []

        self.login_history = []



    def register_user(self, username, password):
        """
        Register new user.
        """

        user = {

            "id":
            len(self.users) + 1,

            "username":
            username,

            "password":
            password

        }


        self.users.append(user)


        return True



    def login(self, username, password):
        """
        Verify user login.
        """

        for user in self.users:

            if (
                user["username"] == username
                and user["password"] == password
            ):

                self.login_history.append({

                    "username":
                    username,

                    "status":
                    "Success",

                    "time":
                    str(datetime.datetime.now())

                })


                return True


        self.login_history.append({

            "username":
            username,

            "status":
            "Failed",

            "time":
            str(datetime.datetime.now())

        })


        return False



    def get_login_history(self):
        """
        Return login history.
        """

        return self.login_history




# Testing

if __name__ == "__main__":


    login = LoginSystem()


    login.register_user(
        "Himanshu",
        "12345"
    )


    print(
        login.login(
            "Himanshu",
            "12345"
        )
    )
