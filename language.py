# DG AI Language System


current_language = "Hindi"


def set_language(language):

    global current_language

    current_language = language

    print("Language changed to:", current_language)



def get_language():

    return current_language



def show_language():

    print("Current Language:", current_language)
