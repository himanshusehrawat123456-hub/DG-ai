"""
DG AI Version 1
Notification Management System

Purpose:
- Manage system notifications
- Create alerts and reminders
- Provide notification foundation

Version: 1.0
"""


import datetime



class NotificationManager:
    """
    Handles DG AI notifications.
    """



    def __init__(self):

        self.notifications = []



    def create_notification(self, title, message):
        """
        Create a new notification.
        """

        notification = {

            "id":
            len(self.notifications) + 1,

            "title":
            title,

            "message":
            message,

            "time":
            str(datetime.datetime.now()),

            "status":
            "New"

        }


        self.notifications.append(
            notification
        )


        return notification



    def mark_as_read(self, notification_id):
        """
        Mark notification as read.
        """

        for notification in self.notifications:

            if notification["id"] == notification_id:

                notification["status"] = "Read"

                return True


        return False



    def get_notifications(self):
        """
        Return all notifications.
        """

        return self.notifications



    def clear_notifications(self):
        """
        Clear all notifications.
        """

        self.notifications.clear()


        return True




# Testing

if __name__ == "__main__":


    manager = NotificationManager()


    manager.create_notification(
        "DG AI Alert",
        "System started successfully"
    )


    manager.create_notification(
        "Reminder",
        "Complete Python practice"
    )


    print(
        "DG AI Notifications:"
    )


    for item in manager.get_notifications():

        print(item)
