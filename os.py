import pyttsx3
import os

pyttsx3.speak("welcome to my tool, which is an OS Based program into Menu Driven using Python")
print("\n\t>>> : An OS Based program into Menu Driven using Python : <<<")
print("\t-------------------------------------------------------------")
print("\n")

while True:
    print("chat with me with your requirements : ", end='')
    p = input()

    if ("run" in p) and ("chrome" in p):
        os.system("chrome")

    elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
        os.system("notepad")

    elif ("run" in p) and ("player" in p) and ("media" in p):
        os.system("vlc player")

    elif ("run" in p) and ("file " in p) and ("manager" in p):
        os.system("start..")

    elif ("run" in p) and ("vm" in p) and ("box" in p):
        os.system("VirtualBox")

    elif ("firefox" in p) and (("run" in p) or ("start" in p)):
        os.system("start firefox")

    elif  ("run" in p ) and (("ms" in p) or ("microsoft" in p)):
        if "excel" in p:
            os.system("start excel")
        elif "word" in p:
            os.system("start winword")
        elif "power point" in p or "ppt" in p or "powerpoint" in p:
            os.system("start powerpnt")

    elif ("telegram" in p) or ("tele" in p):
        os.system("start telegram")

    elif ("exit" in p) or ("quit" in p):
        break

    else:
        print("don't support")

print("\t\t\n > Thank You :)")
pyttsx3.speak("Thank you for using it, Have a good day.")