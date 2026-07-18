def notes():
    print("=== DG AI Notes ===")

    note = input("Write your note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved successfully.")
