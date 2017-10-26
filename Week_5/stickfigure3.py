from graphics import *

def drawStickfigure():
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(60, 90), Point(140, 90))
    arms.draw(win)
    leg1 = Line(Point(100, 120), Point(70, 170))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(130, 170))
    leg2.draw(win)
