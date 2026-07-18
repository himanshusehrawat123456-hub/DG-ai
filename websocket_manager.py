"""
DG AI Version 1
WebSocket Manager System

Purpose:
- Manage real-time connections
- Handle live communication foundation

Version: 1.0
"""


import datetime



class WebSocketManager:
    """
    Handles real-time communication.
    """



    def __init__(self):

        self.connections = []



    def connect_user(self, user_id):
        """
        Add new user connection.
        """

        connection = {

            "user_id":
            user_id,

            "status":
            "connected",

            "time":
            str(datetime.datetime.now())

        }


        self.connections.append(connection)


        return connection



    def disconnect_user(self, user_id):
        """
        Remove user connection.
        """

        for connection in self.connections:

            if connection["user_id"] == user_id:

                self.connections.remove(connection)

                return True


        return False



    def send_message(self, user_id, message):
        """
        Send real-time message.
        """

        return {

            "user_id":
            user_id,

            "message":
            message,

            "status":
            "sent",

            "time":
            str(datetime.datetime.now())

        }



    def get_connections(self):
        """
        Return active connections.
        """

        return self.connections




# Testing

if __name__ == "__main__":


    websocket = WebSocketManager()


    websocket.connect_user(
        "User_001"
    )


    print(
        websocket.send_message(
            "User_001",
            "Hello DG AI"
        )
    )
