"""
DG AI Version 1
Plugin Communication Manager

Purpose:
- Manage communication between plugins
- Send and receive plugin messages

Version: 1.0
"""


import datetime



class CommunicationManager:
    """
    Handles plugin communication.
    """



    def __init__(self):

        self.messages = []



    def send_message(self, sender, receiver, message):
        """
        Send message from one plugin to another.
        """

        data = {

            "id":
            len(self.messages) + 1,

            "sender":
            sender,

            "receiver":
            receiver,

            "message":
            message,

            "status":
            "Sent",

            "time":
            str(datetime.datetime.now())

        }


        self.messages.append(data)


        return data



    def receive_message(self, receiver):
        """
        Get messages for a plugin.
        """

        result = []


        for message in self.messages:

            if message["receiver"] == receiver:

                result.append(message)


        return result



    def get_all_messages(self):
        """
        Return all messages.
        """

        return self.messages



    def clear_messages(self):
        """
        Clear all messages.
        """

        self.messages.clear()

        return True




# Testing

if __name__ == "__main__":


    communication = CommunicationManager()


    communication.send_message(
        "Voice_Plugin",
        "Memory_Plugin",
        "Save voice data"
    )


    print(
        communication.get_all_messages()
    )
``
