# Practical Worksheet 1: Getting started with Python
# Sam Mercer, 814446


def sayHello():
    print("Hello world")


def count():
    for i in range(1, 11):
        print(i)


def kilos2pounds():
    kilos = int(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("The weight in pounds is", pounds)


def kilos_2_pounds_no_input(kilos):
    return 2.2 * kilos


def sayName():
    print("Sam")


def sayHello2():
    print("Hello \nWorld")


def euros2pounds(value):
    return value * 1.09


def addup(x, y):
    return x + y


def changeCounter():
    onepence = int(input("Enter amount of 1p coins:"))
    twopence = int(input("Enter amount of 2p coins:"))
    fivepence = int(input("Enter amount of 5 couns:"))
    print(onepence + (2 * twopence) + (5 * fivepence))


def tenHellos():
    for x in range(0, 10):
        print("hello, world")
    #print("Hello World\n" *10)


def weightsTable():
    print("KG, LBS")
    for x in range(0, 110, 10):
        print(x, "|", kilos_2_pounds_no_input(x))


def futureValue():
    year = int(input("Amount of years to pass:"))
    value = int(input("How much wonga!:"))
    for x in range(0, year):
        value += (value * 0.055)
    print(value)


weightsTable()
