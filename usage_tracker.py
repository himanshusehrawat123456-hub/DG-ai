"""
DG AI Version 1
Usage Tracker System

Purpose:
- Track DG AI usage
- Store user activity records

Version: 1.0
"""


import datetime



class UsageTracker:
    """
    Handles usage tracking operations.
    """



    def __init__(self):

        self.activities = []



    def track_usage(self, user_id, action):
        """
        Track user activity.
        """

        activity = {

            "id":
            len(self.activities) + 1,

            "user_id":
            user_id,

            "action":
            action,

            "time":
            str(datetime.datetime.now())

        }


        self.activities.append(activity)


        return activity



    def get_usage(self):
        """
        Return usage records.
        """

        return self.activities



    def clear_usage(self):
        """
        Clear usage history.
        """

        self.activities.clear()

        return True




# Testing

if __name__ == "__main__":


    tracker = UsageTracker()


    print(
        tracker.track_usage(
            "user1",
            "Used DG AI Chat"
        )
    )
