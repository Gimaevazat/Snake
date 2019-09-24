from graph import *
import random

#скорость змеи в зависимости от нажатой кнопки
#При нажатии кнопки змея поворачивает, и в это время в list заносится пара головы(это же пара поворота). Эта пара заносится сразу после пары головы
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

#отрисовка змеи
def doMove():
  global dx, dy, obj, x, y, V
  #удаление старой змеи
  deleteObject(obj)
  x += dx
  y += dy
  #установка нового положения головы
  list[0] = (x, y)
  #i - номер конца змеи в массиве
  i = len(list) - 1
  A = list[i]
  B = list[i - 1]
  if A[0] >= B[0] - V and A[0] <= B[0] + V and A[1] >= B[1] - V and A[1] <= B[1] + V : #если конец совпал с первым поворотом, то удаляем первый поворот
    list.pop()
    i -= 1
    A = list[i]
    B = list[i - 1]
    #без следующих условий конец догонял голову
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
  #движение конца в сторону первого поворота
  if A[0] == B[0]:
    if A[1] > B[1]:
      list[i] = ( A[0], A[1] - V)
    else: list[i] = ( A[0], A[1] + V)
  else:
    if A[0] > B[0]:
      list[i] = (A[0] - V, A[1])
    else:
      list[i] = (A[0] + V, A[1])
  #отрисовка новой змеи
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

#проверка на удар об стену
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

V = 0     #скорость змеи
L = 100     #длина змеи, во время поедания увеличивается
sqore = 0     #счёт
Xe = random.randint(0,500)    #первая еда
Ye = random.randint(0,600)
penSize(5)
penColor("green")
brushColor("blue")
windowSize(500, 600)
rectangle(0, 0, 500, 600)
x = 100; y = 100
dx = 0;  dy = 0
list = [(x, y),(x + L , y)]     #list - массив, в котором хранятся пары. Пара состоит из координат. Каждая пара это либо хвост, либо голова, либо поворот
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