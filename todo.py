def todo():
    print("=== DG AI To-Do List ===")

    task = input("Enter a task: ")

    with open("todo.txt", "a") as file:
        file.write(task + "\n")

    print("Task saved successfully.")
# DG AI Todo System

tasks = []

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


while True:

    print("\n--- DG AI Todo Menu ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("DG AI Todo Closed")
        break

    else:
        print("Invalid choice")
