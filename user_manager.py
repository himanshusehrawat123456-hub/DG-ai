# DG AI User Manager System

import json


USER_FILE = "users.json"



def add_user(name):

    try:

        file = open(USER_FILE, "r")

        users = json.load(file)

        file.close()


    except:

        users = []


    users.append({

        "name": name

    })


    file = open(USER_FILE, "w")

    json.dump(users, file)

    file.close()


    print("User added:", name)



def show_users():

    try:

        file = open(USER_FILE, "r")

        users = json.load(file)

        file.close()


        print("===== DG AI Users =====")


        for user in users:

            print("-", user["name"])


    except:

        print("No users found")
