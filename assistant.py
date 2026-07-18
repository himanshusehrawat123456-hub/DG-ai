# DG AI Assistant Core

import chat
import command
import calculator
import todo
import memory


def assistant():

    print("=== DG AI Assistant ===")


    while True:

        user_input = input("You: ")


        if user_input == "calculator":

            calculator.calculator()


        elif user_input == "todo":

            todo.todo()


        elif user_input == "chat":

            chat.chat()


        elif user_input == "command":

            command.command()


        elif user_input == "memory":

            memory.memory()


        elif user_input == "exit":

            print("DG AI Assistant Closed")
            break


        else:

            print("DG AI: Command not found")
