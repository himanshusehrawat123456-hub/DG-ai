"""
DG AI Version 1
Email Notification System

Purpose:
- Manage email notifications
- Store email notification records

Version: 1.0
"""


import datetime



class EmailNotification:
    """
    Handles email notification operations.
    """



    def __init__(self):

        self.emails = []



    def send_email(self, receiver, subject, message):
        """
        Create email notification record.
        """

        email = {

            "id":
            len(self.emails) + 1,

            "receiver":
            receiver,

            "subject":
            subject,

            "message":
            message,

            "status":
            "Sent",

            "time":
            str(datetime.datetime.now())

        }


        self.emails.append(email)


        return email



    def get_emails(self):
        """
        Return email history.
        """

        return self.emails



    def clear_emails(self):
        """
        Clear email records.
        """

        self.emails.clear()

        return True




# Testing

if __name__ == "__main__":


    email = EmailNotification()


    print(
        email.send_email(
            "user@example.com",
            "Welcome",
            "Welcome to DG AI"
        )
    )
