"""
DG AI Version 1
Event Logging System

Purpose:
- Track system events
- Store activity records
- Provide analytics foundation

Version: 1.0
"""


import json
import os
import datetime



class EventLogger:
    """
    Handles DG AI event logging.
    """



    def __init__(self, file_path="data/events.json"):

        self.file_path = file_path

        self.events = []

        self._create_storage()

        self._load_events()



    def _create_storage(self):
        """
        Create storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def add_event(self, event_type, description):
        """
        Add new event.
        """

        event = {

            "type":
            event_type,

            "description":
            description,

            "time":
            str(datetime.datetime.now())

        }


        self.events.append(event)

        self._save_events()


        return event



    def get_events(self):
        """
        Return all events.
        """

        return self.events



    def clear_events(self):
        """
        Clear event history.
        """

        self.events.clear()

        self._save_events()



    def _save_events(self):
        """
        Save events.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.events,
                file,
                indent=4
            )



    def _load_events(self):
        """
        Load saved events.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.events = json.load(file)




# Testing

if __name__ == "__main__":


    logger = EventLogger()


    logger.add_event(
        "START",
        "DG AI Started Successfully"
    )


    logger.add_event(
        "COMMAND",
        "User opened AI Assistant"
    )


    print(
        "DG AI Events:"
    )


    print(
        logger.get_events()
    )
