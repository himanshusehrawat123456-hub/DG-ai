"""
DG AI Version 1
Response Handler

Purpose:
- Handle API responses
- Format response data

Version: 1.0
"""


import datetime



class ResponseHandler:
    """
    Handles API response operations.
    """



    def __init__(self):

        self.responses = []



    def create_response(self, status, data):
        """
        Create response object.
        """

        response = {

            "id":
            len(self.responses) + 1,

            "status":
            status,

            "data":
            data,

            "time":
            str(datetime.datetime.now())

        }


        self.responses.append(response)


        return response



    def get_responses(self):
        """
        Return response history.
        """

        return self.responses



    def clear_responses(self):
        """
        Clear response history.
        """

        self.responses.clear()

        return True




# Testing

if __name__ == "__main__":


    handler = ResponseHandler()


    print(
        handler.create_response(
            "success",
            {
                "message": "DG AI Response"
            }
        )
    )
