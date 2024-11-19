import tkinter.colorchooser,flet,os,tkinter,json,io,PIL,base64
from PIL import Image
from pathlib import Path
import pyperclip as cl

data = {"bg_col" : "#2f3048"}
dataJsonName = "save.json"

#images bytes 
#images
sellectTheamImg = Image

#settings
theamColorBtnSize = 50

def getSave():
    global data
    with open(dataJsonName,"r",encoding="utf-8") as saves:
        data = json.load(saves)
def doSave():
    global data
    with open(dataJsonName,"w") as saves:
        json.dump(data,saves,indent=5,ensure_ascii=False)
try:
    getSave()
except:
     print("exepted")
doSave()

def doToBytes():
    path = Path(__file__).parent
    
    cl.copy(base64.b64encode(open(str(path) + "\\selectTheam.png", "rb").read()))
#doToBytes()
def doToImage():
    global sellectTheamImg
    path = Path(__file__).parent
    #sellectTheamImg = Image.open(io.BytesIO(base64.b64decode(sellectTheam))).save(str(path)+"\\sellectedTheam.png")

#doToImage()

def chooseColor():
    chooseBg = tkinter.colorchooser.askcolor()
    data["bg_col"] = chooseBg[1]
    pagebgcolor = flet.colors.with_opacity(1,data["bg_col"])
    doSave()
    #chooseColor()
    getSave()
def main(page : flet.Page):
    global bg
    page.window.bgcolor = flet.colors.TRANSPARENT
    page.bgcolor = flet.colors.with_opacity(1,data["bg_col"])
    page.controls.append(flet.Text(value="Hello, user!",color="cyan"))
    path = Path(__file__).parent
    page.add(
        flet.Stack(
            width=100,
            height=100,
            controls=[
                flet.Positioned(
                    left=10,
                    top=10,
                    child=flet.Icon(flet.icons.FAVORITE, size=24)
                ),
                flet.positioned(
                    right=10,
                    bottom=10,
                    child=flet.Icon(flet.icons.FAVORITE, size=24, color=flet.colors.RED)
                )
            ]
        )
    )
    theamSellectButton = flet.IconButton(icon=flet.icons.PALETTE,icon_size=theamColorBtnSize)
    
    page.add(theamSellectButton)

    
    page.update()


flet.app(target=main)