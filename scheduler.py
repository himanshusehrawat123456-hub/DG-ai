# DG AI Scheduler System

import datetime


tasks = []


def add_task(task, time):

    tasks.append({

        "task": task,
        "time": time

    })

    print("Task scheduled:", task)



def show_tasks():

    print("===== DG AI Scheduled Tasks =====")


    if len(tasks) == 0:

        print("No tasks found")


    else:

        for item in tasks:

            print(
                "Task:",
                item["task"],
                "| Time:",
                item["time"]
            )



def current_time():

    now = datetime.datetime.now()

    print("Current Time:", now)
