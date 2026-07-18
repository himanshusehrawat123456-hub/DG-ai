# DG AI Settings System

import json


def save_settings():

    settings = {

        "language": "Hindi",
        "voice": "Off",
        "theme": "Default"

    }


    file = open("settings.json", "w")

    json.dump(settings, file)

    file.close()

    print("Settings saved successfully")


def show_settings():

    try:

        file = open("settings.json", "r")

        settings = json.load(file)

        file.close()


        print("\nDG AI Settings")

        print("Language:", settings["language"])
        print("Voice:", settings["voice"])
        print("Theme:", settings["theme"])


    except:

        print("No settings found")
