"""
DG AI Version 1
Email Receiver

Purpose:
- Receive email data
- Store received emails
- Read and manage inbox

Version: 1.0
"""

import logging
from datetime import datetime


class EmailReceiver:
    """
    Professional Email Receiver Manager
    """

    def __init__(self):

        self.inbox = []

        self.read_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def receive_email(
        self,
        sender,
        subject,
        message
    ):
        """
        Receive new email.
        """

        email = {

            "sender": sender,

            "subject": subject,

            "message": message,

            "status": "unread",

            "received_time": str(datetime.now())

        }


        self.inbox.append(
            email
        )


        logging.info(
            "New email received"
        )


        return email


    # ---------------------------------

    def get_inbox(self):
        """
        Return all received emails.
        """

        return self.inbox


    # ---------------------------------

    def read_email(
        self,
        index
    ):
        """
        Read email from inbox.
        """

        try:

            email = self.inbox[index]


            email["status"] = "read"


            self.read_history.append(
                email
            )


            return email


        except IndexError:

            return None


    # ---------------------------------

    def search_email(
        self,
        keyword
    ):
        """
        Search emails.
        """

        results = []


        for email in self.inbox:

            if keyword.lower() in str(email).lower():

                results.append(email)


        return results


    # ---------------------------------

    def delete_email(
        self,
        index
    ):
        """
        Delete email.
        """

        try:

            return self.inbox.pop(index)


        except IndexError:

            return None


    # ---------------------------------

    def get_read_history(self):

        return self.read_history


    # ---------------------------------

    def clear_inbox(self):

        self.inbox.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    receiver = EmailReceiver()


    receiver.receive_email(

        "dg@example.com",

        "Welcome",

        "DG AI Started"

    )


    print(
        receiver.get_inbox()
    )
