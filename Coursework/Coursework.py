from graphics import *


def drawFirstPatch(win, startX, startY, colour):
    bottomRight = Point(startX + 100, startY + 100)

    for i in range(10):
        topLeft = Point(startX + (i * 10), startY + (9 - i) * 10)

        rectangle = Rectangle(topLeft, bottomRight)
        rectangle.setFill(colour)
        rectangle.setOutline(colour)
        rectangle.draw(win)


def drawSecondPatch(win, startX, startY, colour):

    xModifier = 0
    yModifier = 0

    for i in range(4):
        for j in range(4):
            posX = i * 30 + startX + xModifier
            posY = j * 30 + startY + yModifier
            rectangleSize(win, posX, posY, startX, colour)

    xModifier = -10
    yModifier = 10

    for i in range(4):
        for j in range(3):
            posX = i * 30 + startX + xModifier
            posY = j * 30 + startY + yModifier
            rectangleSize(win, posX, posY, startX, colour)

    xModifier = 10
    yModifier = 20

    for i in range(3):
        for j in range(3):
            posX = i * 30 + startX + xModifier
            posY = j * 30 + startY + yModifier
            rectangleSize(win, posX, posY, startX, colour)


def rectangleSize(win, posX, posY, startX, colour):
    leftModifier = 0
    rightModifier = 0

    if(posX < startX):
        leftModifier = 10
    if(posX > startX + 80):
        rightModifier = 10

    drawRectangle(win, posX, posY, leftModifier, rightModifier, colour)


def drawRectangle(win, posX, posY, leftModifier, rightModifier, colour):
    topLeft = Point(posX + leftModifier, posY)
    bottomRight = Point(topLeft.getX() + 20 - leftModifier -
                        rightModifier, topLeft.getY() + 10)

    rectangle = Rectangle(topLeft, bottomRight)
    rectangle.setFill(colour)
    rectangle.draw(win)


def main():
    validSizes = ["5", "7", "9", "11"]
    isValidSize = False

    while(not isValidSize):
        size = input("Enter size: ")
        for i in validSizes:
            if(size == i):
                isValidSize = True
        if(not isValidSize):
            print("Invalid input")

    validColours = ["red", "green", "blue",
                    "magenta", "cyan", "orange", "brown", "pink"]
    colourArray = []

    for i in range(3):
        isValidColour = False
        while(not isValidColour):
            colour = input("Enter colour {}: ".format(i + 1))
            for j in validColours:
                if(colour == j):
                    isValidColour = True
            if(isValidColour):
                colourArray.append(colour)
            else:
                print("Invalid input")

    win = GraphWin("Patch", int(size) * 100, int(size) * 100)

    count = 0
    for j in range(int(size)):
        for i in range(int(size)):
            if(i > 0 and i < int(size) - 1):
                if(j != int(size) // 2):
                    drawSecondPatch(win, i * 100, j * 100,
                                    colourArray[count % 3])
                else:
                    drawFirstPatch(win, i * 100, j * 100,
                                   colourArray[count % 3])
            else:
                drawFirstPatch(win, i * 100, j * 100, colourArray[count % 3])
            count = count + 1

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
