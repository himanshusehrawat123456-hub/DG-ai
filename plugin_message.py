"""
DG AI Version 1
Plugin Message System

Purpose:
- Create and manage plugin messages
- Store message details

Version: 1.0
"""


import datetime



class PluginMessage:
    """
    Handles plugin message creation.
    """



    def __init__(self):

        self.messages = []



    def create_message(self, sender, receiver, content):
        """
        Create new plugin message.
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

            "status":
            "Created",

            "time":
            str(datetime.datetime.now())

        }


        self.messages.append(message)


        return message



    def update_status(self, message_id, status):
        """
        Update message status.
        """

        for message in self.messages:

            if message["id"] == message_id:

                message["status"] = status

                return True


        return False



    def get_messages(self):
        """
        Return all messages.
        """

        return self.messages




# Testing

if __name__ == "__main__":


    msg = PluginMessage()


    print(
        msg.create_message(
            "Plugin_A",
            "Plugin_B",
            "Data Request"
        )
    )
