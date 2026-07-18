# DG AI User Profile

import json


def save_profile():

    name = input("Enter your name: ")

    profile = {
        "name": name
    }

    file = open("profile.json", "w")

    json.dump(profile, file)

    file.close()

    print("Profile saved")


def show_profile():

    try:

        file = open("profile.json", "r")

        profile = json.load(file)

        file.close()

        print("User Name:", profile["name"])

    except:

        print("No profile found")
