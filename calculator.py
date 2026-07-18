def calculator():
    print("=== Calculator ===")

    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))

    print("Addition =", num1 + num2)
    print("Subtraction =", num1 - num2)
    print("Multiplication =", num1 * num2)

    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Cannot divide by zero.")
