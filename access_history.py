"""
DG AI Version 1
Access History

Purpose:
- Track file access activities
- Store security access records
- Maintain audit history

Version: 1.0
"""

from datetime import datetime
import logging


class AccessHistory:

    def __init__(self):

        self.records = []

        logging.basicConfig(
            level=logging.INFO
        )


    def add_record(
        self,
        user_id,
        file_name,
        action,
        status
    ):

        record = {

            "id": len(self.records) + 1,

            "user_id": user_id,

            "file_name": file_name,

            "action": action,

            "status": status,

            "time": str(datetime.now())

        }


        self.records.append(record)

        return record


    def get_history(self):

        return self.records


    def get_user_history(
        self,
        user_id
    ):

        return [

            record for record in self.records

            if record["user_id"] == user_id

        ]


    def get_file_history(
        self,
        file_name
    ):

        return [

            record for record in self.records

            if record["file_name"] == file_name

        ]


    def clear_history(self):

        self.records.clear()

        return True



if __name__ == "__main__":

    history = AccessHistory()

    history.add_record(
        1,
        "data.txt",
        "read",
        "allowed"
    )

    print(
        history
