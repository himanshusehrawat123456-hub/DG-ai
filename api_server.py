"""
DG AI Version 1
API Server System

Purpose:
- Handle API communication
- Provide server foundation

Version: 1.0
"""


import datetime



class APIServer:
    """
    Handles DG AI API operations.
    """



    def __init__(self):

        self.requests = []



    def receive_request(self, user, message):
        """
        Receive user request.
        """

        data = {

            "user":
            user,

            "message":
            message,

            "status":
            "received",

            "time":
            str(datetime.datetime.now())

        }


        self.requests.append(data)


        return data



    def process_request(self, request):
        """
        Process API request.
        """

        response = {

            "status":
            "success",

            "message":
            "DG AI request processed",

            "request":
            request

        }


        return response



    def get_requests(self):
        """
        Return request history.
        """

        return self.requests




# Testing

if __name__ == "__main__":


    server = APIServer()


    request = server.receive_request(
        "User",
        "Hello DG AI"
    )


    print(
        server.process_request(
            request
        )
    )
