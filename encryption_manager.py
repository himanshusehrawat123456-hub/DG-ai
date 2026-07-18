"""
DG AI Version 1
Encryption Management System

Purpose:
- Encrypt sensitive information
- Decrypt protected data
- Provide security foundation

Version: 1.0
"""


import base64



class EncryptionManager:
    """
    Handles DG AI data encryption.
    """



    def __init__(self):

        self.status = "Ready"



    def encrypt(self, text):
        """
        Encrypt text data.
        """

        if not isinstance(text, str):

            raise TypeError(
                "Input must be text"
            )


        encoded = base64.b64encode(
            text.encode("utf-8")
        )


        return encoded.decode("utf-8")



    def decrypt(self, encrypted_text):
        """
        Decrypt protected text.
        """

        decoded = base64.b64decode(
            encrypted_text
        )


        return decoded.decode("utf-8")



    def get_status(self):
        """
        Return encryption status.
        """

        return {

            "module":
            "Encryption Manager",

            "status":
            self.status

        }




# Testing

if __name__ == "__main__":


    security = EncryptionManager()


    message = "DG AI Secure Data"


    encrypted = security.encrypt(
        message
    )


    print(
        "Encrypted:"
    )

    print(encrypted)


    print(
        "\nDecrypted:"
    )

    print(
        security.decrypt(
            encrypted
        )
    )


    print(
        security.get_status()
    )
