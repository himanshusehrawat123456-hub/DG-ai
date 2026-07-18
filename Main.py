
# DG AI Main File

import login
import calculator
import todo
import chat
import command
import storage
import memory
import notes

import user_profile
import settings
import history
import database
import voice
import assistant
import tools


def main():

    user = login.login()


    if user:

        print("\n===================")
        print("   Welcome DG AI   ")
        print("===================")


        while True:

            print("\n===== DG AI MENU =====")

            print("1. Calculator")
            print("2. Todo")
            print("3. Chat")
            print("4. Command")
            print("5. Memory")
            print("6. Notes")
            print("7. User Profile")
            print("8. Settings")
            print("9. History")
            print("10. Voice Assistant")
            print("11. AI Assistant")
            print("12. Exit")


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

                user_profile.save_profile()


            elif choice == "8":

                settings.save_settings()


            elif choice == "9":

                history.show_history()


            elif choice == "10":

                voice.voice_assistant()


            elif choice == "11":

                assistant.assistant()


            elif choice == "12":

                print("DG AI Closed")
                break


            else:

                print("Invalid Choice")


    else:

        print("Login Failed")



main()
