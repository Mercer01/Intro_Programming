#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

from graphics import *
import time
import math
import random

# For exercise 2


def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def distanceBetweenPoints(p1, p2):
    return (math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2))


def drawColouredEye(window, center, radius_eye, colour):
    drawCircle(window, center, radius_eye, "")
    drawCircle(window, center, radius_eye / 2, colour)
    drawCircle(window, center, radius_eye / 4, "black")


def calculateGrade(mark):  # from 06 cba import
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


def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        green.setFill('Black')
        red.setFill('Red')
        time.sleep(1)
        amber.setFill('yellow')
        red.setFill('Black')
        time.sleep(1)
        amber.setFill('Black')
        green.setFill('green')
        time.sleep(1)
    # remove the pass and add your code here


# For exercise 6


def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32


def askName():
    while True:
        name = str(input("Please enter your name: "))
        if name.isalpha():
            break
        print("Your name invalid try again")


def calculateCoursework():
    while True:
        value = int(input('Please enter the mark:'))
        if value.isnumeric() and value >= 0 and value <= 20:
            calculateGrade(value)
            break
        print('Invalid Input')


def orderPrice():
    total = 0
    while True:
        price = str(input("Please enter the value of the item "))
        if price.isnumeric():
            price = float(price)
            count = input("Please enter the amount: ")
            if count.isnumeric():
                count = int(count)
                total += (price * count)
                more = input("Are there any more (Y,N)?: ")
                if more == 'N':
                    break

    print("The total price is", total)


def clickableEye():
    win = GraphWin("clicable Eye", 400, 400)
    drawColouredEye(win, Point(200, 200), 100, "Brown")

    message = Text(Point(200, 350), "").draw(win)
    while True:
        p = win.getMouse()
        distance = distanceBetweenPoints(p, Point(200, 200))

        if distance <= 25:
            message.setText("pupil")
        elif distance <= 50:
            message.setText("iris")
        elif distance <= 100:
            message.setText("sclera")
        else:
            break


def temperatureConverter():
    while True:
        c_or_f = input("Please enter starting unit of the temperature (C/F): ")
        if c_or_f is not "":
            entry = input("Please enter the temperature (" + str(c_or_f) +
                          "):")
            if c_or_f.lower() in ("c", "f"):
                entry = float(entry)
                if c_or_f.lower() == "c":
                    print(celsius2Fahrenheit(entry))
                elif c_or_f.lower() == 'f':
                    print(fahrenheit2Celsius(entry))
            else:
                print("Invalid input try again")
        else:
            break


def guessTheNumber():
    rand_numb = random.randint(0, 100)
    succsess = False
    for x in range(0, 7):
        guess = int(input("Please enter the value you want to guess: "))
        if guess == rand_numb:
            print("Well done it took you {0} tries to guess the right number".
                  format(x + 1))
            succsess = True
            break
        elif guess > rand_numb:
            print("Too High!")
        elif guess < rand_numb:
            print("Too Low!")
    if not (succsess):
        print("You were unable to guess the number")


def tableTennisScorer():
    win = GraphWin("Table Tennis")
    player_text_a = Text(Point(50, 100), "0")
    player_text_a.draw(win).setSize(15)
    player_text_b = Text(Point(150, 100), "0")
    player_text_b.draw(win).setSize(15)
    win_text_a = Text(Point(50, 125), "")
    win_text_b = Text(Point(150, 125), "")
    win_text_a.draw(win)
    win_text_a.setSize(15)
    win_text_b.draw(win)
    win_text_b.setSize(15)

    border = Rectangle(Point(0, 0), Point(100, 200)).draw(win)
    border_2 = Rectangle(Point(0, 0), Point(200, 200)).draw(win)
    player_1_score = 0
    player_2_score = 0
    while True:

        point = win.getMouse()
        if point.getX() > 100:
            player_2_score += 1
        else:
            player_1_score += 1
        print(player_1_score, player_2_score)
        player_text_a.setText(player_1_score)
        player_text_b.setText(player_2_score)

        if player_1_score >= 11 and player_1_score >= player_2_score + 2:
            print("Player 1 wins")
            win_text_a.setText("Wins")
            break
        if player_2_score >= 11 and player_2_score >= player_1_score + 2:
            print("Player 2 wins")
            win_text_b.setText("Wins")
            break
    win.getMouse()


def clickableBoxOfEyes(row, column):
    win = GraphWin("Eyes", 100 * column + 100, 100 * row + 100)
    border_int = Rectangle(
        Point(50, 50), Point(100 * column + 50, 100 * row + 50)).draw(win)
    border_ext = Rectangle(
        Point(0, 0), Point(100 * column + 100, 100 * row + 100)).draw(win)
    for x in range(0, column):
        for y in range(0, row):
            drawColouredEye(win,
                            Point(100 + (x * 100), 100 + (y * 100)), 50,
                            "Brown")
    message = Text(Point(column / 2 * 100 + 50, row * 100 + 70),
                   "test123").draw(win)
    while True:
        point = win.getMouse()
        eye_x = (point.getX() - 50) / 100
        eye_y = (point.getY() - 50) / 100
        print(eye_x, eye_y)
        message.setText("Eye X " + str(int(eye_x) + 1) + "Eye Y " +
                        str(int(eye_y) + 1))
        print(point)
    win.getMouse()


clickableBoxOfEyes(2, 4)
