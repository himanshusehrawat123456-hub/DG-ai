"""
DG AI Version 1
Learning Management System

Purpose:
- Store learning data
- Manage user preferences
- Provide personalization foundation

Version: 1.0
"""


import datetime



class LearningManager:
    """
    Handles DG AI learning operations.
    """



    def __init__(self):

        self.learning_data = {}



    def add_learning(self, user_id, key, value):
        """
        Store user learning data.
        """

        if user_id not in self.learning_data:

            self.learning_data[user_id] = {}


        self.learning_data[user_id][key] = {

            "value": value,

            "time":
            str(datetime.datetime.now())

        }


        return True



    def get_learning(self, user_id):
        """
        Get user learning data.
        """

        return self.learning_data.get(
            user_id,
            {}
        )



    def remove_learning(self, user_id, key):
        """
        Remove learning data.
        """

        if user_id in self.learning_data:

            if key in self.learning_data[user_id]:

                del self.learning_data[user_id][key]

                return True


        return False



    def clear_learning(self):
        """
        Clear all learning data.
        """

        self.learning_data.clear()

        return True




# Testing

if __name__ == "__main__":


    manager = LearningManager()


    manager.add_learning(
        "DG001",
        "language",
        "Hindi"
    )


    print(
        manager.get_learning(
            "DG001"
        )
    )
