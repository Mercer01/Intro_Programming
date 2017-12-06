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
    for y in range(pos_y, pos_y + 100, 20):
        swap = True
        for x in range(pos_x, pos_x + 100, 20):
            if swap:
                if int(y / 20) % 2 == 0:
                    draw_pacman(win, y + 1, x, colour, True)
                else:
                    draw_square(win, y - 1, x, colour)
                swap = False
            else:
                if int(y / 20) % 2 == 0:
                    draw_square(win, y - 1, x, colour)
                else:  # added +2 to make it look nicer
                    draw_pacman(win, y - 2, x, colour, False)
                swap = True


def draw_patterns(win, count, colourslist):
    col_index = 0
    for y in range(0, count):
        for x in range(0, count):
            if x % 2 == 0:
                penultimate(win, y * 100, x * 100, colourslist[col_index])
            else:
                final_patchwork(win, x * 100, y * 100, colourslist[col_index])
            col_index += 1
            if col_index == 3:
                col_index = 0


def getInputs():
    colours_array = []
    size_col = 0  # setup for colours inputs
    valid_colours = ["red", "green", "blue",
                     "magenta", "cyan", "orange", "brown", "pink"]
    while True:  # Loops until done
        size = input("Please enter the size of the patchwork:")
        # checks if input is a number
        if size.isnumeric():
            if int(size) % 2 == 1:
                if size in ["5", "7", "9", "11"]:
                    size = int(size)
                    break
                else:
                    print("Your Input is not one of the valid options 5, 7, 9, 11")
            else:
                print("Your Input is an even number this is invalid")
        else:
            print("Your Input is not a  number")

    while True:
        colour = input("Please enter the {0} colour: ".format(size_col + 1))
        if hasNumbers(colour):  # checks fir digit in input
            print("Your colour contains number. Invalid Input")
        else:
            if colour in valid_colours:
                if colour not in colours_array:  # checks if colour is already added
                    colours_array.append(colour)
                else:
                    print("You cannot enter the same colour more than once")
            else:
                print("Your colour is not avaliable please try a different one. The valid colours are {0}".format(
                    valid_colours))
        # does size of the colours array for breaking purposes
        size_col = len(colours_array)
        if size_col >= 3:  # checks if enough colours have been entered
            break

    return size,


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
