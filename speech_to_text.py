"""
DG AI Version 1
Speech To Text System

Purpose:
- Convert speech input to text
- Provide voice recognition foundation

Version: 1.0
"""


import datetime



class SpeechToText:
    """
    Handles speech to text operations.
    """



    def __init__(self):

        self.history = []



    def convert(self, speech_input):
        """
        Convert speech data into text.

        Note:
        Actual voice recognition engine
        will be connected in future.
        """

        text = str(speech_input)


        self.history.append({

            "input":
            speech_input,

            "text":
            text,

            "time":
            str(datetime.datetime.now())

        })


        return text



    def get_history(self):
        """
        Return conversion history.
        """

        return self.history



    def clear_history(self):
        """
        Clear voice history.
        """

        self.history.clear()

        return True




# Testing

if __name__ == "__main__":


    stt = SpeechToText()


    result = stt.convert(
        "Hello DG AI"
    )


    print(
        result
    )


    print(
        stt.get_history()
    )
