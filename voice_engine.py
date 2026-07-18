# DG AI Voice Engine


def speak(text):

    print("DG AI Voice:", text)



def listen():

    user_input = input("You: ")

    return user_input



def voice_test():

    print("=== DG AI Voice Engine ===")


    command = listen()


    speak("You said: " + command)
