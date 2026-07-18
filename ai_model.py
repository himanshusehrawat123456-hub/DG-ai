# DG AI AI Model System


MODEL_NAME = "DG AI Basic Model"



def load_model():

    print(MODEL_NAME, "loaded successfully")



def generate_response(user_input):

    user_input = user_input.lower()


    if "hello" in user_input or "hi" in user_input:

        return "Hello, I am DG AI"


    elif "your name" in user_input:

        return "My name is DG AI"


    else:

        return "I am learning this command"



def model_status():

    print("AI Model Status: Active")
