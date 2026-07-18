"""
DG AI Version 1
API Security

Purpose:
- Manage API keys
- Validate access
- Protect API information

Version: 1.0
"""

import hashlib
import logging
from datetime import datetime


class APISecurity:
    """
    Professional API Security Manager
    """

    def __init__(self):

        self.keys = {}

        self.security_logs = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def generate_key(
        self,
        name
    ):
        """
        Generate secure API key.
        """

        raw_key = (
            name +
            str(datetime.now())
        )


        api_key = hashlib.sha256(
            raw_key.encode()
        ).hexdigest()


        self.keys[name] = api_key


        self.log_action(
            "Key Generated"
        )


        return api_key


    # ---------------------------------

    def validate_key(
        self,
        name,
        key
    ):
        """
        Validate API key.
        """

        if name in self.keys:

            return self.keys[name] == key


        return False


    # ---------------------------------

    def remove_key(
        self,
        name
    ):
        """
        Remove API key.
        """

        if name in self.keys:

            del self.keys[name]

            self.log_action(
                "Key Removed"
            )

            return True


        return False


    # ---------------------------------

    def log_action(
        self,
        action
    ):

        self.security_logs.append({

            "action": action,

            "time": str(datetime.now())

        })


    # ---------------------------------

    def get_logs(self):

        return self.security_logs



if __name__ == "__main__":

    security = APISecurity()

    key = security.generate_key(
        "DG_AI"
    )

    print(key)

    print(
        security.validate_key(
            "DG_AI",
            key
        )
    )
