def memory():
    print("=== DG AI Memory ===")

    name = input("Enter your name: ")

    with open("memory.txt", "w") as file:
        file.write(name)

    print("Memory saved successfully.")
def memory():
    name = input("Enter your name: ")
    print("Hello,", name)
