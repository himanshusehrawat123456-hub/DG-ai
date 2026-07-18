"""
DG AI Version 1
User Activity

Purpose:
- Track user activities
- Store activity history
- Monitor user actions

Version: 1.0
"""

import logging
from datetime import datetime


class UserActivity:
    """
    Professional User Activity Tracker
    """

    def __init__(self):

        self.activities = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_activity(
        self,
        user_id,
        action,
        details=None
    ):
        """
        Create activity record.
        """

        activity = {

            "user_id": user_id,

            "action": action,

            "details": details,

            "time": str(datetime.now())

        }


        return activity


    # ---------------------------------

    def add_activity(
        self,
        user_id,
        action,
        details=None
    ):
        """
        Save user activity.
        """

        activity = self.create_activity(
            user_id,
            action,
            details
        )


        self.activities.append(
            activity
        )


        logging.info(
            "User activity recorded"
        )


        return activity


    # ---------------------------------

    def get_user_activity(
        self,
        user_id
    ):
        """
        Get specific user history.
        """

        result = []


        for activity in self.activities:

            if activity["user_id"] == user_id:

                result.append(activity)


        return result


    # ---------------------------------

    def search_activity(
        self,
        keyword
    ):
        """
        Search activity records.
        """

        result = []


        for activity in self.activities:

            if keyword.lower() in str(activity).lower():

                result.append(activity)


        return result


    # ---------------------------------

    def get_all_activity(self):
        """
        Return all activities.
        """

        return self.activities


    # ---------------------------------

    def clear_activity(self):
        """
        Clear activity records.
        """

        self.activities.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    tracker = UserActivity()


    tracker.add_activity(
        1,
        "login",
        "User logged into DG AI"
    )


    print(
        tracker.get_all_activity()
    )
