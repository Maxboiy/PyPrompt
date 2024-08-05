import time
import sys
import os
import webbrowser
import random

pathtofile = "temp folder"
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
setuptemp = "_files/setup.json"
pathtown = "Whatsnew.txt"
pathtown1 = os.path.join(base_path, pathtown)
pathtosetup = os.path.join(base_path, setuptemp)
pathtonontemp = "C:/Users/Public/PyPrompt/setup.json"

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.20)

os.system("cls")
delay_print("PyPrompt")
print("")
print("Version 1.4 PBR")
print()
print("Type help to get a list for commands.")

while True:
    command = input("#/> ")
    
    if command == "help":
        print("------------PyPrompt------------")
        print("help     // Shows this list of commands.")
        print("dir      // Shows the directory.")
        print("clear    // Will cls the screen")
        print("exit     // This will quit the Script")
        print("cd       // Will bring you to an other directory")
        print("run   (T)// Will allow you to run files")
        print("show  (T)// Will show you the text from a text file")
        print("wn       // Will show a list of What's new")
        print("settings // Will open the settings")
        print("------------PyPrompt------------")
    
    elif command == "cd":
        cd = input("cd_dir/>")
        os.chdir(cd)

    elif command == "clear":
        os.system("cls")

    elif command == "exit":  
        break

    elif command == "dir":
        os.system("dir")

    elif command == "run":
        os.system("cls")
        print("Welcome to run! use 'help' to see all active commands ")
        print("If you wanna run python code put python before the name of file")
        print("else it will open in text editor")
        while True:
            run = input("run/>")
            if run == "help":
                print("------------PyPrompt/run------------")
                print("dir     // Will show all files expect .uselessfileextensionthatwillprobablyneverbeusedbecauseimwrittingthisat1130pmandisalsomadebymbd1343 sorry!")
                print("cd      // Allows you to go to different folders")
                print("exit    // Will bring you back to the main terminal")
                print("cexit   // Will clear the console and also exit back to the main terminal")
                print("------------PyPrompt/run------------")

            elif run == "dir":
                os.system("dir /B/A-D | findstr /EILV '.uselessfileextensionthatwillprobablyneverbeusedbecauseimwrittingthisat1130pmandisalsomadebymbd1343'")
            
            elif run == "cd": 
                os.system("dir /a:d ")
                print("Please enter which folder you want")
                foldercd = input("run_folder/>")
                if foldercd == "":
                    print("Prompt is empty!")

                elif foldercd == "..":
                    print("This currently doesn't work :( I blame os.chdir!")

                elif foldercd == ".":
                    print("This currently doesn't work :( I blame os.chdir!")
                
                else:
                 os.chdir(foldercd)

            elif run == "exit":
                break

            elif run == "cexit":
                os.system("cls")
                break

            else:
                os.system(run)

    elif command == "show":
        os.system("cls")
        print("Welcome to show! use 'help' to see all active commands ")
        while True:
            show = input("show/>")
            if show == "help":
                print("------------PyPrompt/show------------")
                print("this is kinda the same as run but here you read the contents of the file and not run it")
                print("------------PyPrompt/show------------")
                print("dir     // Will show all files expect .uselessfileextensionthatwillprobablyneverbeusedbecauseimwrittingthisat1130pmandisalsomadebymbd1343 sorry!")
                print("cd      // Allows you to go to different folders")
                print("exit    // Will bring you back to the main terminal")
                print("cexit   // Will clear the console and also exit back to the main terminal")
                print("------------PyPrompt/show------------")

            elif show == "dir":
                os.system("dir /B/A-D | findstr /EILV '.uselessfileextensionthatwillprobablyneverbeusedbecauseimwrittingthisat1130pmandisalsomadebymbd1343'")
            
            elif show == "cd": 
                os.system("dir /a:d ")
                print("Please enter which folder you want")
                foldercd = input("show_folder\>")
                if foldercd == "":
                    print("Prompt is empty!")
                else:
                    os.chdir(foldercd)

            elif show == "..":
                    print("This currently doesn't work :( I blame os.chdir!")

            elif show == ".":
                print("This currently doesn't work :( I blame os.chdir!")

            elif show == "exit":
                break

            elif show == "cexit":
                os.system("cls")
                break
            
            elif show == "":
                print("Prompt is empty! Maybe type something?")

            else:
                os.system('%s %s' % ("more", show))

    elif command == "wn":
        os.system('%s %s' % ("more", pathtown1))

    elif command == "settings":
        os.system("cls")
        print("------------\033[0;30;47mPyPrompt/Settings\033[0m------------")
        print("Welcome to the settings menu! What can we do for you?")
        while True:
            print("[1] = General")
            print("[2] = Credits & Info")
            print("[3] = Exit")
            settingsmenu = input("#/Settings/>")
            if settingsmenu == "1":
            
                os.system("cls")
                print("------------\033[0;30;47mPyPrompt/Settings/General\033[0m------------")
                print("Settings/General Basic settings for PyPrompt")
                while True: 
                    print("[1] = Delete setup file")
                    print("[2] = Go back")
                    genesettings = input("#/S/General>")
                    if genesettings == "1":
                        if os.path.exists(pathtonontemp):
                            pathtofile = "C:/Users/Public/PyPrompt/setup.json"
                        os.system("cls")
                        print("------------\033[0;30;47mConfirm\033[0m------------")
                        print("Are you sure you want to erase the setup file?")
                        print("By doing this you will have to do the setup again when you open this program\n")
                        print("Path to file:", pathtofile)
                        print("[y/n]")
                        while True:
                            eraseconfirm = input("Confirm> ")
                            if eraseconfirm == "y":
                                os.remove(pathtofile)
                                if os.path.exists(pathtofile):
                                    print("The file is not deleted! Something happend")
                                    input("------------\033[0;30;47mContinue\033[0m------------")
                                else:
                                    print("The file is successfully deleted!")
                                    input("------------\033[0;30;47mContinue\033[0m------------")
                                break
                            elif eraseconfirm == "n":
                                break
                    elif genesettings == "2":
                        break
            elif settingsmenu == "2":
                os.system("cls")
                print("------------\033[0;30;47mCredits & Info\033[0m------------")
                print("Version: 1.4 Public Beta Release | Change log >> [1]\n")
                print("Created by Maxboiy/MBD\n")
                print("Credits to:")
                print("the internet | Without it you would not have this program right now\n")
                print("Compiler:\n PyInstaller\n")
                print("Compile date:\n 5-August-2024\n")
                print("Open Github page \n [2]\n")
                print("[3] = Go back")
                while True:
                    candi = input("#/S/Info> ")
                    if candi == "1":
                        os.system('%s %s' % ("more", pathtown1))
                        print("[3] = Go back")
                    elif candi == "2":
                        webbrowser.open("https://github.com/Maxboiy/PyPrompt")
                    elif candi == "3":
                        break
                    elif candi == "4":
                        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                        print("Got you ;)")
            elif settingsmenu == "3":
                os.system("cls")
                print("------------\033[0;30;47mClose\033[0m------------")
                print("[1] = Go back to the program")
                print("[2] = Close the program")
                closeandquit = input("#/S/Quit> ")
                if closeandquit == "1":
                    break
                elif closeandquit == "2":
                    Programclosed

    else:
      print(command, "Invalid command! Maybe check for typos?")