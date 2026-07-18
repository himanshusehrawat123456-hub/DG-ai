"""
DG AI Version 1
Context Management System

Purpose:
- Manage conversation context
- Store temporary conversation information
- Provide context foundation

Version: 1.0
"""


import datetime



class ContextManager:
    """
    Handles DG AI conversation context.
    """



    def __init__(self):

        self.context = {}



    def create_context(self, user_id):
        """
        Create new user context.
        """

        self.context[user_id] = {

            "messages": [],

            "created_time":
            str(datetime.datetime.now())

        }


        return True



    def add_message(self, user_id, role, message):
        """
        Add conversation message.
        """

        if user_id not in self.context:

            self.create_context(user_id)


        self.context[user_id]["messages"].append({

            "role": role,

            "message": message,

            "time":
            str(datetime.datetime.now())

        })


        return True



    def get_context(self, user_id):
        """
        Get user context.
        """

        return self.context.get(
            user_id,
            {}
        )



    def clear_context(self, user_id):
        """
        Clear user context.
        """

        if user_id in self.context:

            del self.context[user_id]

            return True


        return False



    def get_all_context(self):
        """
        Return all contexts.
        """

        return self.context




# Testing

if __name__ == "__main__":


    manager = ContextManager()


    manager.add_message(
        "DG001",
        "User",
        "Hello DG AI"
    )


    manager.add_message(
        "DG001",
        "AI",
        "Hello, how can I help?"
    )


    print(
        manager.get_context(
            "DG001"
        )
    )
