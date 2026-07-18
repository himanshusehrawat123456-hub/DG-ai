"""
DG AI Version 1
Request Handler

Purpose:
- Handle incoming API requests
- Process request data

Version: 1.0
"""


import datetime



class RequestHandler:
    """
    Handles API request operations.
    """



    def __init__(self):

        self.requests = []



    def create_request(self, endpoint, data):
        """
        Create and store request.
        """

        request = {

            "id":
            len(self.requests) + 1,

            "endpoint":
            endpoint,

            "data":
            data,

            "time":
            str(datetime.datetime.now())

        }


        self.requests.append(request)


        return request



    def get_requests(self):
        """
        Return request history.
        """

        return self.requests



    def clear_requests(self):
        """
        Clear request history.
        """

        self.requests.clear()

        return True




# Testing

if __name__ == "__main__":


    handler = RequestHandler()


    print(
        handler.create_request(
            "/chat",
            {
                "message": "Hello DG AI"
            }
        )
    )
