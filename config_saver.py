"""
DG AI Version 1
Configuration Saver

Purpose:
- Save configuration files
- Write JSON configuration

Version: 1.0
"""

import json
import datetime


class ConfigSaver:
    """
    Handles configuration saving.
    """

    def __init__(self):
        self.last_saved = None

    def save_config(self, file_path, config_data):
        """
        Save configuration to file.
        """

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                config_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        self.last_saved = str(datetime.datetime.now())

        return True

    def get_last_saved(self):
        """
        Return last saved time.
        """

        return self.last_saved


# Testing

if __name__ == "__main__":

    saver = ConfigSaver()

    sample_config = {
        "app_name": "DG AI",
        "version": "1.0.0",
        "theme": "dark"
    }

    saver.save_config(
        "config.json",
        sample_config
    )

    print(
        saver.get_last_saved()
    )
