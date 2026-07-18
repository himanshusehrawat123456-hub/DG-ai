"""
DG AI Version 1
User Settings System

Purpose:
- Manage user preferences
- Store user settings

Version: 1.0
"""


import datetime



class UserSettings:
    """
    Handles user settings.
    """



    def __init__(self):

        self.settings = {}



    def save_settings(self, user_id, settings):
        """
        Save user settings.
        """

        self.settings[user_id] = {

            "settings":
            settings,

            "time":
            str(datetime.datetime.now())

        }


        return True



    def get_settings(self, user_id):
        """
        Get user settings.
        """

        return self.settings.get(
            user_id,
            {}
        )



    def update_settings(self, user_id, new_settings):
        """
        Update user settings.
        """

        if user_id in self.settings:

            self.settings[user_id]["settings"] = new_settings

            return True


        return False




# Testing

if __name__ == "__main__":


    settings = UserSettings()


    settings.save_settings(
        "user1",
        {
            "language": "Hindi",
            "theme": "Dark"
        }
    )


    print(
        settings.get_settings(
            "user1"
        )
    )
