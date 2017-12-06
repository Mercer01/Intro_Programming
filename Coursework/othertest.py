from graphics import *


def drawTriangle(win, pos_1, pos_2, pos_3, colour):
    triangle = Polygon(Point(pos_1, pos_2, pos_3)
    triangle.draw(win)
    triangle.setFill(colour)


def drawshape(win, pos_x, pos_y, colour, flip):
    if flip:
        drawTriangle(Point(pos_x, pos_y), Point(
            pos_x + 10, pos_y + 10), Point(pos_x, pos_y + 20))
        drawTriangle(Point(pos_x, pos_y + 20), Point(
            pos_x + 10, pos_y + 10), Point(pos_x + 20, pos_y + 20))
    else:
        drawTriangle(Point(pos_x + 20, pos_y + 20), Point(
            pos_x + 10, pos_y + 10), Point(pos_x, pos_y + 20))


def Patch2(win, x, y, colour):
    for i in range(5):
        for j in range(5):
            drawTriangle(win, i * 20, j * 20, colour, True)


win=GraphWin("test", 100, 100)
Patch2(win, 0, 0, "red")

win.getMouse()
