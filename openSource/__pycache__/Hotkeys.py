import keyboard,webbrowser,time

keyBindPressed = {"yt" : False}
def do():
    if(keyboard.is_pressed("ctrl+y")):
        if(keyBindPressed["yt"] == False):
            webbrowser.open("https://www.youtube.com/")
            keyBindPressed["yt"] = True
    else:
        keyBindPressed["yt"] = False        