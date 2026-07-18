"""
DG AI Version 1
Professional Event Dispatcher

Purpose:
- Route events to registered handlers
- Manage event execution flow
- Track dispatch status
- Prepare future message/event bus integration

Version: 1.0
"""

import logging
import uuid
from datetime import datetime



class EventDispatcher:
    """
    Professional Event Dispatch System
    """


    def __init__(self):

        self.event_handlers = {}

        self.dispatch_history = []


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )



    # ---------------------------------------
    # Register handler
    # ---------------------------------------

    def register_handler(
        self,
        event_name,
        handler
    ):

        try:

            if event_name not in self.event_handlers:

                self.event_handlers[event_name] = []


            self.event_handlers[event_name].append(
                handler
            )


            logging.info(
                f"Handler registered for {event_name}"
            )


            return True



        except Exception as error:

            logging.error(
                f"Handler registration failed: {error}"
            )

            return False



    # ---------------------------------------
    # Dispatch event
    # ---------------------------------------

    def dispatch(
        self,
        event_name,
        event_data
    ):

        try:

            dispatch_id = str(
                uuid.uuid4()
            )


            result = {

                "dispatch_id":
                dispatch_id,


                "event_name":
                event_name,


                "data":
                event_data,


                "status":
                "processing",


                "created_at":
                str(datetime.now())

            }


            handlers = self.event_handlers.get(
                event_name,
                []
            )


            responses = []


            for handler in handlers:

                response = handler(
                    event_data
                )

                responses.append(
                    response
                )


            result["responses"] = responses


            result["status"] = "completed"


            self.dispatch_history.append(
                result
            )


            logging.info(
                "Event dispatched successfully"
            )


            return result



        except Exception as error:


            logging.error(
                f"Event dispatch failed: {error}"
            )


            return None



    # ---------------------------------------
    # Get handlers
    # ---------------------------------------

    def get_handlers(self):

        return self.event_handlers



    # ---------------------------------------
    # Get dispatch history
    # ---------------------------------------

    def get_dispatch_history(self):

        return self.dispatch_history



    # ---------------------------------------
    # Clear history
    # ---------------------------------------

    def clear_history(self):

        self.dispatch_history.clear()

        return True




# ---------------------------------------
# Testing
# ---------------------------------------

if __name__ == "__main__":


    dispatcher = EventDispatcher()


    def test_handler(data):

        return {

            "message":
            "Event processed",

            "data":
            data

        }


    dispatcher.register_handler(

        "system_start",

        test_handler

    )


    print(

        dispatcher.dispatch(

            "system_start",

            {
                "service":
                "DG AI"
            }

        )

    )
