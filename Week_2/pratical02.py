import math
pi = math.pi

def circumferenceOfCircle():
    radius = int(input("Please enter the radius of your circle:"))
    print(2*radius*pi)

def areaofCircle():
    radius = int(input("Enter Radius:"))
    print(pi**(radius**2))

def costOfPizza():
    diameter = int(input("Enter the diameter of your circle:"))
    print(((diameter/2)**2)*pi * 1.5)

def slopeOfLine(x1,x2,y1,y2):
    print((y2-y1)/(x2-x1))

def distanceBetweenFourPoints(x1,x2,y1,y2):
    print(math.sqrt((x2-x1)**2 + (y2-y1)**2))

def travelStatistics():
    speed = int(input("Please can you input tje average speed for the journey:"))
    time = int(input("Please enter how long the journey took:"))
    distance = speed * time
    print("Distance " + str(distance) +" Fuel Efff " + str(distance/5) + "Liters were consumed")

def sumOfNumbers():
    count = int(input("Enter number of values:"))
    total = 0
    for x in range(count):
        total = total + (int(input("Enter Number " + str(x +1) + ":")))
    print(total)

def averageOfNumbers():
    count = int(input("Enter number of values:"))
    total = 0
    for x in range(count):
        total = total + (int(input("Enter Number " + str(x+1) + ":")))
    print(total/count)

def selectCoins(total_coins):
    total_coins = int(input("Please input the total amount of code:"))
    for current_coin in [200,100,50,20,10,5,2,1]:
        total_amount = int(total_coins/current_coin)
        print("There are " + str(total_amount) + " of " + str(current_coin) + " coins")
        total_coins -= total_amount*current_coin
