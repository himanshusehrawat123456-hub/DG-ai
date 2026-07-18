"""
DG AI Version 1
Data Validator System

Purpose:
- Validate stored data
- Check data quality and format

Version: 1.0
"""


import datetime



class DataValidator:
    """
    Handles data validation operations.
    """



    def __init__(self):

        self.history = []



    def validate(self, data):
        """
        Validate data input.
        """

        status = "Valid"


        if data is None:

            status = "Invalid"


        elif data == "":

            status = "Empty"



        result = {

            "data":
            data,

            "status":
            status,

            "time":
            str(datetime.datetime.now())

        }


        self.history.append(result)


        return result



    def get_history(self):
        """
        Return validation history.
        """

        return self.history



    def clear_history(self):
        """
        Clear validation history.
        """

        self.history.clear()

        return True




# Testing

if __name__ == "__main__":


    validator = DataValidator()


    print(
        validator.validate(
            "DG AI Data"
        )
    )


    print(
        validator.validate(
            None
        )
    )
