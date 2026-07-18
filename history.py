# DG AI Chat History System

import json


def save_history(message):

    try:

        file = open("history.json", "r")

        history = json.load(file)

        file.close()

    except:

        history = []


    history.append(message)


    file = open("history.json", "w")

    json.dump(history, file)

    file.close()


    print("History saved")


def show_history():

    try:

        file = open("history.json", "r")

        history = json.load(file)

        file.close()


        print("\nChat History:")

        for chat in history:

            print("-", chat)


    except:

        print("No history found")
