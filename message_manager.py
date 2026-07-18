"""
DG AI Version 1
Message Manager System

Purpose:
- Manage messages
- Store and retrieve communication data

Version: 1.0
"""


import datetime



class MessageManager:
    """
    Handles message operations.
    """



    def __init__(self):

        self.messages = []



    def send_message(self, sender, receiver, content):
        """
        Create and store message.
        """

        message = {

            "id":
            len(self.messages) + 1,

            "sender":
            sender,

            "receiver":
            receiver,

            "content":
            content,

            "time":
            str(datetime.datetime.now())

        }


        self.messages.append(message)


        return message



    def get_messages(self):
        """
        Return all messages.
        """

        return self.messages



    def delete_message(self, message_id):
        """
        Delete message by id.
        """

        for message in self.messages:

            if message["id"] == message_id:

                self.messages.remove(message)

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = MessageManager()


    manager.send_message(
        "User",
        "DG AI",
        "Hello AI"
    )


    print(
        manager.get_messages()
    )
