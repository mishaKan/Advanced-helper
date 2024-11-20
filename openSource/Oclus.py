import json
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
     print("exepted")
doSave()
