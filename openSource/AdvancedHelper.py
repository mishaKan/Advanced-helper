import tkinter.colorchooser,os,tkinter,json,io,PIL,base64,time
from PIL import Image
from pathlib import Path
import pyperclip as cl
import flet as ft

data = {"bg_col" : "#2f3048"}
dataJsonName = "save.json"

#images bytes 
#images
sellectTheamImg = Image

#settings
theamColorBtnSize = 50

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


def main(page : ft.Page):
    global bg,coeff,pagebgcolor
    def chooseColor(e):
        global pagebgcolor
        chooseBg = tkinter.colorchooser.askcolor()
        data["bg_col"] = chooseBg[1]
        pagebgcolor = ft.colors.with_opacity(1,data["bg_col"])
        doSave()
        pagebgcolor = ft.colors.with_opacity(1,chooseBg[1])
        getSave()
        page.bgcolor = ft.colors.with_opacity(1,data["bg_col"])
        page.update()
    page.window.bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.with_opacity(1,data["bg_col"])
    page.controls.append(ft.Text(value="Hello, user!",color="cyan"))
    path = Path(__file__).parent
    page.expand=True
    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    width=50,
                    height=50,
                    content=ft.IconButton(icon=ft.icons.PALETTE_OUTLINED,scale=6,icon_size=10,alignment=ft.alignment.center,highlight_color=ft.colors.RED_500,disabled_color=ft.colors.TRANSPARENT,on_click=chooseColor,data=0),
                    margin=ft.margin.only(top=500,left=10),
                    border_radius=20,
                )
            ],
        )
    )
    page.update()
        
ft.app(target=main)
while(True):
    getSave()
    
