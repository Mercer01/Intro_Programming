from graphics import *
import random
import time
import math


def distanceBetweenFourPoints(x1, x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def get_Inputs():
    border = int(input("Please enter the range for the walk:"))
    count_walks = int(input("How many walks do you want to do:"))
    return border, count_walks


def do_multiple_walks(amount_of_walks, distance_till_death):
    win = GraphWin("A window", 500, 500)
    the_wall = Circle(Point(250, 250), distance_till_death).draw(win)
    for x in range(amount_of_walks):
        do_walk(win, distance_till_death)


def do_walk(win, distance_till_death):
    distance_from_origin = 0
    old_pos_x = 250
    old_pos_y = 250
    calculated_pos_y = 250
    calculated_pos_x = 250

    while distance_from_origin <= distance_till_death:
        distance_from_origin = distanceBetweenFourPoints(
            old_pos_x, old_pos_y, 250, 250)
        num_rand = random.randint(0, 3)
        if num_rand == 0:
            calculated_pos_x += 5
        elif num_rand == 1:
            calculated_pos_y += 5
        elif num_rand == 2:
            calculated_pos_x -= 5
        else:
            calculated_pos_y -= 5
        print(old_pos_x in range(calculated_pos_x - 5, calculated_pos_x + 5),
              old_pos_y in range(calculated_pos_y - 5, calculated_pos_y + 5))
        # time.sleep(0.1)
        walking = Line(Point(old_pos_x, old_pos_x),
                       Point(calculated_pos_x, calculated_pos_y)).draw(win)
        old_pos_x = calculated_pos_x
        old_pos_y = calculated_pos_y


def main():
    border, count_walks = get_Inputs()
    do_multiple_walks(count_walks, border)


if __name__ == '__main__':
    main()
