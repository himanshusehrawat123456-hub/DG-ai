"""
DG AI Version 1
Settings Management System

Purpose:
- Manage DG AI configuration settings
- Store user preferences
- Control system options

Version: 1.0
"""


import json
import os



class SettingsManager:
    """
    Handles DG AI settings operations.
    """



    def __init__(self, file_path="data/settings.json"):

        self.file_path = file_path

        self.settings = {}

        self._create_storage()

        self._load_settings()



    def _create_storage(self):
        """
        Create settings storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def set_setting(self, key, value):
        """
        Add or update setting.
        """

        self.settings[key] = value

        self._save_settings()



    def get_setting(self, key):
        """
        Get specific setting.
        """

        return self.settings.get(
            key,
            None
        )



    def get_all_settings(self):
        """
        Return all settings.
        """

        return self.settings



    def remove_setting(self, key):
        """
        Remove a setting.
        """

        if key in self.settings:

            del self.settings[key]

            self._save_settings()

            return True


        return False



    def _save_settings(self):
        """
        Save settings permanently.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.settings,
                file,
                indent=4
            )



    def _load_settings(self):
        """
        Load saved settings.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.settings = json.load(file)




# Testing

if __name__ == "__main__":


    settings = SettingsManager()


    settings.set_setting(
        "language",
        "Hindi"
    )


    settings.set_setting(
        "voice",
        True
    )


    print(
        "DG AI Settings:"
    )


    print(
        settings.get_all_settings()
    )
