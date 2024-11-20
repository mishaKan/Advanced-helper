import json,rich,os,PIL
from PIL import Image
from rich.console import Console
import Loop
data = {"bg_col" : "#2f3048"}
dataJsonName = "save.json"

def getSave():
    global data,pagebgcolor
    with open(dataJsonName,"r",encoding="utf-8") as saves:
        data = json.load(saves)
def doSave():
    global data,pagebgcolor
    with open(dataJsonName,"w") as saves:
        json.dump(data,saves,indent=5,ensure_ascii=False)
try:
    getSave()
except:
     pass
doSave()

console = Console()



def start():
    console.print("[bold green] hello")
start()
def main():
    pass
    
while(True):
    main()