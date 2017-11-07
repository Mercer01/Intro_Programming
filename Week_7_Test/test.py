from graphics import *


def drawCircle(win, centre, radius, colour,colour2):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.setOutline(colour2)
    circle.draw(win)

def circles():
    win = GraphWin("Circles",400,400)
    
    for x in range(0,20):
        point = win.getMouse()
        filled = ""
        outline = ""
        y_point = point.getY()
        if y_point <= 100:
            filled = 'Blue'
            outline = 'Blue'
        elif y_point <= 200:
            outline = 'Blue'
        elif y_point <= 300:
            outline = 'Pink'
            filled = 'Pink'
        elif y_point <= 400:
            outline = 'Pink'
        
        drawCircle(win,point,20,filled,outline)
        

def circles2():
    win = GraphWin("Circles2", 400,400)

    for x in range(0,10):
        for y in range(0,3):
            point = win.getMouse()
            filled = ""
            outline = ""
            y_point = point.getY()
            if y_point <= 100:
                filled = 'Blue'
                outline = 'Blue'
            elif y_point <= 200:
                outline = 'Blue'
            elif y_point <= 300:
                outline = 'Pink'
                filled = 'Pink'
            elif y_point <= 400:
                outline = 'Pink'

            drawCircle(win,Point(420 - (3-y) * 40, 20 + (x * 40)),20,filled,outline)


circles()
