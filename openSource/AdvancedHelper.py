from rich.console import Console
from rich import print
import random

console = Console
commands = ["help"]
commandsHelpList = ["help - help"]

def ConsoleSettings():
    print("[bold green]Hello user 😎")
def Init():
    ConsoleSettings()
Init()
def DoCommand(com = ""):        
    if(com == commands[0]): # help
        for i in commandsHelpList:
            print("[bold bright_yellow]" + i)

        
def DoAll():
    command = str(input())
    for curCommand in commands:
        if(curCommand == command):
            DoCommand(command)
            break
        else:
            if(curCommand != commands[len(commands) - 1]):
                continue
            else:
                print("[bold red]The command was not found 😔")
                DoAll()
                break


while(True):
    DoAll()