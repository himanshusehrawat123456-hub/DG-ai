# DG AI Todo System

import storage

tasks = []
completed_tasks = []


def add_task():

    task = input("Enter task: ")

    tasks.append(task)

    storage.save_data("tasks.txt", task)

    print("Task added successfully")


def show_tasks():

    if len(tasks) == 0:
        print("No pending tasks")

    else:
        print("\nPending Tasks:")

        for i, task in enumerate(tasks, 1):
            print(i, task)


def remove_task():

    show_tasks()

    number = int(input("Enter task number to remove: "))

    if number <= len(tasks):

        removed = tasks.pop(number - 1)

        print(removed, "removed")

    else:
        print("Invalid number")


def edit_task():

    show_tasks()

    number = int(input("Enter task number to edit: "))

    if number <= len(tasks):

        new_task = input("Enter new task: ")

        tasks[number - 1] = new_task

        print("Task updated")

    else:
        print("Invalid number")


def complete_task():

    show_tasks()

    number = int(input("Enter completed task number: "))

    if number <= len(tasks):

        task = tasks.pop(number - 1)

        completed_tasks.append(task)

        print("Task completed")

    else:
        print("Invalid number")


def show_completed():

    if len(completed_tasks) == 0:
        print("No completed tasks")

    else:
        print("\nCompleted Tasks:")

        for task in completed_tasks:
            print("-", task)



def todo():

    while True:

        print("\n--- DG AI Todo ---")
        print("1. Add Task")
        print("2. Show Pending Tasks")
        print("3. Remove Task")
        print("4. Edit Task")
        print("5. Complete Task")
        print("6. Show Completed Tasks")
        print("7. Back")


        choice = input("Choose option: ")


        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            edit_task()

        elif choice == "5":
            complete_task()

        elif choice == "6":
            show_completed()

        elif choice == "7":
            break

        else:
            print("Invalid choice")
