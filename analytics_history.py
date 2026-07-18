"""
DG AI Version 1
Analytics History

Purpose:
- Store analytics recordstics_
- Track analysis results
- Maintain report history

Version: 1.0
"""

import logging
from datetime import datetime


class AnalyticsHistory:
    """
    Professional Analytics History Manager
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
        analysis_type,
        result,
        status="completed"
    ):
        """
        Add analytics record.
        """

        record = {

            "id":
            len(self.records) + 1,

            "type":
            analysis_type,

            "result":
            result,

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
        Return all analytics history.
        """

        return self.records


    # ---------------------------------

    def get_by_type(
        self,
        analysis_type
    ):
        """
        Get specific analysis records.
        """

        return [

            record for record in self.records

            if record["type"] == analysis_type

        ]


    # ---------------------------------

    def search_records(
        self,
        keyword
    ):
        """
        Search analytics history.
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

    history = AnalyticsHistory()


    history.add_record(
        "User Analysis",
        {
            "active_users": 100
        }
    )


    print(
        history.get_history()
    )
