from graphics import *


def draw_square(win, x, y, colour):
    rect = Rectangle(Point(x, y), Point(x + 20, y + 20))
    rect.setFill(colour)
    rect.setOutline(colour)
    rect.draw(win)


def draw_pacman(win, x, y, colour, flip):
    pac = Circle(Point(x + 10, y + 10), 10)
    pac.setFill(colour)
    pac.setOutline(colour)
    pac.draw(win)
    if flip:
        polygon = Polygon(Point(x + 20, y),
                          Point(x + 10, y + 10), Point(x + 20, y + 20))
    else:
        polygon = Polygon(Point(x, y), Point(x + 10, y + 10), Point(x, y + 20))

    polygon.setOutline("white")
    polygon.setFill("White")
    polygon.draw(win)


def penultimate(win, pos_x, pos_y, colour):
    for y in range(pos_y, pos_y + 100, 20):
        swap = True
        for x in range(pos_x, pos_x + 100, 20):

            if swap:
                if int(y / 20) % 2 == 0:
                    draw_pacman(win, y + 1, x, colour, True)
                else:
                    draw_square(win, y - 1, x, colour)
                swap = False
            else:
                if int(y / 20) % 2 == 0:
                    draw_square(win, y - 1, x, colour)
                else:  # added +2 to make it look nicer
                    draw_pacman(win, y - 2, x, colour, False)
                swap = True


win = GraphWin("win", 500, 500)
penultimate(win, 0, 0, "red")
print("2nd one")
penultimate(win, 100, 0, "blue")
print("3rd One")
penultimate(win, 200, 0, "green")


win.getMouse()
