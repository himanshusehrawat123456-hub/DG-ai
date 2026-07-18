# DG AI Voice System

def speak(text):

    print("DG AI:", text)



def listen():

    user_voice = input("You: ")

    return user_voice



def voice_assistant():

    print("=== DG AI Voice Assistant ===")


    while True:

        command = listen()


        if command == "exit":

            print("Voice Assistant Closed")
            break


        else:

            speak("You said: " + command)
