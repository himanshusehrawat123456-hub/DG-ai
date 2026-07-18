# DG AI Global Language Configuration


APP_NAME = "DG AI"

VERSION = "1.0"


SUPPORTED_LANGUAGES = {

    "India": [
        "Hindi",
        "English",
        "Bengali",
        "Telugu",
        "Marathi",
        "Tamil",
        "Gujarati",
        "Urdu",
        "Kannada",
        "Malayalam",
        "Punjabi",
        "Odia",
        "Assamese",
        "Sanskrit"
    ],


    "Europe": [
        "Spanish",
        "French",
        "German",
        "Italian",
        "Portuguese",
        "Russian"
    ],


    "Asia": [
        "Chinese",
        "Japanese",
        "Korean",
        "Arabic",
        "Thai",
        "Vietnamese"
    ],


    "Africa": [
        "Swahili",
        "Amharic",
        "Hausa"
    ],


    "Americas": [
        "English",
        "Spanish",
        "Portuguese",
        "French"
    ]

}


CURRENT_LANGUAGE = "Hindi"



def show_languages():

    print("===== DG AI Languages =====")


    for region, languages in SUPPORTED_LANGUAGES.items():

        print("\n", region)

        for language in languages:

            print("-", language)
"""
DG AI Version 1
Configuration Management System

Purpose:
- Manage global settings
- Store application configuration
- Provide centralized control

Version: 1.0
"""


import os



class DGConfig:
    """
    Main configuration controller.
    """



    def __init__(self):

        # Application Information

        self.APP_NAME = "DG AI"

        self.VERSION = "1.0"


        # Developer Information

        self.DEVELOPER = "DG AI Team"


        # Directory Configuration

        self.BASE_DIR = os.path.dirname(
            os.path.abspath(__file__)
        )


        self.DATA_DIR = os.path.join(
            self.BASE_DIR,
            "data"
        )


        self.MEMORY_FILE = os.path.join(
            self.DATA_DIR,
            "memory.json"
        )


        self.LOG_FILE = os.path.join(
            self.DATA_DIR,
            "activity_logs.json"
        )


        # System Settings

        self.LANGUAGE = "English"

        self.DEBUG_MODE = True


        # AI Settings (Future)

        self.AI_MODEL = None

        self.VOICE_ENABLED = False



    def get_config(self):
        """
        Return complete configuration.
        """

        return {

            "name": self.APP_NAME,

            "version": self.VERSION,

            "developer": self.DEVELOPER,

            "language": self.LANGUAGE,

            "debug": self.DEBUG_MODE,

            "voice": self.VOICE_ENABLED

        }



# Testing

if __name__ == "__main__":


    config = DGConfig()


    print("\nDG AI Configuration")

    print("--------------------")


    settings = config.get_config()


    for key, value in settings.items():

        print(
            f"{key}: {value}"
        )
