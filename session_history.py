"""
DG AI Version 1
Professional Session History Manager

Purpose:
- Maintain session activity logs
- Track login/logout events
- Store session audit records
- Prepare future database integration

Version: 1.0
"""

import logging
import uuid
from datetime import datetime


class SessionHistory:
    """
    Professional Session History System
    """


    def __init__(self):

        self.history_records = []


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )



    # ---------------------------------------
    # Add history record
    # ---------------------------------------

    def add_record(
        self,
        session_id,
        user_id,
        action,
        status="completed",
        details=None
    ):

        try:

            record = {

                "history_id":
                str(uuid.uuid4()),


                "session_id":
                session_id,


                "user_id":
                user_id,


                "action":
                action,


                "status":
                status,


                "details":
                details,


                "timestamp":
                str(datetime.now())

            }


            self.history_records.append(
                record
            )


            logging.info(
                "Session history record added"
            )


            return record



        except Exception as error:

            logging.error(
                f"History creation failed: {error}"
            )

            return None



    # ---------------------------------------
    # Get complete history
    # ---------------------------------------

    def get_history(self):

        return self.history_records



    # ---------------------------------------
    # Get user history
    # ---------------------------------------

    def get_user_history(
        self,
        user_id
    ):


        return [

            record

            for record in self.history_records

            if record["user_id"] == user_id

        ]



    # ---------------------------------------
    # Get session history
    # ---------------------------------------

    def get_session_history(
        self,
        session_id
    ):


        return [

            record

            for record in self.history_records

            if record["session_id"] == session_id

        ]



    # ---------------------------------------
    # Search history
    # ---------------------------------------

    def search_history(
        self,
        keyword
    ):


        results = []


        for record in self.history_records:


            if keyword.lower() in str(record).lower():

                results.append(record)



        return results



    # ---------------------------------------
    # Delete history
    # ---------------------------------------

    def delete_record(
        self,
        history_id
    ):


        for record in self.history_records:


            if record["history_id"] == history_id:


                self.history_records.remove(
                    record
                )


                return True



        return False



    # ---------------------------------------
    # Clear history
    # ---------------------------------------

    def clear_history(self):

        self.history_records.clear()

        return True




# ---------------------------------------
# Testing
# ---------------------------------------

if __name__ == "__main__":


    history = SessionHistory()


    record = history.add_record(

        "session_001",

        "user_001",

        "login",

        "success",

        "User logged into DG AI"

    )


    print(record)
