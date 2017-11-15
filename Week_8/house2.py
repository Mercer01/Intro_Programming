#-------------------------------------------------------------------------------
# house.py - a simple program to draw a house
#-------------------------------------------------------------------------------

from graphics import *


def main():
    doorColour, lightsOn, house_number, window_size = getInputs()
    drawHouse(doorColour, lightsOn, house_number, window_size)


def getInputs():
    window_size = int(
        input("Please enter the size of the window (single value):"))
    doorColour = input("Enter door colour: ")
    lightsYN = input("Are the lights on (y/n): ")
    lightsOn = lightsYN[0] == "y"
    housenumber = int(input("Please enter the house number: "))
    return doorColour, lightsOn, housenumber, window_size


def drawHouse(doorColour, lightsOn, house_number, window_size):
    win = GraphWin("House", window_size, window_size)
    win.setCoords(200, 200, 0, 0)

    roof = Polygon(Point(2, 60), Point(42, 2),
                   Point(158, 2), Point(198, 60))
    roof.setFill("pink")
    roof.draw(win)
    # draw wall and door
    drawRectangle(win, Point(2, 60), Point(198, 198), "brown")
    drawRectangle(win, Point(30, 110), Point(80, 198), doorColour)
    # house_number
    message = Text(Point(55, 154), house_number).draw(win)
    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point(110, 110), Point(170, 170), windowColour)
    win.getMouse()


def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)


main()
