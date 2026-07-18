def chat():
    print("Welcome to DG AI Chat")

    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("DG AI: Hello! How can I help you?")

        elif message == "your name":
            print("DG AI: My name is DG AI.")

        elif message == "bye":
            print("DG AI: Goodbye!")
            break

        else:
            print("DG AI: I don't understand that yet.")
