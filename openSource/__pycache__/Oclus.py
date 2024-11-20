import json,rich,os,PIL
from PIL import Image
from rich.console import Console
import Loop
data = {"bg_col" : "#2f3048"}
dataJsonName = "save.json"
console = Console()
def getSave():
    global data
    with open(dataJsonName,"r",encoding="utf-8") as saves:
        data = json.load(saves)
def doSave():
    global data
    console.print(1)
    with open(dataJsonName,"w") as saves:
        json.dump(data,saves,indent=5,ensure_ascii=False)
try:
    getSave()
except:
     pass
doSave()





def start():
    console.print("[bold green] hello")
start()
def main():
    pass
    
while(True):
    main()