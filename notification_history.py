"""
DG AI Version 1
Notification History System

Purpose:
- Store notification history
- Manage previous notifications

Version: 1.0
"""


import datetime



class NotificationHistory:
    """
    Handles notification history.
    """



    def __init__(self):

        self.history = []



    def add_notification(self, notification_type, message):
        """
        Add notification record.
        """

        record = {

            "id":
            len(self.history) + 1,

            "type":
            notification_type,

            "message":
            message,

            "time":
            str(datetime.datetime.now())

        }


        self.history.append(record)


        return record



    def get_history(self):
        """
        Return notification history.
        """

        return self.history



    def delete_notification(self, notification_id):
        """
        Delete notification record.
        """

        for item in self.history:

            if item["id"] == notification_id:

                self.history.remove(item)

                return True


        return False



    def clear_history(self):
        """
        Clear all history.
        """

        self.history.clear()

        return True




# Testing

if __name__ == "__main__":


    history = NotificationHistory()


    history.add_notification(
        "Email",
        "Welcome to DG AI"
    )


    print(
        history.get_history()
    )
