"""
DG AI Version 1
Scheduler Manager System

Purpose:
- Manage scheduled tasks
- Store schedule records

Version: 1.0
"""


import datetime



class SchedulerManager:
    """
    Handles scheduler operations.
    """



    def __init__(self):

        self.schedules = []



    def create_schedule(self, task_name, schedule_time):
        """
        Create new schedule.
        """

        schedule = {

            "id":
            len(self.schedules) + 1,

            "task":
            task_name,

            "time":
            schedule_time,

            "status":
            "Scheduled",

            "created_at":
            str(datetime.datetime.now())

        }


        self.schedules.append(schedule)


        return schedule



    def get_schedules(self):
        """
        Return all schedules.
        """

        return self.schedules



    def cancel_schedule(self, schedule_id):
        """
        Cancel schedule.
        """

        for item in self.schedules:

            if item["id"] == schedule_id:

                item["status"] = "Cancelled"

                return True


        return False




# Testing

if __name__ == "__main__":


    scheduler = SchedulerManager()


    print(
        scheduler.create_schedule(
            "Daily Backup",
            "10:00 AM"
        )
    )
