#-------------------------------------------------------------------------------
# Practical Worksheet 5: Using functions
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

from graphics import *
import math

# For exercises 1 and 2
pi = math.pi


def areaOfCircle(radius):
    return pi * radius ** 2


def circumferenceOfCircle(radius):
    return 2 * pi * radius


def circleInfo():
    radius = input("What is the radius of the circle:")
    print("The area is {1} and the circumference is {0}".format(
        circumferenceOfCircle(radius), areaOfCircle(radius)))


def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def drawBlockOfStars(width, height):
    for x in range(height):
        print("*" * width)


def drawLetterE():
    drawBlockOfStars(9, 2)
    drawBlockOfStars(2, 2)
    drawBlockOfStars(5, 2)
    drawBlockOfStars(2, 2)
    drawBlockOfStars(9, 2)


def drawBrownEye(window, center, radius_eye):
    drawCircle(window, Point(center, 100), radius_eye, "")
    drawCircle(window, Point(center, 100), radius_eye / 2, "brown")
    drawCircle(window, Point(center, 100), radius_eye / 4, "black")


def drawBrownEyeNoPoint(window, center, radius_eye):
    drawCircle(window, center, radius_eye, "")
    drawCircle(window, center, radius_eye / 2, "brown")
    drawCircle(window, center, radius_eye / 4, "black")


def drawPairOfBrownEyes():
    win = GraphWin()
    drawBrownEye(win, 100, 60)
    drawBrownEye(win, 220, 60)
    win.getMouse()


def distanceBetweenPoints(p1, p2):
    return (math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2))
# print(distanceBetweenPoints(Point(1, 2), Point(4, 6)))


def drawBlockOfStars2(gap_1, star_1, gap_2, star_2, row):
    for x in range(row):
        print(" " * gap_1, end="")
        print("*" * star_1, end="")
        print(" " * gap_2, end="")
        print("*" * star_2)


def drawLetterA():
    drawBlockOfStars2(1, 8, 0, 0, 2)
    drawBlockOfStars2(0, 2, 6, 2, 2)
    drawBlockOfStars2(0, 10, 0, 0, 2)
    drawBlockOfStars2(0, 2, 6, 2, 3)


def drawFourPairsOfBrownEyes():
    win = GraphWin("Brown Eyes", 800, 800)
    for x in range(4):
        left_point = win.getMouse()
        radius = distanceBetweenPoints(left_point, win.getMouse())
        drawBrownEyeNoPoint(win, left_point, radius)
        right_x_coord = left_point.getX() + radius * 2
        drawBrownEyeNoPoint(win, Point(
            right_x_coord, left_point.getY()), radius)
    win.getMouse()


def displayTextWithSpaces(win, text, text_size, position):
    text = text.replace("", " ")
    print(text)
    text_label = Text(position, text).draw(win)
    text_label.setSize(text_size)


# win = GraphWin("")
# displayTextWithSpaces(win, "text", 15, Point(100, 100))

def constructVisionChart():
    win = GraphWin("Vision Chart", 300, 400)
    increment_y = 80
    increment_x = 150
    point_sizes = [30, 25, 20, 15, 10, 5]
    for point_size in point_sizes:
        inputBox = Entry(Point(50, 30), 10).draw(win)
        win.getMouse()
        displayTextWithSpaces(win, inputBox.getText(),
                              point_size, Point(increment_x, increment_y))
        increment_x -= 5
        increment_y += 40
    win.getMouse()


def drawStickFigure(win, size, pos):
    pos_X = pos.getX()
    pos_Y = pos.getY()
    head = Circle(pos, size / 2).draw(win)
    body = Line(Point(pos_X, pos_Y + size / 2),
                Point(pos_X, pos_Y + size)).draw(win)
    arm1 = Line(Point(pos_X, pos_Y + size / 2),
                Point(pos_X - size, pos_Y - size / 2)).draw(win)
    arm2 = Line(Point(pos_X, pos_Y + size / 2),
                Point(pos_X + size / 2, pos_Y - size / 2)).draw(win)
    leg1 = Line(Point(pos_X, pos_Y + size), Point(80, 140)).draw(win)
    leg2 = Line(Point(100, 120), Point(120, 140)).draw(win)

    win.getMouse()


def drawStickFigureFamily():
    win = GraphWin("People",  400, 400)
    drawStickFigure(win, 50, Point(100, 100))


drawStickFigureFamily()
