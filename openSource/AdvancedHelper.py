import flet,os

def main(page : flet.Page):
    page.window.bgcolor = flet.colors.TRANSPARENT
    bgCol = flet.colors.with_opacity(0.95,"#324AB2")
    page.bgcolor = bgCol
    page.controls.append(flet.Text(value="Hello, user!",color="cyan"))
    page.update()
flet.app(target=main)