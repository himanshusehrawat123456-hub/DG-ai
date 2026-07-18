"""
DG AI Version 1
Professional Session Storage

Purpose:
- Store session data
- Retrieve session information
- Update session records
- Prepare future database integration

Version: 1.0
"""

import logging
import json
import os
from datetime import datetime


class SessionStorage:
    """
    Professional Session Storage Manager
    """


    def __init__(
        self,
        storage_file="sessions.json"
    ):

        self.storage_file = storage_file

        self.sessions = {}


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


        self.load_sessions()



    # ---------------------------------------
    # Load sessions from storage
    # ---------------------------------------

    def load_sessions(self):

        try:

            if os.path.exists(
                self.storage_file
            ):

                with open(
                    self.storage_file,
                    "r"
                ) as file:

                    self.sessions = json.load(
                        file
                    )


            else:

                self.sessions = {}


        except Exception as error:

            logging.error(
                f"Loading sessions failed: {error}"
            )

            self.sessions = {}



    # ---------------------------------------
    # Save sessions
    # ---------------------------------------

    def save_sessions(self):

        try:

            with open(
                self.storage_file,
                "w"
            ) as file:

                json.dump(
                    self.sessions,
                    file,
                    indent=4,
                    default=str
                )


            return True



        except Exception as error:

            logging.error(
                f"Saving sessions failed: {error}"
            )

            return False



    # ---------------------------------------
    # Store session
    # ---------------------------------------

    def store_session(
        self,
        session_id,
        session_data
    ):

        self.sessions[session_id] = {

            **session_data,

            "updated_at":
            str(datetime.now())

        }


        self.save_sessions()


        return True



    # ---------------------------------------
    # Get session
    # ---------------------------------------

    def get_session(
        self,
        session_id
    ):

        return self.sessions.get(
            session_id
        )



    # ---------------------------------------
    # Delete session
    # ---------------------------------------

    def delete_session(
        self,
        session_id
    ):


        if session_id in self.sessions:


            del self.sessions[session_id]


            self.save_sessions()


            return True



        return False



    # ---------------------------------------
    # Get all sessions
    # ---------------------------------------

    def get_all_sessions(self):

        return self.sessions



    # ---------------------------------------
    # Clear storage
    # ---------------------------------------

    def clear_storage(self):

        self.sessions.clear()

        self.save_sessions()

        return True



# ---------------------------------------
# Testing
# ---------------------------------------

if __name__ == "__main__":


    storage = SessionStorage()


    storage.store_session(

        "session_001",

        {
            "user_id":
            "user_001",

            "status":
            "active"
        }

    )


    print(
        storage.get_all_sessions()
    )
