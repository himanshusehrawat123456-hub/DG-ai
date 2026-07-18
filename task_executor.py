"""
DG AI Version 1
Task Executor

Purpose:
- Execute tasks
- Update task status

Version: 1.0
"""

import datetime


class TaskExecutor:
    """
    Handles task execution.
    """

    def __init__(self):
        self.execution_history = []

    def execute_task(self, task):

        task["status"] = "Completed"

        record = {
            "task_id": task["id"],
            "title": task["title"],
            "status": task["status"],
            "executed_at": str(datetime.datetime.now())
        }

        self.execution_history.append(record)

        return record

    def get_execution_history(self):

        return self.execution_history

    def clear_history(self):

        self.execution_history.clear()

        return True


# Testing

if __name__ == "__main__":

    executor = TaskExecutor()

    sample_task = {
        "id": 1,
        "title": "Build DG AI",
        "status": "Pending"
    }

    print(
        executor.execute_task(
            sample_task
        )
    )
