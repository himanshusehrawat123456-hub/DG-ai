print("Welcome to DG AI")
print("This is my first AI project")
print("Welcome to DG AI")

name = input("What is your name? ")

print("Hello", name)
print("Welcome to DG AI")
question = input("Ask DG AI: ")

if question == "hello":
    print("Hello! How are you?")
elif question == "your name":
    print("My name is DG AI.")
else:
    print("Sorry, I don't understand.")
age = input("What is your age? ")

print("You are", age, "years old.")
city = input("Which city do you live in? ")

print("You live in", city)

if city == "Delhi":
    print("Welcome, Delhi user!")
else:
    print("Welcome to DG AI!")
command = input("Enter command: ")

if command == "time":
    print("Time feature will be added soon.")
elif command == "date":
    print("Date feature will be added soon.")
elif command == "bye":
    print("Goodbye! See you again.")
else:
    print("Command not available.")
favorite = input("What is your favorite color? ")

if favorite == "red":
    print("Red is a powerful color.")
elif favorite == "blue":
    print("Blue is a calm color.")
elif favorite == "green":
    print("Green represents nature.")
else:
    print("That's a nice color!")
print("===== DG AI =====")
print("1. Say Hello")
print("2. Tell Your Name")
print("3. Exit")

choice = input("Choose an option: ")

if choice == "1":
    print("Hello! Welcome to DG AI.")
elif choice == "2":
    print("I am DG AI.")
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid choice.")
print("===== Calculator =====")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
else:
    print("Division by zero is not allowed.")
print("========== DG AI ==========")

while True:
    command = input("You: ")

    if command == "hello":
        print("DG AI: Hello! How can I help you?")

    elif command == "your name":
        print("DG AI: My name is DG AI.")

    elif command == "bye":
        print("DG AI: Goodbye!")
        break

    else:
        print("DG AI: I don't understand that command yet.")
print("========== DG AI MENU ==========")
print("1. Say Hello")
print("2. Calculator")
print("3. Exit")

choice = input("Choose an option: ")

if choice == "1":
    print("DG AI: Hello! Welcome.")

elif choice == "2":
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))

    print("Addition =", num1 + num2)
    print("Subtraction =", num1 - num2)
    print("Multiplication =", num1 * num2)

    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Cannot divide by zero.")

elif choice == "3":
    print("DG AI: Goodbye!")

else:
    print("Invalid Option.")
