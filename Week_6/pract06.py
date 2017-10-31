#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

from graphics import *
import math
import random

# For exercises 8 & 11


def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

# For exercise 8


def distanceBetweenPoints(p1, p2):
    return (math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2))


def drawColouredEye(window, center, radius_eye, colour):
    drawCircle(window, center, radius_eye, "")
    drawCircle(window, center, radius_eye / 2, colour)
    drawCircle(window, center, radius_eye / 4, "black")


def fastFoodOrderPrice():
    cost = float(input("Please enter the price of the pizza:"))
    if cost < 10.00:
        cost += 1.50
    print("The Cost of the pizza is £{0}".format(cost))


def whatToDoToday():
    temp = int(input('Please enter todays temperature: '))
    if temp > 25:
        print('I suggest you go for a swim in the sea')
    elif temp < 25 and temp > 10:
        print('Shopping at Gunwharf would be a good idea')
    elif temp < 10:
        print('Watch a movie at home')
    else:
        print("Invalid temperature, we dont support hot weather")


def displaySquareRoots(a, b):
    for x in range(a, b):
        print("The square root of {0} is {1}".format(x, math.sqrt(x)))


def calculateGrade():
    mark = int(input('Please enter the mark: '))
    if mark >= 16:
        print('A')
    elif mark >= 12:
        print('B')
    elif mark >= 8:
        print('C')
    elif mark < 8:
        print('F')
    else:
        print('Invalid Input')


def peasInAPod():
    peas = int(input('How many peas:'))
    win = GraphWin("Peas in a pod", peas * 100, 100)
    for x in range(peas):
        pea = Circle(Point((x * 100) + 50, 50), 50).draw(win).setFill('green')
    win.getMouse()


def ticketPrice(distance, age):
    if age >= 60 or age <= 15:
        discount = 0.60
    else:
        discount = 1.00
    total_price = discount * (3.00 + (0.15 * distance))
    print("The price is £{0:.2f}".format(total_price))


def numberedSquare(n):
    for y in range(n, 0, -1):
        for x in range(n):
            print(str(y + x) + " ", end='')
        print('')


def eyePicker():
    pos = str(input("Please enter the position of  the eye (x y):")).split()
    size = int(input("Please enter the size of the eye:"))
    colour = str(input("Please enter a valid colour for the eye:"))
    win = GraphWin("eye", 300, 400)
    drawColouredEye(win, Point(int(pos[0]), int(pos[1])), size, colour)
    win.getMouse()


def drawPatchWindow():
    win = GraphWin("Window", 100, 100)
    n = 10
    for y in range(100, 0, -10):
        for x in range(n, 0, -1):
            square = Rectangle(Point(100 - x, y), Point(100 - x * 10, y - 10))
            square.setFill("Red")
            square.setOutline("Red")
            square.draw(win)

        n -= 1
        if n == -1:
            break
    border = Rectangle(Point(0, 0), Point(100, 100)).draw(win)
    win.getMouse()


def drawPatch(win, pos_x, pos_y, colour):
    n = 10
    pos_x += 100
    for y in range(pos_y + 100, pos_y, -10):
        for x in range(n, 0, -1):
            square = Rectangle(Point(pos_x - x, y),
                               Point(pos_x - x * 10, y - 10))
            square.setFill("Red")
            square.setOutline("Red")
            square.draw(win)
        n -= 1
        if n == -1:
            break
    border = Rectangle(Point(pos_x, pos_y), Point(
        pos_x + 100, pos_y + 100)).draw(win)


def drawPatchWork():
    win = GraphWin("Patchwork", 300, 200)
    for x in range(0, 3):
        for y in range(0, 2):
            drawPatch(win, x * 100, y * 100, "Blue")
    win.getMouse()


def eyesAllAround():
    win = GraphWin("Eyes all around", 500, 500)
    colour_int = 0
    colours = ["blue", "grey", "green", "brown"]
    for x in range(0, 30):
        drawColouredEye(win, win.getMouse(), 30, colours[colour_int])
        colour_int += 1
        if colour_int == 4:
            colour_int = 0

    win.getMouse()


def archeryGame():
    score = 0
    win = GraphWin("Window")
    drawCircle(win, Point(100, 100), 60, "blue")
    drawCircle(win, Point(100, 100), 30, "red")
    drawCircle(win, Point(100, 100), 15, "yellow")
    score_text = Text(Point(100, 10), "").draw(win)

    for x in range(5):
        point = win.getMouse()

        drawCircle(win, Point(point.getX() + random.randint(-5, 5),
                              point.getY() + random.randint(-5, 5)), 5, "black")
        distance_score = distanceBetweenPoints(point, Point(100, 100))
        if distance_score <= 60 and distance_score >= 30:
            score += 2
            score_text.setText("You scored 2 points")
        elif distance_score <= 30 and distance_score >= 15:
            score += 5
            score_text.setText("You scored 5 points")
        elif distance_score <= 15:
            score += 10
            score_text.setText("You scored 10 points")
        else:
            score_text.setText("You missed!")
    score_text.setText("Your total score is " + str(score) + " points")
    win.getMouse()


archeryGame()
