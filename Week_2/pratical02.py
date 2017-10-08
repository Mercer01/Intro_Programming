import math
pi = math.pi

def circumferenceOfCircle():
    var = int(input("enter:"))
    return 2*var*pi

def areaofCircle():
    var = int(input("Enter Radius:"))
    return pi**(var**2)

def costOfPizza():
    var = int(input("Enter Diameter:"))
    return ((var/2)**2)*pi * 1.5

def slopeOfLine(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)

def distanceBetweenPoints(x1,x2,y1,y2):
    return ((x2-x1)**2 + (y2-y1)**2) // 2

def travelStatistics(speed, time):
    distance = speed * time
    return "Distance " + str(distance) +" Fuel Efff " + str(distance/5) + "Liters were consumed"

def sumOfNumbers():
    count = int(input("Enter number of values:"))
    total = 0
    for x in range(count):
        total = total + (int(input("Enter Number " + str(x +1) + ":")))
    return total

def averageOfNumbers():
    count = int(input("Enter number of values:"))
    total = 0
    for x in range(count):
        total = total + (int(input("Enter Number " + str(x+1) + ":")))
    print(total/count)

def selectCoins(total_coins):
    for current_coin in [200,100,50,20,10,5,2,1]:
        total_amount = int(total_coins/current_coin)
        print("There are " + str(total_amount) + " of " + str(current_coin) + " coins")
        total_coins -= total_amount*current_coin
    
selectCoins(8023) 