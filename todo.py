def todo():
    print("=== DG AI To-Do List ===")

    task = input("Enter a task: ")

    with open("todo.txt", "a") as file:
        file.write(task + "\n")

    print("Task saved successfully.")
# DG AI Todo System

tasks = []
completed_tasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added successfully!")


def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, task)


def remove_task():
    show_tasks()
    
    number = int(input("Enter task number to remove: "))

    if number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(removed, "removed")
    else:
        print("Invalid task number")

def edit_task():

    show_tasks()

    number = int(input("Enter task number to edit: "))

    if number <= len(tasks):

        new_task = input("Enter new task: ")

        tasks[number - 1] = new_task

        print("Task updated successfully")

    else:
        print("Invalid task number")

def complete_task():

    show_tasks()

    number = int(input("Enter task number completed: "))

    if number <= len(tasks):

        task = tasks.pop(number - 1)

        completed_tasks.append(task)

        print("Task completed successfully")

    else:
        print("Invalid task number")
        


while True:

    print("\n--- DG AI Todo Menu ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Edit Task")
    print("5. Complete Task")
    print("6. Back")

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
        break

    else:
        print("Invalid choice")
