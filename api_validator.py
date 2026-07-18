"""
DG AI Version 1
API Validator

Purpose:
- Validate API requests and responses
- Check required data format

Version: 1.0
"""


import datetime



class APIValidator:
    """
    Handles API validation.
    """



    def __init__(self):

        self.validation_logs = []



    def validate_request(self, request_data):
        """
        Validate incoming request.
        """

        status = True


        if request_data is None:

            status = False


        log = {

            "type":
            "request",

            "status":
            status,

            "time":
            str(datetime.datetime.now())

        }


        self.validation_logs.append(log)


        return status



    def validate_response(self, response_data):
        """
        Validate API response.
        """

        status = True


        if response_data is None:

            status = False


        log = {

            "type":
            "response",

            "status":
            status,

            "time":
            str(datetime.datetime.now())

        }


        self.validation_logs.append(log)


        return status



    def get_logs(self):
        """
        Return validation logs.
        """

        return self.validation_logs




# Testing

if __name__ == "__main__":


    validator = APIValidator()


    print(
        validator.validate_request(
            {
                "message": "Hello"
            }
        )
    )


    print(
        validator.get_logs()
    )
