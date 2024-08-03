import time
import sys
import os

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.20)

delay_print("PyPromptOS")
print("")
print("Version 1.0 PBR")
print()
print("Type help to get a list for commands.")

while True:
    mainmenu = input("C:/> ")
    
    if mainmenu == "help":
        print("------------PyPromptOS------------")
        print("'help' Shows this list of commands.")
        print("'dir' Shows the directory.")
        print("'clear' Will clear the screen")
        print("'echo' Will repeat your message")
        print("'quit' This will quit the Script")
        print("'cd' Will bring you to an other directory")
        print("'run' Will run an Program")

    elif mainmenu == "clear":
        os.system("cls")

    elif mainmenu == "echo":
        print("What do you want it to repeat?")
        echo = input("Text >> ")
        os.system("cls")
        print(echo)

    elif mainmenu == "quit":  
        break

    elif mainmenu == "dir":
        os.system("dir")

    elif mainmenu == "cd":
        print("Type in a folder name")
        cd = input("Name >> ")
        os.system('%s %s' % ('cd', cd))

    elif mainmenu == "run":
        print("What is the full name of the file?")
        runprogram = input("File name >> ")
        os.system('%s %s' % ('python', runprogram))
        
    else:
        print(mainmenu, "is invalid or not found")