import time
import sys
import os

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.20)

os.system("cls")
delay_print("PyPrompt")
print("")
print("Version 1.3 PBR")
print()
print("WARNING: If the program is renamed or")
print("placed out if its current folder some features might not work!")
print("")
print("Type help to get a list for commands.")

while True:
    mainmenu = input("#\> ")
    
    if mainmenu == "help":
        print("If this program is renamed or moved commands with >> will not work!")
        print("------------PyPromptOS------------")
        print("help     // Shows this list of commands.")
        print("dir      // Shows the directory.")
        print("cls      // Will cls the screen")
        print("echo     // Will repeat your message")
        print("exit     // This will quit the Script")
        print("cd       // Will bring you to an other directory")
        print("run      // Will run an Program >>")
        print("reboot   // This will reboot the program for changes made to the script. >>")
        print("fakeload // This does nothing but give you an fake loading screen. >>")
        print("show     // Will show you the text from a text file")
        print("wn       // Will show a list of What's new >>")
        print("bhelp    // Shows how you are able to use the command")
        print("pp")
        print("------------PyPromptOS------------")
        

    elif mainmenu == "clear":
        os.system("cls")

    elif mainmenu == "echo":
        print("What do you want it to repeat?")
        echo = input("Text >> ")
        os.system("cls")
        print(echo)

    elif mainmenu == "exit":  
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
      os.system("python main.py")

    elif mainmenu == "fakeload":
      os.system("python Mods\load.py")

    elif mainmenu == "show":
        print("Which text file do you want to read?")
        show = input("full text file >> ")
        os.system('%s %s' % ('more', show))

    elif mainmenu == "wn":
        os.system('more Whatsnew.txt')

    elif mainmenu == 'bhelp':
        print("------------PyPromptOS------------")
        print("Most commands need to be typed and then it should work")
        print("------------PyPromptOS------------")


    else:
      print(mainmenu, "is an invalid command!")