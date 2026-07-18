"""
DG AI Version 1
Task Creator

Purpose:
- Create new tasks
- Store task information

Version: 1.0
"""

import datetime


class TaskCreator:
    """
    Handles task creation.
    """

    def __init__(self):
        self.tasks = []

    def create_task(self, title, description, priority="Normal"):

        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "status": "Pending",
            "created_at": str(datetime.datetime.now())
        }

        self.tasks.append(task)

        return task

    def get_tasks(self):

        return self.tasks

    def clear_tasks(self):

        self.tasks.clear()

        return True


# Testing

if __name__ == "__main__":

    creator = TaskCreator()

    print(
        creator.create_task(
            "Build DG AI",
            "Create
