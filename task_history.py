"""
DG AI Version 1
Task History

Purpose:
- Store completed task history
- View and manage task records

Version: 1.0
"""

import datetime


class TaskHistory:
    """
    Handles task history.
    """

    def __init__(self):
        self.history = []

    def add_history(self, task):
        """
        Add a completed task to history.
        """

        record = {
            "id": task["id"],
            "title": task["title"],
            "status": task["status"],
            "completed_at": str(datetime.datetime.now())
        }

        self.history.append(record)

        return record

    def get_history(self):
        """
        Return all task history.
        """

        return self.history

    def clear_history(self):
        """
        Clear task history.
        """

        self.history.clear()

        return True


# Testing

if __name__ == "__main__":

    history = TaskHistory()

    sample_task = {
        "id": 1,
        "title": "Build DG AI",
        "status": "Completed"
    }

    print(
        history.add_history(
            sample_task
        )
    )

    print(
        history.get_history()
    )
