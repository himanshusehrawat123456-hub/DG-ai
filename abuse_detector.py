"""
DG AI Version 1
Abuse Detection System

Purpose:
- Detect suspicious input patterns
- Provide safety monitoring foundation

Version: 1.0
"""


import datetime



class AbuseDetector:
    """
    Handles abuse detection operations.
    """



    def __init__(self):

        self.rules = []

        self.history = []



    def add_rule(self, rule):
        """
        Add detection rule.
        """

        self.rules.append(
            rule.lower()
        )

        return True



    def check_input(self, text):
        """
        Check input against rules.
        """

        status = "Safe"


        for rule in self.rules:

            if rule in text.lower():

                status = "Suspicious"

                break



        result = {

            "input":
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
        Return detection history.
        """

        return self.history




# Testing

if __name__ == "__main__":


    detector = AbuseDetector()


    detector.add_rule(
        "spam"
    )


    print(
        detector.check_input(
            "This is spam message"
        )
    )
