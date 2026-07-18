def memory():
    print("=== DG AI Memory ===")

    name = input("Enter your name: ")

    with open("memory.txt", "w") as file:
        file.write(name)

    print("Memory saved successfully.")
def memory():
    name = input("Enter your name: ")
    print("Hello,", name)
# DG AI Memory System

def save_memory():

    data = input("What should DG AI remember? ")

    file = open("memory.txt", "a")

    file.write(data + "\n")

    file.close()

    print("Memory saved successfully")


def show_memory():

    file = open("memory.txt", "r")

    print("\nDG AI Memory:")

    for line in file:
        print("-", line.strip())

    file.close()


def memory():

    while True:

        print("\n--- Memory Menu ---")
        print("1. Save Memory")
        print("2. Show Memory")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
            save_memory()

        elif choice == "2":
            show_memory()

        elif choice == "3":
            break

        else:
            print("Invalid choice")
