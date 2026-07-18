"""
DG AI Version 1
Security Management System

Purpose:
- Handle basic security checks
- Manage user verification
- Provide security foundation

Version: 1.0
"""


import hashlib
import datetime



class SecurityManager:
    """
    Controls DG AI security operations.
    """



    def __init__(self):

        self.system_name = "DG AI Security"



    def create_password_hash(self, password):
        """
        Convert password into secure hash.

        Parameters:
            password (str)

        Returns:
            hashed password
        """


        if not isinstance(password, str):

            raise TypeError(
                "Password must be string"
            )


        return hashlib.sha256(
            password.encode()
        ).hexdigest()



    def verify_password(self, password, stored_hash):
        """
        Verify password with saved hash.
        """

        password_hash = (
            self.create_password_hash(password)
        )


        return password_hash == stored_hash



    def security_status(self):
        """
        Return security status.
        """

        return {

            "system":
            self.system_name,

            "status":
            "Active",

            "time":
            str(datetime.datetime.now())

        }



# Testing

if __name__ == "__main__":


    security = SecurityManager()


    password = "DG_AI_Test"


    hashed = (
        security.create_password_hash(password)
    )


    print(
        "Password Hash:"
    )

    print(hashed)



    print(
        "\nVerification:"
    )


    print(
        security.verify_password(
            password,
            hashed
        )
    )


    print(
        "\nSecurity Status:"
    )

    print(
        security.security_status()
    )
