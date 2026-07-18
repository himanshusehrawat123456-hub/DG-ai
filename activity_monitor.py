"""
DG AI Version 1
Activity Monitor System

Purpose:
- Monitor system activities
- Store activity records

Version: 1.0
"""


import datetime



class ActivityMonitor:
    """
    Handles activity monitoring.
    """



    def __init__(self):

        self.activities = []



    def record_activity(self, module, action):
        """
        Record new activity.
        """

        activity = {

            "id":
            len(self.activities) + 1,

            "module":
            module,

            "action":
            action,

            "time":
            str(datetime.datetime.now())

        }


        self.activities.append(activity)


        return True



    def get_activities(self):
        """
        Return activity history.
        """

        return self.activities



    def clear_activities(self):
        """
        Clear activity history.
        """

        self.activities.clear()

        return True




# Testing

if __name__ == "__main__":


    monitor = ActivityMonitor()


    monitor.record_activity(
        "AI Core",
        "Response generated"
    )


    print(
        monitor.get_activities()
    )
