"""
DG AI Version 1
Content Filter System

Purpose:
- Check input content
- Provide AI safety foundation

Version: 1.0
"""


import datetime



class ContentFilter:
    """
    Handles content safety checks.
    """



    def __init__(self):

        self.blocked_words = []

        self.history = []



    def add_blocked_word(self, word):
        """
        Add word to filter list.
        """

        self.blocked_words.append(
            word.lower()
        )

        return True



    def check_content(self, text):
        """
        Check content safety.
        """

        status = "Allowed"


        for word in self.blocked_words:

            if word in text.lower():

                status = "Blocked"


                break



        result = {

            "text":
            text,

            "status":
            status,

            "time":
            str(datetime.datetime.now())

        }


        self.history.append(result)


        return result



    def get_history(self):
        """
        Return filter history.
        """

        return self.history




# Testing

if __name__ == "__main__":


    filter_system = ContentFilter()


    filter_system.add_blocked_word(
        "test"
    )


    print(
        filter_system.check_content(
            "This is a test"
        )
    )
