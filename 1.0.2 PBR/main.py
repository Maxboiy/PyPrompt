import time
import sys
import os

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.20)

delay_print("PyPrompt")
print("")
print("Version 1.0.2 PBR")
print()
print("Type help to get a list for commands.")

while True:
    mainmenu = input("C:/> ")
    
    if mainmenu == "help":
        print("------------PyPromptOS------------")
        print("help   // Shows this list of commands.")
        print("dir    // Shows the directory.")
        print("cls    // Will cls the screen")
        print("echo   // Will repeat your message")
        print("quit   // This will quit the Script")
        print("cd     // Will bring you to an other directory")
        print("run    // Will run an Program")
        print("reboot // This will reboot the program for changes made to the script.")
        print("load   // This does nothing but give you an fake loading screen.")
        print("show   // Will show you the text from a text file")
        print("WN     // Will show a list of What's new")
        print("BHelp  // Shows how you are able to use the command")
        print("------------PyPromptOS------------")
        

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
        os.chdir(cd)

    elif mainmenu == "run":
        print("What is the full name of the file?")
        runprogram = input("File name >> ")
        os.system('%s %s' % ('python', runprogram))

    elif mainmenu == "reboot":
      os.system("cls")
      os.system("python main.py")

    elif mainmenu == "load":
      os.system("python load.py")

    elif mainmenu == "show":
        print("Which text file do you want to read?")
        show = input("full text file >> ")
        os.system('%s %s' % ('more', show))

    elif mainmenu == "WN":
        os.system('more Whatsnew.txt')


        
        
    else:
      print(mainmenu, "is an invalid command!")