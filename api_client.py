"""
DG AI Version 1
API Client

Purpose:
- Handle external API communication
- Send and receive API requests
- Maintain request history

Version: 1.0
"""

import logging
import json
from datetime import datetime
from urllib.request import Request, urlopen


class APIClient:
    """
    Professional API Client
    """

    def __init__(self):

        self.request_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_request(
        self,
        url,
        method="GET",
        data=None
    ):
        """
        Create API request.
        """

        request_data = {

            "url": url,

            "method": method,

            "data": data,

            "time": str(datetime.now())

        }

        return request_data


    # ---------------------------------

    def send_request(
        self,
        url,
        method="GET"
    ):
        """
        Send basic API request.
        """

        try:

            request = Request(
                url,
                method=method
            )


            response = urlopen(
                request,
                timeout=5
            )


            result = response.read().decode(
                "utf-8"
            )


            record = {

                "url": url,

                "status": "success",

                "response": result,

                "time": str(datetime.now())

            }


            self.request_history.append(
                record
            )


            return record


        except Exception as error:


            record = {

                "url": url,

                "status": "failed",

                "error": str(error),

                "time": str(datetime.now())

            }


            self.request_history.append(
                record
            )


            return record


    # ---------------------------------

    def parse_json(
        self,
        response
    ):
        """
        Convert response into JSON.
        """

        try:

            return json.loads(
                response
            )

        except Exception:

            return None


    # ---------------------------------

    def get_history(self):

        return self.request_history


    # ---------------------------------

    def clear_history(self):

        self.request_history.clear()

        return True



if __name__ == "__main__":

    client = APIClient()

    print(
        client.create_request(
            "https://example.com"
        )
    )
