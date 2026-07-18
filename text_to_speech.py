"""
DG AI Version 1
Text To Speech System

Purpose:
- Convert text into speech output
- Provide voice response foundation

Version: 1.0
"""


import datetime



class TextToSpeech:
    """
    Handles DG AI text to speech operations.
    """



    def __init__(self):

        self.history = []



    def speak(self, text):
        """
        Convert text into voice.

        Note:
        Actual voice engine will be
        connected in future.
        """

        response = {

            "text":
            text,

            "status":
            "Ready for speech",

            "time":
            str(datetime.datetime.now())

        }


        self.history.append(response)


        return response



    def get_history(self):
        """
        Return speech history.
        """

        return self.history



    def clear_history(self):
        """
        Clear speech history.
        """

        self.history.clear()

        return True




# Testing

if __name__ == "__main__":


    tts = TextToSpeech()


    result = tts.speak(
        "Hello, I am DG AI"
    )


    print(
        result
    )


    print(
        tts.get_history()
    )
