"""
DG AI Version 1
Image History

Purpose:
- Store image activity records
- Track generated and processed images
- Maintain image audit history

Version: 1.0
"""

import logging
from datetime import datetime


class ImageHistory:
    """
    Professional Image History Manager
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
        image_name,
        action,
        status="completed"
    ):
        """
        Add image activity record.
        """

        record = {

            "id":
            len(self.records) + 1,

            "image":
            image_name,

            "action":
            action,

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

        return self.records


    # ---------------------------------

    def search_history(
        self,
        keyword
    ):

        return [

            record for record in self.records

            if keyword.lower() in str(record).lower()

        ]


    # ---------------------------------

    def clear_history(self):

        self.records.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    history = ImageHistory()


    history.add_record(
        "robot.png",
        "generated"
    )


    print(
        history.get_history()
    )
