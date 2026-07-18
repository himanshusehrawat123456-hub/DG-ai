"""
DG AI Version 1
Schedule History

Purpose:
- Store scheduled task history
- Track job execution records
- Maintain scheduler audit logs

Version: 1.0
"""

import logging
from datetime import datetime


class ScheduleHistory:
    """
    Professional Schedule History Manager
    """

    def __init__(self):

        self.history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def add_record(
        self,
        job_name,
        status,
        details=None
    ):
        """
        Add schedule execution record.
        """

        record = {

            "id":
            len(self.history) + 1,

            "job":
            job_name,

            "status":
            status,

            "details":
            details,

            "time":
            str(datetime.now())

        }


        self.history.append(
            record
        )


        return record


    # ---------------------------------

    def get_history(self):
        """
        Return all schedule history.
        """

        return self.history


    # ---------------------------------

    def get_job_history(
        self,
        job_name
    ):
        """
        Search specific job history.
        """

        return [

            record for record in self.history

            if record["job"] == job_name

        ]


    # ---------------------------------

    def search_history(
        self,
        keyword
    ):
        """
        Search history records.
        """

        result = []


        for record in self.history:

            if keyword.lower() in str(record).lower():

                result.append(record)


        return result


    # ---------------------------------

    def clear_history(self):

        self.history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    history = ScheduleHistory()


    history.add_record(
        "Daily AI Task",
        "completed",
        "Task executed successfully"
    )


    print(
        history.get_history()
    )
