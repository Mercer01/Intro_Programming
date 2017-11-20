from graphics import *
import math


def final_patchwork(win, pos_x, pos_y, colour):
    n = 10
    pos_x += 100
    for y in range(pos_y + 100, pos_y, -10):
        for x in range(n, 0, -1):
            square = Rectangle(Point(pos_x - x, y),
                               Point(pos_x - x * 10, y - 10))
            square.setFill(colour)
            square.setOutline(colour)
            square.draw(win)
        n -= 1
        if n == -1:
            break


def draw_square(win, x, y, colour):
    rect = Rectangle(Point(x, y), Point(x + 20, y + 20))
    rect.setFill(colour)
    rect.setOutline(colour)
    rect.draw(win)


def draw_pacman(win, x, y, colour, flip):
    pac = Circle(Point(x + 10, y + 10), 10)
    pac.setFill(colour)
    pac.setOutline(colour)
    pac.draw(win)
    if flip:
        polygon = Polygon(Point(x + 20, y),
                          Point(x + 10, y + 10), Point(x + 20, y + 20))
    else:
        polygon = Polygon(Point(x, y), Point(x + 10, y + 10), Point(x, y + 20))

    polygon.setOutline("white")
    polygon.setFill("White")
    polygon.draw(win)


def penultimate(win, pos_x, pos_y, colour):
    for y in range(pos_x, pos_x + 100, 20):
        for x in range(pos_y, pos_y + 100, 20):
            if int((x / 20)) % 2 == 0:
                if int((y / 20)) % 2 == 0:
                    draw_pacman(win, y, x, colour, True)
                else:
                    draw_square(win, y, x, colour)
            else:
                if int((y / 20)) % 2 == 0:
                    draw_square(win, y, x, colour)
                else:
                    draw_pacman(win, y, x, colour, False)


def draw_patterns(win, count, colourslist):
    colour_index = 0
    for y in range(0, count):
        for x in range(0, count):
            if x % 2 == 0:
                penultimate(win, x * 100, y * 100, colourslist[colour_index])
            else:
                final_patchwork(win, x * 100, y * 100,
                                colourslist[colour_index])
            colour_index += 1
            if colour_index == 3:
                colour_index = 0


def getInputs():
    colours_array = []
    size_col = 0  # setup for colours inputs

    while True:  # Loops until done
        size = input("Please enter the size of the patchwork:")
        if size.isnumeric():  # checks if input is a number
            size = int(size)  # converts value to integer before returning
            break
        print("Invalid input")

    while True:
        colour = input("Please enter the {0} colour: ".format(size_col + 1))
        if hasNumbers(colour):  # checks fir digit in input
            print("Your colour contains number. Invalid Input")
        else:
            if colour not in colours_array:  # checks if colour is already added
                colours_array.append(colour)
            else:
                print("You cannot enter the same colour more than once")
        # does size of the colours array for breaking purposes
        size_col = len(colours_array)
        if size_col >= 3:  # checks if enough colours have been entered
            break

    return size, colours_array


def hasNumbers(inputString):
    # Loops through entire string checking for digit inside input
    return any(char.isdigit() for char in inputString)


def main():
    size, colours = getInputs()
    win = GraphWin("Coursework 814446", size * 100, size * 100)
    draw_patterns(win, size, colours)
    win.getMouse()


if __name__ == '__main__':
    main()
