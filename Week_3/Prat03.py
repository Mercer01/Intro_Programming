# Practical Worksheet 3: Graphical Programming
# your name, your number

from graphics import *
import random


def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arm1 = Line(Point(80, 80), Point(100, 90)).draw(win)
    arm2 = Line(Point(120, 80), Point(100, 90)).draw(win)
    leg1 = Line(Point(100, 120), Point(80, 140)).draw(win)
    leg2 = Line(Point(100, 120), Point(120, 140)).draw(win)

    win.getMouse()


def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100, 100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")


def drawCircle():
    radius = int(input("Enter Radius of circle: "))
    win = GraphWin("drawCircle")
    Circle(Point(100, 60), radius).draw(win)

    win.getMouse()


def drawArcheryTarget():
    win = GraphWin("drawArcheryTarget")
    circle1 = Circle(Point(100, 100), 90).draw(win)
    circle1.setFill("red")
    circle2 = Circle(Point(100, 100), 60).draw(win)
    circle2.setFill("green")
    circle3 = Circle(Point(100, 100), 30).draw(win)
    circle3.setFill("blue")
    win.getMouse()


def drawRectangle():
    win = GraphWin("drawRectangle", 200, 200)
    height = int(input("Please input Height:"))
    width = int(input("Please Input Width: "))
    rect = Rectangle(Point(100 - height / 2, 100 - width / 2),
                     Point(100 + height / 2, 100 + width / 2)).draw(win)
    rect.setFill("black")
    win.getMouse()


def blueCircle():
    win = GraphWin("blueCircle")
    p = win.getMouse()
    circle = Circle(Point(p.getX(), p.getY()), 50).draw(win)
    circle.setFill("blue")

    win.getMouse()


def tenLines():
    for x in range(10):
        drawLine()


def tenStrings():
    win = GraphWin("tenStrings", 400, 300)
    for x in range(10):
        inputBox = Entry(Point(50, 30), 10)
        inputBox.draw(win)
        p = win.getMouse()
        message = Text(Point(p.getX(), p.getY()), inputBox.getText()).draw(win)


def tenColouredRectangles():
    win = GraphWin("tenColouredRectangles", 400, 300)
    for x in range(10):
        inputBox = Entry(Point(50, 30), 10)
        inputBox.draw(win)
        pos1 = win.getMouse()
        pos2 = win.getMouse()
        rect = Rectangle(Point(pos1.getX(), pos1.getY()),
                         Point(pos2.getX(), pos2.getY())).draw(win)
        rect.setFill(inputBox.getText())


def fiveClickStickFigure():
    win = GraphWin("fiveClickStickFigure", 300, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = (((p2.getX() - p1.getX())**2) + (p2.getY() - p2.getY())**2)**0.5
    #radius = (((p2.getX() * p1.getX())) + (p2.getY() * p2.getY()))
    head = Circle(p1, radius).draw(win)
    p3 = win.getMouse()
    body = Line(Point(p1.getX(), p1.getY() + radius), p3).draw(win)
    p4 = win.getMouse()
    distance2 = p4.getX() - p3.getX()
    arms = Line(Point(p4.getX(), p4.getY()), Point(
        p4.getX() - (distance2 * 2), p4.getY())).draw(win)
    p5 = win.getMouse()
    leg1 = Line(p5, p3).draw(win)
    distance3 = p5.getX() - p3.getX()
    leg2 = Line(Point(p5.getX() - distance3 * 2, p5.getY()), p3).draw(win)

    win.getMouse()


def plotRainfall():
    win = GraphWin("tenStrings", 400, 300)
    inputBox = Entry(Point(50, 30), 10)
    inputBox.draw(win)
    for x in range(7):
        win.getMouse()
        size = int(inputBox.getText())
        rect = Rectangle(Point(x * 20 + 20, 300 - size),
                         Point(x * 20, 300)).draw(win)
        rect.setFill(random.choice(
            ["black", "red", "green", "blue", "gold", "yellow"]))
    win.getMouse()
