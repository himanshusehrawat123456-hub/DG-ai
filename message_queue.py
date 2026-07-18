"""
DG AI Version 1
Message Queue System

Purpose:
- Manage message queue
- Process messages in order

Version: 1.0
"""


import datetime



class MessageQueue:
    """
    Handles message queue operations.
    """



    def __init__(self):

        self.queue = []



    def add_message(self, user, message):
        """
        Add message to queue.
        """

        data = {

            "id":
            len(self.queue) + 1,

            "user":
            user,

            "message":
            message,

            "status":
            "waiting",

            "time":
            str(datetime.datetime.now())

        }


        self.queue.append(data)


        return True



    def get_next_message(self):
        """
        Get next message from queue.
        """

        if len(self.queue) > 0:

            return self.queue.pop(0)


        return None



    def get_queue(self):
        """
        Return current queue.
        """

        return self.queue



    def clear_queue(self):
        """
        Clear all messages.
        """

        self.queue.clear()

        return True




# Testing

if __name__ == "__main__":


    queue = MessageQueue()


    queue.add_message(
        "User",
        "Hello DG AI"
    )


    print(
        queue.get_next_message()
    )
