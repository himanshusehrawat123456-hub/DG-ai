"""
DG AI Version 1
Voice History

Purpose:
- Store voice activity records
- Track speech and voice generation events
- Maintain voice audit history

Version: 1.0
"""

import logging
from datetime import datetime


class VoiceHistory:
    """
    Professional Voice History Manager
    """

    def __init__(self):

        self.records = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def add_record(
        self,
        action,
        input_data,
        status="completed"
    ):
        """
        Add voice activity record.
        """

        record = {

            "id":
            len(self.records) + 1,

            "action":
            action,

            "input":
            input_data,

            "status":
            status,

            "time":
            str(datetime.now())

        }


        self.records.append(
            record
        )


        return record


    # ---------------------------------

    def get_history(self):
        """
        Return all voice history.
        """

        return self.records


    # ---------------------------------

    def search_history(
        self,
        keyword
    ):
        """
        Search voice records.
        """

        result = []


        for record in self.records:

            if keyword.lower() in str(record).lower():

                result.append(record)


        return result


    # ---------------------------------

    def clear_history(self):

        self.records.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    history = VoiceHistory()


    history.add_record(
        "Speech Recognition",
        "hello audio"
    )


    print(
        history.get_history()
    )
