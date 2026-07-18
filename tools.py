# DG AI Tools System

import datetime


def show_time():

    current_time = datetime.datetime.now()

    print("Current Time:", current_time)



def calculator_tool(a, b, operation):

    if operation == "add":

        return a + b


    elif operation == "subtract":

        return a - b


    elif operation == "multiply":

        return a * b


    elif operation == "divide":

        if b != 0:
            return a / b

        else:
            return "Cannot divide by zero"


    else:

        return "Invalid operation"



def welcome():

    print("Welcome to DG AI Tools")
