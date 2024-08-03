import os

while True:
    os.system("clear")
    print("Calculator--")
    print("+ = +")
    print("x = *")
    print(": = /")
    print("Type Q to Quit")
    print("Type Info for Credits and stuff")
    Menu = input("What is your Math question? >> ")
    print("Your answer is:")
    print(eval(Menu))
    print("-----------------------")
    input("Press Enter to Continue > ")
    os.system("clear")

    if Menu == "Q":
        break

    elif Menu == "Info":
      os.system("clear")
      print("Calculator--")
      print("Some code is used from another project!")
      print("SimplePyMath So credits to me, i guess?")
      print("--")
      print("Writen and made by @Maxboiy")
      print("---")
      print("This program is made for another project,") 
      print("PyPromptOS, But its still in Beta so do not expect for alot of features,")
      print("But you can wait right? Right??")
      input("Press Enter to continue")

    