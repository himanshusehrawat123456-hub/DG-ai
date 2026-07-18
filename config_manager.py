"""
DG AI Version 1
Configuration Management System

Purpose:
- Manage system configuration
- Store and update settings
- Provide configuration foundation

Version: 1.0
"""


import json
import os



class ConfigManager:
    """
    Handles DG AI configuration.
    """



    def __init__(self, file_path="data/config.json"):

        self.file_path = file_path

        self.config = {}

        self._create_storage()

        self._load_config()



    def _create_storage(self):
        """
        Create configuration folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def set_config(self, key, value):
        """
        Add or update configuration.
        """

        self.config[key] = value

        self._save_config()



    def get_config(self, key):
        """
        Get configuration value.
        """

        return self.config.get(
            key,
            None
        )



    def get_all_config(self):
        """
        Return all configuration.
        """

        return self.config



    def remove_config(self, key):
        """
        Remove configuration.
        """

        if key in self.config:

            del self.config[key]

            self._save_config()

            return True


        return False



    def _save_config(self):
        """
        Save configuration data.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.config,
                file,
                indent=4
            )



    def _load_config(self):
        """
        Load existing configuration.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.config = json.load(file)




# Testing

if __name__ == "__main__":


    config = ConfigManager()


    config.set_config(
        "AI_Name",
        "DG AI"
    )


    config.set_config(
        "Version",
        "1.0"
    )


    print(
        "DG AI Configuration:"
    )


    print(
        config.get_all_config()
    )
