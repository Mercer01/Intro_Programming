from graphics import *
import math
size = eval(input("Enter the common width and heght in terms of patches:"))
win_size = size * 100
win = GraphWin("coursework", win_size, win_size)
# for design and layout
penultimate_patchX = size - 1  # across
penultimate_patchY = size - 2  # down
# patch 1


y1 = 0
y2 = 100
y3 = 10
for a in range(size):
    x1 = 100
    x2 = 0
    x3 = 90
    for b in range(5):
        square = Rectangle(Point(x1, y1), Point(x2, y2))
        square.setFill("white")
        square.draw(win)
        square2 = Rectangle(Point(x3, y3), Point(x2, y2))
        square2.setFill("red")
        square2.draw(win)
        x1 = x1 - 20
        y1 = y1 + 20
        x3 = x3 - 20
        y3 = y3 + 20
    y2 = y2 + 100

x1 = 100
x2 = 0
x3 = 90
for c in range(size):
    for d in range(5):
        square = Rectangle(Point(x1, y1), Point(x2, y2))
        square.setFill("white")
        square.draw(win)
        square2 = Rectangle(Point(x3, y3), Point(x2, y2))
        square2.setFill("red")
        square2.draw(win)
        x1 = x1 - 20
        y1 = y1 + 20
        x3 = x3 - 20
        y3 = y3 + 20
    y1 = win_size - 200
    y2 = win_size - 100
    y3 = win_size - 190
    x1 = x1 + 200
    x2 = x2 + 100
    x3 = x3 + 200
x1 = 100
x2 = 0
x3 = 90
for e in range(size):
    for f in range(5):
        square = Rectangle(Point(x1, y1), Point(x2, y2))
        square.setFill("white")
        square.draw(win)
        square2 = Rectangle(Point(x3, y3), Point(x2, y2))
        square2.setFill("red")
        square2.draw(win)
        x1 = x1 - 20
        y1 = y1 + 20
        x3 = x3 - 20
        y3 = y3 + 20
    y1 = win_size - 100
    y2 = win_size
    y3 = win_size - 90
    x1 = x1 + 200
    x2 = x2 + 100
    x3 = x3 + 200

# patch 2
for i in range(penultimate_patchY):
    x1 = 100
    y1 = 0
    x2 = 120
    y2 = 0
    for a in range(3):
        for i in range(3):
            circle = Circle(Point(x1 + 10, y1 + 10), 10)
            circle.setFill("red")
            circle.setOutline("red")
            circle.draw(win)
            triangle = Polygon(
                Point(x1 + 20, y1), Point(x1 + 10, y1 + 10), Point(x1 + 20, y1 + 20))
            triangle.setFill("white")
            triangle.setOutline("white")
            triangle.draw(win)
            rect = Rectangle(Point(x2, y2), Point(x2 + 20, y2 + 20))
            rect.setFill("red")
            rect.setOutline("red")
            rect.draw(win)
            x1 = x1 + 42
            x2 = x2 + 42
        x1 = 100
        y1 = y1 + 40
        x2 = 120
        y2 = y2 + 40

    x1 = 120
    y1 = 20
    x2 = 130
    y2 = 30
    for i in range(2):
        for i in range(3):
            rect = Rectangle(Point(x1, y1), Point(x1 - 20, y1 + 20))
            rect.setFill("red")
            rect.setOutline("red")
            rect.draw(win)
            circle = Circle(Point(x1 + 10, y1 + 10), 10)
            circle.setFill("red")
            circle.setOutline("red")
            circle.draw(win)
            triangle = Polygon(Point(x2, y2), Point(
                x2 - 10, y2 - 10), Point(x2 - 10, y2 + 10))
            triangle.setFill("white")
            triangle.setOutline("white")
            triangle.draw(win)
            x1 = x1 + 42
            x2 = x2 + 42

        x1 = 120
        y1 = y1 + 40
        x2 = 130
        y2 = y2 + 40
    y1 = y1 + 100
    y2 = y2 + 100
    y3 = y3 + 100
    y4 = y4 + 100
