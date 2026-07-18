from chat import chat
from calculator import calculator

print("===== DG AI =====")
print("1. Chat")
print("2. Calculator")

choice = input("Choose: ")

if choice == "1":
    chat()
elif choice == "2":
    calculator()
else:
    print("Invalid Choice")
