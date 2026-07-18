# DG AI API System

import json


def save_api_key():

    key = input("Enter API Key: ")


    data = {

        "api_key": key

    }


    file = open("api_config.json", "w")

    json.dump(data, file)

    file.close()


    print("API Key Saved")



def load_api_key():

    try:

        file = open("api_config.json", "r")

        data = json.load(file)

        file.close()


        return data["api_key"]


    except:

        return None



def connect_api():

    api_key = load_api_key()


    if api_key:

        print("API Connection Ready")

    else:

        print("API Key Not Found")
