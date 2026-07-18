
# DG AI Assistant Core

import brain
import calculator
import todo
import chat
import command
import memory
import notes


def assistant():

    print("===================")
    print("  DG AI Assistant  ")
    print("===================")


    while True:

        user_input = input("\nYou: ")


        result = brain.process_command(user_input)


        if result == "OPEN_CALCULATOR":

            calculator.calculator()


        elif result == "OPEN_TODO":

            todo.todo()


        elif result == "OPEN_CHAT":

            chat.chat()


        elif result == "OPEN_COMMAND":

            command.command()


        elif result == "OPEN_MEMORY":

            memory.memory()


        elif result == "OPEN_NOTES":

            notes.notes()


        elif result == "EXIT":

            print("DG AI: Closing Assistant")
            break


        else:

            print("DG AI:", result)
