"""
DG AI Version 1
Calculator Tool

Purpose:
- Perform basic calculations
Version: 1.0
"""


class CalculatorTool:
    """
    Handles calculation operations.
    """

    def add(self, a, b):
        return a + b


    def subtract(self, a, b):
        return a - b


    def multiply(self, a, b):
        return a * b


    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"

        return a / b



# Testing

if __name__ == "__main__":

    calc = CalculatorTool()

    print(calc.add(10, 5))
    print(calc.subtract(10, 5))
    print(calc.multiply(10, 5))
    print(calc.divide(10, 5))
