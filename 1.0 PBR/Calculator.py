import os

while True:
    os.system("cls")
    print("Calculator--")
    print("Plus = +")
    print("Exqels = ")

    Mathandstuff = input("What is your Math question? >> ")
    print("Your answer is:")
    print(eval(Mathandstuff))
    print("-----------------------")
    print("Type Q to Quit")
    input = input("Press Enter to Continue")
    os.system("cls")

    if input == "Q":
        break

    elif input == "q":
        break