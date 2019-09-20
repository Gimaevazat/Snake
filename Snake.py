from graph import *
def keyPressed(event):
    global  Vx, Vy
    if event.code == VK_LEFT:
        Vx = -1
    if event.code == VK_RIGHT:
        Vx = 1
    if event.code == VK_UP:
        Vy = -1
    if event.code == VK_DOWN:
        Vy = 1
def  update ():
    moveObjectBy(snake, Vx, Vy)
windowSize(800, 800)
canvasSize(800, 800)

x = 500
y = 500
Vx = 0
Vy = 0
brushColor("blue")
rectangle(0, 0, 1000, 1000)

brushColor("green")
penColor("green")
snake =  rectangle(x, y, x+20, y+20)

onTimer(update, 50)
onKey(keyPressed)
run()
