"""
DG AI Version 1
File Encryptor

Purpose:
- Encrypt and decrypt files
- Protect important data
- Maintain encryption history

Version: 1.0
"""

import os
import hashlib
import logging
from datetime import datetime


class FileEncryptor:
    """
    Professional File Encryption Manager
    """

    def __init__(self):

        self.history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def generate_key(
        self,
        password
    ):
        """
        Generate encryption key.
        """

        key = hashlib.sha256(
            password.encode()
        ).digest()


        return key


    # ---------------------------------

    def encrypt_file(
        self,
        file_path,
        password
    ):
        """
        Encrypt file data.
        """

        try:

            if not os.path.exists(file_path):

                return {
                    "success": False,
                    "message": "File not found"
                }


            key = self.generate_key(
                password
            )


            with open(
                file_path,
                "rb"
            ) as file:

                data = file.read()


            encrypted = bytes(
                [
                    data[i] ^ key[i % len(key)]
                    for i in range(len(data))
                ]
            )


            output = file_path + ".enc"


            with open(
                output,
                "wb"
            ) as file:

                file.write(encrypted)


            record = {

                "action": "encrypt",

                "file": file_path,

                "output": output,

                "time": str(datetime.now())

            }


            self.history.append(
                record
            )


            return record


        except Exception as error:

            return {

                "success": False,

                "error": str(error)

            }


    # ---------------------------------

    def decrypt_file(
        self,
        file_path,
        password
    ):
        """
        Decrypt encrypted file.
        """

        try:

            key = self.generate_key(
                password
            )


            with open(
                file_path,
                "rb"
            ) as file:

                data = file.read()


            decrypted = bytes(
                [
                    data[i] ^ key[i % len(key)]
                    for i in range(len(data))
                ]
            )


            output = file_path.replace(
                ".enc",
                ".dec"
            )


            with open(
                output,
                "wb"
            ) as file:

                file.write(decrypted)


            record = {

                "action": "decrypt",

                "file": file_path,

                "output": output,

                "time": str(datetime.now())

            }


            self.history.append(
                record
            )


            return record


        except Exception as error:

            return {

                "success": False,

                "error": str(error)

            }


    # ---------------------------------

    def get_history(self):

        return self.history


    # ---------------------------------

    def clear_history(self):

        self.history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    encryptor = FileEncryptor()

    print(
        encryptor.generate_key(
            "DG_AI"
        )
    )
