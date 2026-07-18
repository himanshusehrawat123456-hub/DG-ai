"""
DG AI Version 1
Conversation Management System

Purpose:
- Manage chat conversations
- Store user and AI messages
- Provide conversation memory foundation

Version: 1.0
"""


import datetime
import json
import os



class ConversationManager:
    """
    Handles DG AI conversations.
    """



    def __init__(self, file_path="data/conversation.json"):

        self.file_path = file_path

        self.messages = []

        self._create_storage()

        self._load_messages()



    def _create_storage(self):
        """
        Create storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def add_message(self, sender, message):
        """
        Add conversation message.
        """

        data = {

            "sender":
            sender,

            "message":
            message,

            "time":
            str(datetime.datetime.now())

        }


        self.messages.append(data)

        self._save_messages()



    def get_conversation(self):
        """
        Return conversation history.
        """

        return self.messages



    def clear_conversation(self):
        """
        Clear chat history.
        """

        self.messages.clear()

        self._save_messages()



    def _save_messages(self):
        """
        Save conversation.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.messages,
                file,
                indent=4
            )



    def _load_messages(self):
        """
        Load previous conversation.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.messages = json.load(file)




# Testing

if __name__ == "__main__":


    chat = ConversationManager()


    chat.add_message(
        "User",
        "Hello DG AI"
    )


    chat.add_message(
        "DG AI",
        "Hello, how can I help you?"
    )


    print(
        chat.get_conversation()
    )
