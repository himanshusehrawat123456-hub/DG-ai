"""
DG AI Version 1
Chat Manager System

Purpose:
- Manage chat sessions
- Handle conversation history

Version: 1.0
"""


import datetime



class ChatManager:
    """
    Handles chat operations.
    """



    def __init__(self):

        self.chats = {}



    def create_chat(self, user_id):
        """
        Create new chat session.
        """

        self.chats[user_id] = []


        return True



    def add_message(self, user_id, sender, message):
        """
        Add message to chat history.
        """

        if user_id not in self.chats:

            self.create_chat(user_id)


        self.chats[user_id].append({

            "sender":
            sender,

            "message":
            message,

            "time":
            str(datetime.datetime.now())

        })


        return True



    def get_chat_history(self, user_id):
        """
        Return chat history.
        """

        return self.chats.get(
            user_id,
            []
        )



    def clear_chat(self, user_id):
        """
        Clear chat history.
        """

        if user_id in self.chats:

            self.chats[user_id].clear()

            return True


        return False




# Testing

if __name__ == "__main__":


    chat = ChatManager()


    chat.add_message(
        "user1",
        "User",
        "Hello DG AI"
    )


    print(
        chat.get_chat_history(
            "user1"
        )
    )
