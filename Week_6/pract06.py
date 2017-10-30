#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

from graphics import *
import math

# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

# For exercise 8 
def drawColouredEye(win, centre, radius, colour):
    pass
    # remove the pass and add your code here

def fastFoodOrderPrice():
    cost = float(input("Please enter the price of the pizza:"))
    if  cost < 10.00:
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
    
def displaySquareRoots(a,b):
    for x in range(a,b):
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
    
    win = GraphWin("Peas in a pod",peas*100,100)
    for x in range(peas):
        pea = Circle(Point((x*100)+50,50),50).draw(win).setFill('green')
