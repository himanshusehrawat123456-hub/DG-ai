# DG AI Main File

import login
import calculator
import todo
import chat
import command
import storage
import memory
import notes


def main():

    user = login.login()

    if user:

        print("\nWelcome To DG AI")

        while True:

            print("\n===== DG AI MENU =====")
            print("1. Calculator")
            print("2. Todo")
            print("3. Chat")
            print("4. Command")
            print("5. Memory")
            print("6. Notes")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                calculator.calculator()

            elif choice == "2":
                todo.todo()

            elif choice == "3":
                chat.chat()

            elif choice == "4":
                command.command()

            elif choice == "5":
                memory.memory()

            elif choice == "6":
                notes.notes()

            elif choice == "7":
                print("DG AI Closed")
                break

            else:
                print("Invalid Choice")

    else:
        print("Login Failed")


main()
