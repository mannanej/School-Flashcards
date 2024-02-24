from subprocess import call
####################################################################################################################################
# Get imports installed
cmds = ["python -m ensurepip --upgrade", "py -m ensurepip --upgrade",
        "python -m pip install colorama", "py -m pip install colorama"]
for i in range(0, len(cmds), 2):
    cmd = call(cmds[i], shell = True)
    if cmd == 0:
        print("Python Success")
    else:
        cmd = call(cmds[i+1], shell = True)
        print("Py Success")
####################################################################################################################################
import os
from colorama import Fore, Style

def main():
    # Start of call to main()
    print("Hello World")
    return
####################################################################################################################################
# This is a call to main to get the ball rolling
if __name__ == '__main__':
    os.system("cls")
    print(Fore.YELLOW, "PROGRAM START", Style.RESET_ALL)
    main()
    print(Fore.YELLOW, "PROGRAM END", Style.RESET_ALL)
# END FILE
####################################################################################################################################