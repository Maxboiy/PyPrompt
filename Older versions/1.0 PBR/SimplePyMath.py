import time
import os

os.system("clear")
print("-----SimplePyMath-----")
print("Welcome to SimplePyMath")
print("Version 1.0 First Public Release")
print("")
print("[1] | Start")
print("[2] | Settings")
print("[3] | Exit")
print("-----SimplePyMath-----")
MainMenu = input("Select Here | >> ")
os.system("clear")

if MainMenu == "1":
  while True:
    os.system("clear")
    print("-----SimplePyMath-----")
    Mathandstuff = input("What is your Math question? >> ")
    print("Your answer is:")
    print(eval(Mathandstuff))
    print("-----SimplePyMath-----")
    input("Press Enter to Continue")
    os.system("clear")
    
elif MainMenu == "2":
  os.system("clear")
  print("-----SimplePyMath-----")
  print("[1] | One-Time use only! ")
  print("[2] | Credits")
  print("[3] | How does it work?")
  print("[4] | Untitled Slot (Coming more Soon!)")
  print("[5] | Back")
  print("-----SimplePyMath-----")
  Settings = input("Select Here | >> ")
  os.system("clear")

  if Settings == "1":
    os.system("clear")
    print("-----SimplePyMath-----")
    Mathandstuff = input("What is your Math question? >> ")
    print("Your answer is:")
    print(eval(Mathandstuff))
    print("-----SimplePyMath-----")
    input("Press Enter to Continue")
    os.system("clear")
    
  elif Settings == "2":
    os.system("clear")
    print("-----SimplePyMath-----")
    print("Credits")
    print("Programmed and Produced")
    print("by @Maxboiy on Replit")
    print("-----SimplePyMath-----")
    input("Press Enter to go Back.")
    os.system("python main.py")
    os.system("clear")

  elif Settings == "3":
    os.system("clear")
    print("-----SimplePyMath-----")
    print("It works like this")
    print(" / Is : >>examples 30/3 = 10.0<<")
    print(" * Is x >>examples 3*10 = 30<<")
    print(" + Is the same >>examples 30+5 = 35<<")
    print("-----SimplePyMath-----")
    input("Press Enter to go Back.")
    os.system("python main.py")
    os.system("clear")

  elif Settings == "4":
    os.system("clear")
    print("-----SimplePyMath-----")
    print("you really thought this is really gonna work did you?")
    print("[1] | Yes")
    print("[2] | No")
    input("Select Here | >> ")
    print("-----SimplePyMath-----")
    os.system("clear")
    print("-----SimplePyMath-----")
    print("Well its not going to work")
    print("[1] | Continue")
    print("[2] | Back to MainMenu")
    print("-----SimplePyMath-----")
    EmptyMenu = input("Select Here | >> ")
    if EmptyMenu == "1":
      os.system("clear")
      print("-----SimplePyMath-----")
      print("Its Still not going to do Nothing")
      print("[1] | Continue")
      print("[2] | Back to MainMenu")
      print("-----SimplePyMath-----")
      EmptyMenu1 = input("Select Here | >> ")
      
      if EmptyMenu1 == "1":
        os.system("clear")
        print("-----SimplePyMath-----")
        print("Okay i give up, You win. Heres your Secret Egg.")
        print("[1] | Continue")
        print("[2] | Back to MainMenu")
        print("-----SimplePyMath-----")
        EmptyMenu2 = input("Select Here | >> ")

        if EmptyMenu2 == "1":
          os.system("clear")
          print("-----SimplePyMath-----")
          print("Today is a Saterday, So i dont want to work hard")
          print("[1] | Continue")
          print("[2] | Back to MainMenu")
          print("-----SimplePyMath-----")
          EmptyMenu3 = input("Select Here | >> ")

          if EmptyMenu3 == "1":
            os.system("clear")
            print("-----SimplePyMath-----")
            print("im Lazy, Get it?")
            print("[1] | Continue")
            print("[2] | Back to MainMenu")
            print("-----SimplePyMath-----")
            EmptyMenu4 = input("Select Here | >> ")

            if EmptyMenu4 == "1":
              os.system("clear")
              print("-----SimplePyMath-----")
              print("Wait are you even paying attantion")
              print("[1] | Continue")
              print("[2] | Back to MainMenu")
              print("-----SimplePyMath-----")
              EmptyMenu5 = input("Select Here | >> ")

              if EmptyMenu5 == "1":
                os.system("clear")
                print("-----SimplePyMath-----")
                print("Anyway have fun with your Secret egg")
                print("[1] | Activate Secret egg")
                print("-----SimplePyMath-----")
                EmptyMenu6 = input("Select Here | >> ")

                if EmptyMenu6 == "1":
                  os.system("clear")
                  print("-----SimplePyMath-----")
                  print("Activated Secret")
                  print("-----SimplePyMath-----")
                  input("Press Enter to Continue")
                  os.system("clear")

                  while True:
                    os.system("clear")
                    print("Theres still no Secret egg.")
                    input("Press Enter to Continue")
                    os.system("clear")
                    print("Now this is a loop, Have fun!")
                    input("Press Enter to Continue")
        
              elif EmptyMenu5 == "2":
                os.system("python main.py")
            
            elif EmptyMenu4 == "2":
              os.system("python main.py")
        
          elif EmptyMenu3 == "2":
            os.system("python main.py")
        
        elif EmptyMenu2 == "2":
          os.system("python main.py")

      elif EmptyMenu1 == "2":
        os.system("python main.py")
  
    elif EmptyMenu == "2":
      os.system("python main.py")

  elif Settings == "5":
    os.system("python main.py")