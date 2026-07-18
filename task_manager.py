"""
DG AI Version 1
Task Management System

Purpose:
- Create and manage tasks
- Track task status
- Provide assistant task foundation

Version: 1.0
"""


import datetime



class TaskManager:
    """
    Handles DG AI task operations.
    """



    def __init__(self):

        self.tasks = []



    def create_task(self, title, priority="Normal"):
        """
        Create a new task.
        """

        task = {

            "id":
            len(self.tasks) + 1,

            "title":
            title,

            "priority":
            priority,

            "status":
            "Pending",

            "created":
            str(datetime.datetime.now())

        }


        self.tasks.append(task)


        return task



    def complete_task(self, task_id):
        """
        Mark task as completed.
        """

        for task in self.tasks:

            if task["id"] == task_id:

                task["status"] = "Completed"

                return True


        return False



    def get_tasks(self):
        """
        Return all tasks.
        """

        return self.tasks



    def remove_task(self, task_id):
        """
        Remove a task.
        """

        for task in self.tasks:

            if task["id"] == task_id:

                self.tasks.remove(task)

                return True


        return False



# Testing

if __name__ == "__main__":


    manager = TaskManager()


    manager.create_task(
        "Build DG AI Assistant",
        "High"
    )


    manager.create_task(
        "Learn Python",
        "Medium"
    )


    print(
        "DG AI Tasks:"
    )


    print(
        manager.get_tasks()
    )


    manager.complete_task(1)


    print(
        "\nUpdated Tasks:"
    )


    print(
        manager.get_tasks()
    )
