from graph import *
import random

def keyPressed(event):
  global dx, dy, V, x, y
  if event.keycode == VK_LEFT:
    V = 1
    dx = -V; dy = 0
    list.insert(1, (x, y))
  elif event.keycode == VK_RIGHT:
    V = 1
    dx = V; dy = 0
    list.insert(1, (x, y))
  elif event.keycode == VK_UP:
    V = 1
    dx = 0; dy = -V
    list.insert(1, (x, y))
  elif event.keycode == VK_DOWN:
    V = 1
    dx = 0; dy = V
    list.insert(1, (x, y))
  elif event.keycode == VK_SPACE:
    V = 0
    dx = dy = 0
  elif event.keycode == VK_ESCAPE:
    close()

def doMove():
  global dx, dy, obj, x, y, V
  deleteObject(obj)
  x += dx
  y += dy
  list[0] = (x, y)
  i = len(list) - 1
  A = list[i]
  B = list[i - 1]
  if A[0] >= B[0] - V and A[0] <= B[0] + V and A[1] >= B[1] - V and A[1] <= B[1] + V :
    list.pop()
    i -= 1
    A = list[i]
    B = list[i - 1]
    if A[0] == B[0]:
      if A[1] > B[1]:
        list[i] = (A[0], A[1] + V)
      else:
        list[i] = (A[0], A[1] - V)
    else:
      if A[0] > B[0]:
        list[i] = (A[0] + V, A[1])
      else:
        list[i] = (A[0] - V, A[1])
    A = list[i]
  if A[0] == B[0]:
    if A[1] > B[1]:
      list[i] = ( A[0], A[1] - V)
    else: list[i] = ( A[0], A[1] + V)
  else:
    if A[0] > B[0]:
      list[i] = (A[0] - V, A[1])
    else:
      list[i] = (A[0] + V, A[1])
  penColor("green")
  obj = polyline(list)

def eating():
  global Xe, Ye, eat, i, A, B, sqore, Sqore
  deleteObject(eat)
  if (x <= Xe + 8) and (x >= Xe - 3) and (y >= Ye - 3) and (y <= Ye + 8):
    Xe = random.randint(0, 490)
    Ye = random.randint(0, 590)
    i = len(list) - 1
    A = list[i]
    B = list[i - 1]
    if A[0] == B[0]:
      if A[1] > B[1]:
        list[i] = (A[0], A[1] + 20)
      else:
        list[i] = (A[0], A[1] - 20)
    else:
      if A[0] > B[0]:
        list[i] = (A[0] + 20, A[1])
      else:
        list[i] = (A[0] - 20, A[1])
    sqore += 1
  penColor("red")
  brushColor("red")
  eat = rectangle(Xe, Ye, Xe + 6, Ye + 6)
  Sqore = label (sqore, 45, 5, bg="blue", fg="red")

def wall ():
  global dx, dy, x, y, V
  if x < 5 and dx < 0:
    V = 0
    dx = 0
  if x > 495 and dx > 0:
    V = 0
    dx = 0
  if y < 5 and dy < 0:
    V = 0
    dy = 0
  if y > 595 and dy > 0:
    V = 0
    dy = 0

V = 0
L = 100
sqore = 0
Xe = random.randint(0,500)
Ye = random.randint(0,600)
print(Xe,Ye)
penSize(5)
penColor("green")
brushColor("blue")
windowSize(500, 600)
rectangle(0, 0, 500, 600)
x = 100; y = 100
dx = 0;  dy = 0
list = [(x, y),(x + L , y)]
obj = polyline(list)
brushColor("red")
eat = rectangle(Xe, Ye, Xe + 20, Ye + 20)
label("Sqore :", 5, 5, bg = "blue", fg = "red")
Sqore = label (sqore, 45, 5, bg = "blue", fg = "red")


onKey(keyPressed)
onTimer(wall, 100)
onTimer(doMove, 10)
onTimer(eating, 100)
run()