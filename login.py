def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("Login Successful!")
    else:
        print("Wrong username or password.")
