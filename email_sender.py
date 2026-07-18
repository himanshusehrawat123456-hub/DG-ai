"""
DG AI Version 1
Email Sender

Purpose:
- Create and send emails
- Manage email sending history
- Provide email service foundation

Version: 1.0
"""

import logging
from datetime import datetime


class EmailSender:
    """
    Professional Email Sending Manager
    """

    def __init__(self):

        self.sent_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_email(
        self,
        receiver,
        subject,
        message
    ):
        """
        Create email structure.
        """

        email = {

            "receiver": receiver,

            "subject": subject,

            "message": message,

            "created_time": str(datetime.now())

        }


        return email


    # ---------------------------------

    def validate_email_data(
        self,
        email
    ):
        """
        Check required email fields.
        """

        required = [

            "receiver",

            "subject",

            "message"

        ]


        for field in required:

            if field not in email:

                return False


        return True


    # ---------------------------------

    def send_email(
        self,
        email
    ):
        """
        Send email foundation.
        """

        if not self.validate_email_data(email):

            return {

                "status": "failed",

                "message": "Invalid email data"

            }


        record = {

            "email": email,

            "status": "sent",

            "sent_time": str(datetime.now())

        }


        self.sent_history.append(
            record
        )


        logging.info(
            "Email sent successfully"
        )


        return record


    # ---------------------------------

    def send_multiple(
        self,
        emails
    ):
        """
        Send multiple emails.
        """

        results = []


        for email in emails:

            results.append(
                self.send_email(email)
            )


        return results


    # ---------------------------------

    def get_history(self):
        """
        Return sent emails.
        """

        return self.sent_history


    # ---------------------------------

    def clear_history(self):
        """
        Clear email history.
        """

        self.sent_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    sender = EmailSender()


    mail = sender.create_email(

        "user@example.com",

        "DG AI Test",

        "System Started"

    )


    print(
        sender.send_email(mail)
    )
