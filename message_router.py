"""
DG AI Version 1
Message Router System

Purpose:
- Route messages between plugins
- Manage message delivery

Version: 1.0
"""


import datetime



class MessageRouter:
    """
    Handles message routing.
    """



    def __init__(self):

        self.routes = []



    def add_route(self, sender, receiver):
        """
        Add communication route.
        """

        route = {

            "id":
            len(self.routes) + 1,

            "sender":
            sender,

            "receiver":
            receiver,

            "status":
            "Active",

            "created_at":
            str(datetime.datetime.now())

        }


        self.routes.append(route)


        return route



    def route_message(self, sender, receiver, message):
        """
        Route message.
        """

        for route in self.routes:

            if (
                route["sender"] == sender
                and route["receiver"] == receiver
            ):

                return {

                    "message":
                    message,

                    "status":
                    "Delivered",

                    "time":
                    str(datetime.datetime.now())

                }


        return {

            "message":
            message,

            "status":
            "Route Not Found"

        }



    def get_routes(self):
        """
        Return all routes.
        """

        return self.routes




# Testing

if __name__ == "__main__":


    router = MessageRouter()


    router.add_route(
        "Plugin_A",
        "Plugin_B"
    )


    print(
        router.route_message(
            "Plugin_A",
            "Plugin_B",
            "Hello"
        )
    )
