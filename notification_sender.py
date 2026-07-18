"""
DG AI Version 1
Notification Sender

Purpose:
- Send notifications
- Manage sending status
- Store sending history

Version: 1.0
"""

import logging
from datetime import datetime


class NotificationSender:
    """
    Professional Notification Sender
    """

    def __init__(self):

        self.send_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_notification(
        self,
        title,
        message,
        user="default"
    ):
        """
        Create notification object.
        """

        notification = {

            "user": user,

            "title": title,

            "message": message,

            "created_at": str(datetime.now())

        }

        return notification


    # ---------------------------------

    def send(
        self,
        notification
    ):
        """
        Send notification foundation.
        """

        record = {

            "notification": notification,

            "status": "sent",

            "sent_at": str(datetime.now())

        }


        self.send_history.append(
            record
        )


        logging.info(
            "Notification sent"
        )


        return record


    # ---------------------------------

    def send_bulk(
        self,
        notifications
    ):
        """
        Send multiple notifications.
        """

        results = []


        for item in notifications:

            results.append(
                self.send(item)
            )


        return results


    # ---------------------------------

    def get_status(
        self,
        notification
    ):
        """
        Check notification status.
        """

        return {

            "notification": notification,

            "status": "ready"

        }


    # ---------------------------------

    def get_history(self):
        """
        Return sending history.
        """

        return self.send_history


    # ---------------------------------

    def clear_history(self):
        """
        Clear send records.
        """

        self.send_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    sender = NotificationSender()


    note = sender.create_notification(
        "DG AI",
        "System Started"
    )


    print(
        sender.send(note)
    )
