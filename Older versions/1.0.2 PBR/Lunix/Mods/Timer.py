import time
import os

c = "clear"
while True:
  print("The not useless timer")
  print("")
  print("Type in for how long its going to be")
  t = input("Type here >> ")
  os.system(c)
  print("Do you want to give it an custom message?")
  print("(if not just press enter!)")
  custom = input("Custom message >> ")
  os.system(c)
  print
  
  time.sleep(int(t))

  print("Your timer set for", t, "Seconds is over!")
  print("Times up")
  print(custom)
  input("Press ENTER to go back to the main menu")
  