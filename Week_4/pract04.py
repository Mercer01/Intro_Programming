from graphics import *
import random


def personalGreeting():
    var = input("Please enter your name:")
    print("Hello", var, "nice to see you!")


def formalName():
    first_name = input("Please enter your first name:")
    last_name = input("Please enter your surname:")
    print(first_name[:1], ".", last_name)


def kilos2pounds():
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = round(2.2 * kilos, 3)
    print(kilos, "Kilos is equal to", pounds, "pounds")


def generateEmail():
    first_name = input("Please enter your first name:")
    last_name = input("Please enter your surname:")
    entry_year = str(input("Please enter the year you entered:"))
    print("The students email is",
          last_name[:4] + "." + first_name[:1] + "." + entry_year[-2:] + "@myport.ac.uk")


def gradeTest():
    var = int(input("Please enter the score:"))
    gradestring = 'FFFFCCCBBAAA'
    print(gradestring[var])


def graphicLetters():
    word = str(input("Please enter the word you want to output:"))
    win = GraphWin("Letters", 300, 400)
    for letter in word:
        mouse_pos = win.getMouse()
        Letter = Text(mouse_pos, letter).draw(win)
        Letter.setSize(30)

    win.getMouse()


def singASong():
    word = str(input("Please enter the word for the song:"))
    line_count = int(
        input("Please input the amount of lines yo want the song to be:"))
    word_per = int(input("Please enter the amount of words per line:"))
    word = word + " "
    for x in range(line_count):
        print(word * word_per)


def exchangeTable():
    for euros in range(0, 20):
        pounds = euros / 1.09
        print("Euros: {0} Pounds {1:.2f}".format(euros, pounds))


def makeAcronym():
    phrase = str(input("Please enter a phrase:"))
    for word in phrase.split():
        print(word[:1].upper(), end="")


def nameToNumber():
    name = str(input("Please input a name:"))
    value = 0
    for x in name:
        value += ord(x.lower()) - 96
    print(value)


def fileInCaps():
    file = open("d:\Workspace\Intro_Programming\Week_4\text.txt")
    for line in file:
        print(line.upper())
    file.close()


def rainfallChart():
    with open('Week_4\\rainfall.txt') as file:
        for line in file:
            print(line.split()[0], "*" * int(line.split()[1]))


def graphicalRainfallChart():
    file = open('Week_4\\rainfall.txt')
    win = GraphWin("graphicalRainfallChart", 400, 300)
    for x, line in enumerate(file):
        size = int(line.split()[1])
        rect = Rectangle(Point(x * 40 + 40, 280 - size),
                         Point(x * 40, 280)).draw(win)
        text = Text(Point(x * 40 + 20, 290), line.split()[0]).draw(win)
        text.setSize(5)
        rect.setFill(random.choice(
            ["black", "red", "green", "blue", "gold", "yellow"]))
    win.getMouse()
    file.close()


def rainfallInInches():
    newfile = open("Week_4\\rainfall_inches.txt", "w+")
    with open('Week_4\\rainfall.txt') as file:
        for line in file:
            size_inches = int(line.split()[1]) / 25.4
            newfile.write("{0} {1:.2f} \n".format(
                line.split()[0], size_inches))

    newfile.close()


def wc():
    line_count = 0
    word_count = 0
    char_count = 0
    # 'Week_4\\quotation.txt'
    file_path = input("Please input the path to the file:")
    with open(file_path) as file:
        for line in file:
            line_count += 1
            char_count += len(line)
            word_count += len(line.split())

    print("The linecount it {0}, the word count is {1}, and the character count is {2}".format(
        line_count, word_count, char_count))
