"""
DG AI Version 1
Access Logger

Purpose:
- Track file access activity
- Store security logs
- Monitor user actions

Version: 1.0
"""

import logging
from datetime import datetime


class AccessLogger:
    """
    Professional File Access Logger
    """

    def __init__(self):

        self.access_logs = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_log(
        self,
        user,
        file_name,
        action
    ):
        """
        Create access record.
        """

        record = {

            "user": user,

            "file": file_name,

            "action": action,

            "time": str(datetime.now())

        }


        return record


    # ---------------------------------

    def log_access(
        self,
        user,
        file_name,
        action
    ):
        """
        Save file access activity.
        """

        record = self.create_log(
            user,
            file_name,
            action
        )


        self.access_logs.append(
            record
        )


        logging.info(
            "File access recorded"
        )


        return record


    # ---------------------------------

    def search_logs(
        self,
        keyword
    ):
        """
        Search security logs.
        """

        results = []


        for log in self.access_logs:

            if keyword.lower() in str(log).lower():

                results.append(log)


        return results


    # ---------------------------------

    def get_logs(self):
        """
        Return all access logs.
        """

        return self.access_logs


    # ---------------------------------

    def get_file_history(
        self,
        file_name
    ):
        """
        Get specific file activity.
        """

        history = []


        for log in self.access_logs:

            if log["file"] == file_name:

                history.append(log)


        return history


    # ---------------------------------

    def clear_logs(self):
        """
        Clear access logs.
        """

        self.access_logs.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    logger = AccessLogger()


    print(
        logger.log_access(
            "Admin",
            "data.txt",
            "open"
        )
    )
