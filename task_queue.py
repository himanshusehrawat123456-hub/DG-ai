"""
DG AI Version 1
Task Queue

Purpose:
- Manage pending tasks
- Maintain execution order
- Handle task queue operations

Version: 1.0
"""

import logging
from datetime import datetime


class TaskQueue:
    """
    Professional Task Queue Manager
    """

    def __init__(self):

        self.queue = []

        self.completed_tasks = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def add_task(
        self,
        task_name,
        priority="normal"
    ):
        """
        Add task to queue.
        """

        task = {

            "id":
            len(self.queue) + 1,

            "name":
            task_name,

            "priority":
            priority,

            "status":
            "pending",

            "created":
            str(datetime.now())

        }


        self.queue.append(task)


        return task


    # ---------------------------------

    def get_next_task(self):
        """
        Get next pending task.
        """

        if self.queue:

            return self.queue[0]


        return None


    # ---------------------------------

    def complete_task(
        self,
        task_id
    ):
        """
        Mark task completed.
        """

        for task in self.queue:

            if task["id"] == task_id:

                task["status"] = "completed"

                task["completed"] = str(
                    datetime.now()
                )


                self.completed_tasks.append(
                    task
                )


                self.queue.remove(
                    task
                )


                return True


        return False


    # ---------------------------------

    def remove_task(
        self,
        task_id
    ):

        for task in self.queue:

            if task["id"] == task_id:

                self.queue.remove(task)

                return True


        return False


    # ---------------------------------

    def get_pending_tasks(self):

        return self.queue


    # ---------------------------------

    def get_completed_tasks(self):

        return self.completed_tasks



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    queue = TaskQueue()


    queue.add_task(
        "AI
