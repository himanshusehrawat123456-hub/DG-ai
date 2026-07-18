# DG AI Storage System

def save_data(filename, data):

    file = open(filename, "a")

    file.write(data + "\n")

    file.close()

    print("Data saved successfully")


def read_data(filename):

    file = open(filename, "r")

    print("\nSaved Data:")

    for line in file:
        print("-", line.strip())

    file.close()
