"""
DG AI Version 1
Configuration Loader

Purpose:
- Load configuration files
- Read JSON configuration

Version: 1.0
"""

import json
import os


class ConfigLoader:
    """
    Handles configuration loading.
    """

    def __init__(self):
        self.config = {}

    def load_config(self, file_path):
        """
        Load configuration file.
        """

        if not os.path.exists(file_path):
            return None

        with open(file_path, "r", encoding="utf-8") as file:
            self.config = json.load(file)

        return self.config

    def get_config(self):
        """
        Return loaded configuration.
        """

        return self.config


# Testing

if __name__ == "__main__":

    loader = ConfigLoader()

    print(
        loader.load_config(
            "config.json"
        )
    )
