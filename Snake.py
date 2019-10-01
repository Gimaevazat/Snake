from graph import *
import random

def keyPressed(event):
  global dx, dy, V, x, y
  if (event.keycode == VK_LEFT) and (head_check(1) is True):
    V = 1
    dx = -V; dy = 0
    list.insert(1, (x, y))
  elif (event.keycode == VK_RIGHT) and (head_check(2) is True):
    V = 1
    dx = V; dy = 0
    list.insert(1, (x, y))
  elif (event.keycode == VK_UP) and (head_check(3) is True) and (wall(2) is False):
    V = 1
    dx = 0; dy = -V
    list.insert(1, (x, y))
  elif (event.keycode == VK_DOWN) and (head_check(4) is True) and (wall(2) is False):
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
  if wall(1) is True:
    dx = V = 0
  if wall(2) is True:
    dx = V = 0
  if wall(3) is True:
    dy = V = 0
  if wall(4) is True:
    dy = V = 0
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
    Xe = random.randint(0, 390)
    Ye = random.randint(0, 390)
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
  Sqore = label (sqore, 45, 5, bg="black", fg="white")

def wall(side_number):  #1 - left ; 2 - right; 3 - up; 4 - down;
  wall_bool = False
  if (x < 10) and (dx < 0) and (side_number == 1):
    wall_bool = True
  elif (x > 390) and (dx > 0) and (side_number == 2) :
    wall_bool = True
  elif (y < 10) and (dy < 0) and (side_number == 3):
    wall_bool = True
  elif (y > 390) and (dy > 0) and (side_number == 4):
    wall_bool = True
  return wall_bool

def head_check(side_number):  #1 - left ; 2 - right; 3 - up; 4 - down;
  head_bool = False
  if (side_number == 1) and (list[0][0] - list[1][0] <= 0):
    head_bool = True
  elif (side_number == 2) and (list[0][0] - list[1][0] >= 0):
    head_bool = True
  elif (side_number == 3) and (list[0][1] - list[1][1] <= 0):
    head_bool = True
  elif (side_number == 4) and (list[0][1] - list[1][1] >= 0):
    head_bool = True
  return head_bool

def snake_check():
  length = len(list) - 2
  if list[0][0] == list[1][0]:
    for i in range(2, length, 2):

      if ((list[0][1] == list[i][1]) and (((list[0][0] >= list[i][0]) and (list[0][0] <= list[i+1][0]))
                                          or ((list[0][0] <= list[i][0]) and (list[0][1] >= list[i+1][0])))):
        print('kek')
        close()





V = 0
L = 100
sqore = 0
Xe = random.randint(0, 400)
Ye = random.randint(0, 400)
print(Xe, Ye)
penSize(5)
penColor("white")
brushColor("black")
windowSize(400, 400)
rectangle(0, 0, 400, 400)
x = 100
y = 100
dx = 0
dy = 0
list = [(x, y),(x + L , y)]
obj = polyline(list)
brushColor("red")
eat = rectangle(Xe, Ye, Xe + 20, Ye + 20)
label("Sqore :", 5, 5, bg="black", fg="white")
Sqore = label(sqore, 45, 5, bg="black", fg="white")


onKey(keyPressed)
#onTimer(wall, 100)
onTimer(doMove, 15)
onTimer(snake_check, 15)
onTimer(eating, 100)
run()