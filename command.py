# DG AI Command System

def command():

    while True:

        user = input("DG AI Command: ")

        if user == "calculator":
            print("Opening Calculator...")

        elif user == "todo":
            print("Opening Todo Manager...")

        elif user == "chat":
            print("Chat System Active")

        elif user == "exit":
            print("Command Closed")
            break

        else:
            print("Command not found")
