"""
DG AI Version 1
Event Management System

Purpose:
- Manage system events
- Track actions and activities
- Provide automation foundation

Version: 1.0
"""


import datetime



class EventManager:
    """
    Handles DG AI event operations.
    """



    def __init__(self):

        self.events = []



    def create_event(self, event_name, data=None):
        """
        Create a new event.
        """

        event = {

            "id":
            len(self.events) + 1,

            "event":
            event_name,

            "data":
            data or {},

            "time":
            str(datetime.datetime.now())

        }


        self.events.append(event)


        return event



    def get_events(self):
        """
        Return all events.
        """

        return self.events



    def get_latest_event(self):
        """
        Return latest event.
        """

        if self.events:

            return self.events[-1]


        return None



    def clear_events(self):
        """
        Remove all events.
        """

        self.events.clear()

        return True




# Testing

if __name__ == "__main__":


    manager = EventManager()


    manager.create_event(
        "System Started",
        {
            "module": "DG AI"
        }
    )


    manager.create_event(
        "User Command Received",
        {
            "command": "Hello"
        }
    )


    print(
        "DG AI Events:"
    )


    for event in manager.get_events():

        print(event)
