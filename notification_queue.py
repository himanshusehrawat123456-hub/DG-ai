"""
DG AI Version 1
Notification Queue

Purpose:
- Manage pending notifications
- Store waiting messages
- Process notification queue

Version: 1.0
"""

import logging
from datetime import datetime


class NotificationQueue:
    """
    Professional Notification Queue Manager
    """

    def __init__(self):

        self.queue = []

        self.processed = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def add_notification(
        self,
        notification
    ):
        """
        Add notification to queue.
        """

        item = {

            "notification": notification,

            "status": "pending",

            "added_time": str(datetime.now())

        }


        self.queue.append(item)


        logging.info(
            "Notification added to queue"
        )


        return item


    # ---------------------------------

    def get_next(self):
        """
        Get next pending notification.
        """

        if len(self.queue) == 0:

            return None


        return self.queue[0]


    # ---------------------------------

    def process_next(self):
        """
        Process first notification.
        """

        if len(self.queue) == 0:

            return None


        item = self.queue.pop(0)


        item["status"] = "processed"

        item["processed_time"] = str(
            datetime.now()
        )


        self.processed.append(item)


        logging.info(
            "Notification processed"
        )


        return item


    # ---------------------------------

    def remove_notification(
        self,
        index
    ):
        """
        Remove notification from queue.
        """

        try:

            return self.queue.pop(index)


        except IndexError:

            return None


    # ---------------------------------

    def get_queue(self):
        """
        Return pending notifications.
        """

        return self.queue


    # ---------------------------------

    def get_processed(self):
        """
        Return processed notifications.
        """

        return self.processed


    # ---------------------------------

    def clear_queue(self):
        """
        Clear pending queue.
        """

        self.queue.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    queue = NotificationQueue()


    queue.add_notification(
        {
            "message":
            "DG AI Started"
        }
    )


    print(
        queue.process_next()
    )
