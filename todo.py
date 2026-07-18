def todo():
    print("=== DG AI To-Do List ===")

    task = input("Enter a task: ")

    with open("todo.txt", "a") as file:
        file.write(task + "\n")

    print("Task saved successfully.")
