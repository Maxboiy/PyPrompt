import sys
import os
import json
import webbrowser

dirfolder = "_files"
pyscript = "_files/main.py"
setupfileno = "setup.json"
userpath = "%USERPROFILE%" 
setupfile = "C:/Users/Public/PyPrompt/setup.json"
pyprompt = "Checking PyPrompt... not Found!"
filescheck = "Checking files... not found!"
programfile = "Checking program files... not found!"
setupdia = "Setup file... not found!"
setup1 = "Entering setup..."

print("------------PyPrompt------------")
print("PyPrompt will shortly begin after this!")

# Checking for the files
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
# Found the files
if base_path == base_path:
    filescheck = "Checking files... found!"

print(filescheck)

# Checking for the PyPrompt script
usedfiles = os.path.join(base_path, pyscript)
if os.path.exists(usedfiles):
    pyprompt = "Checking PyPrompt... found!"

else:
    print("")
    print("WARNING! starter.py didn't find PyPrompt!")
    print("Without PyPrompt this program can't start! If you didn't know\n")
    print("Troubleshot")
    print("[1] = go to the Github page")
    print("[2] = Give new location")
    print("[3] = Ignore warning and contine")
    print("[4] = Give up!")
    cfpy = input("recovery> ")
    if cfpy == "1":
        print("We are going to open the Github page!")
        print("https://github.com/Maxboiy/PyPrompt")
        print("open? [y/n]")
        agreepage = input("recovery/contine> ")
        if agreepage == "y":
            webbrowser.open("https://github.com/Maxboiy/PyPrompt")
        if agreepage == "n":
            print("Please restart this program!")
            input("recovery/quit>")
            ha_error

    elif cfpy == "2":
        print("WARNING: This is temporary and will not happen very time on boot")
        print("Where to look:", usedfiles)
        newlocation = input("recovery/location> ")
        pyscript = newlocation

    elif cfpy == "3":
        print("Continuing...")

    elif cfpy == "4":
        print("Are you giving up?")
        print("Never should you give up!\n")
        print("Do you want me to open some inspirational music? [y/n]")
        inspirationalmusic = input("recovery/give_up> ")
        if inspirationalmusic == "y":
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            print("GOT YOU!!! HAHAHHAHAHAHA")
            input("recovery/give_up/troll> ")
            youvebeenrickrolled
        if inspirationalmusic == "n":
            print("Its sad to see you go! :,(")
            input("recovery/quit> ")
            goodbye

print(pyprompt)

# Checking for the files used by PyPrompt
useddir = os.path.join(base_path, dirfolder)
if os.path.exists(useddir):
    programfile = "Checking program files... found!"

print(programfile)

# Checking for setup file

if os.path.exists(setupfile):
    with open(setupfile, "r") as f:
        data = json.load(f)
    for setup in data["setup"]:
        if setup["done"] == "True":
            setupdia = "Setup file... found!"
            setup1 = "Skipping setup..."   
            print(setupdia)
            print(setup1)    

else:
    os.system("cls")
    print("------------PyPrompt/Setup------------")
    print("Welcome to PyPrompt!\n")
    print("PyPrompt is an terminal recreation but in Python")
    print("It might not have all the features as an normal terminal")
    print("but hey! atleast it works... for the most part\n")
    print("Press enter to contine.")
    input("------------\033[0;30;47mContinue\033[0m------------")
    os.system("cls")
    print("------------PyPrompt/Setup------------")
    print("Hello there! this start program creates an file which auto skips the setup")
    print("But we want permission from you to know if we can save setup.json in the Public user folder.")
    print("If you decline, you will have to do the setup everytime you start PyPrompt")
    print("DIR >>", setupfile)
    print()
    print("[yes/no]")
    permissionneed = input("Permission>")
    if permissionneed == "yes":
        os.system("cls")
        print("------------PyPrompt/Setup------------")
        print("Thank you! The file will be created once setup is completed.\n")
        input("------------\033[0;30;47mContinue\033[0m------------")
    elif permissionneed == "no":
        print("------------PyPrompt/Setup------------")
        print("The setup.json file will be saved in the temp folder!\n")
        input("------------\033[0;30;47mContinue\033[0m------------")
    os.system("cls")
    print("------------PyPrompt/Setup/help------------")
    print("1. Terminal in terminal")
    print("Some commands are there own terminals, meaning they will have there own commands and doesn't work like the main terminal")
    print("the commands that are there own terminal will have an (T) at the end of there name\n")
    print("Type skip to skip this part!\n")
    print("Try it out!\n")
    while True:
        print("Type run")
        sample1 = input("pyprompt/sample1> ")
        if sample1 == "run":
            print("Goodjob! Your now inside the other terminal. But how do you get out?\n")
            print("Type exit")
            sample1_run = input("run\>")   
            if sample1_run == "exit":
                break
            else:
                print(sample1_run, "does not work! ") 
        elif sample1 == "skip":
            break
        else:
                print(sample1, "does not work!") 
    print("And thats the basics of the terminal commands")
    print("Press enter to contine.")
    input("------------\033[0;30;47mContinue\033[0m------------")
    setupw = {"setup": [{"done": "True"}] }
    if permissionneed == "yes":
        permsave = os.path.join(userpath, setupfile)
        if os.path.exists("C:/Users/Public/PyPrompt"):
            with open(permsave, "w") as f:
                json.dump(setupw, f)
        else:
            os.mkdir('C:/Users/Public/PyPrompt')
            with open(permsave, "w") as f:
                json.dump(setupw, f)

    elif permissionneed == "no":
        tempsave = os.path.join(useddir, setupfileno)
        with open(tempsave, "w") as f:
            json.dump(setupw, f)

    os.system('%s %s' % ("python", usedfiles))
    
os.system("%s %s" % ("python", usedfiles))
        


