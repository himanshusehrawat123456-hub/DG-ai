
# DG AI Login System


def login():

    username = input("Enter Username: ")

    password = input("Enter Password: ")


    if username == "admin" and password == "1234":

        print("Login Successful")

        return True

    else:

        print("Wrong Username or Password")

        return False
