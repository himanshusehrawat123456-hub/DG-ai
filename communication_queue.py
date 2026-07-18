"""
DG AI Version 1
Communication Queue System

Purpose:
- Manage plugin message queue
- Process pending messages

Version: 1.0
"""


import datetime



class CommunicationQueue:
    """
    Handles communication queue operations.
    """



    def __init__(self):

        self.queue = []



    def add_to_queue(self, message):
        """
        Add message to queue.
        """

        item = {

            "id":
            len(self.queue) + 1,

            "message":
            message,

            "status":
            "Pending",

            "time":
            str(datetime.datetime.now())

        }


        self.queue.append(item)


        return item



    def process_message(self):
        """
        Process first pending message.
        """

        if len(self.queue) > 0:

            message = self.queue.pop(0)

            message["status"] = "Processed"

            return message


        return None



    def get_queue(self):
        """
        Return current queue.
        """

        return self.queue



    def clear_queue(self):
        """
        Clear queue.
        """

        self.queue.clear()

        return True




# Testing

if __name__ == "__main__":


    queue = CommunicationQueue()


    queue.add_to_queue(
        "Plugin Data Request"
    )


    print(
        queue.process_message()
    )
