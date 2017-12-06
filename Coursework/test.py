__auther__ = "Will"
__project__ = "Patterns Course Word"

import graphics as g


def draw_patch(window, pos_x, pos_y, colour):
    x = pos_x
    y = pos_y
    print(x, y)

    while x < pos_x + 100 and y != pos_y - 100:
        print(x, y, pos_y - 100, x <= 100)
        draw_line(window, y, x, (2 * y) + 100 - x, pos_x + 100, colour)
        # draw_line(window, y, pos_x, pos_y + 100, (2 * pos_x) + 100 - x, colour)
        # draw_line(window, y, pos_x, pos_y, x, colour)
        # draw_line(window, pos_y + 100, x, y, pos_x + 100, colour)

        if x <= 100:
            y -= 20
        else:
            x += 20


def draw_line(window, x1, y1, x2, y2, colour):
    line = g.Line(g.Point(x1, y1), g.Point(x2, y2))
    line.draw(window)
    line.setFill(colour)


def main():
    window = g.GraphWin("Patch Work")

    draw_patch(window, 50, 50, "Red")
    window.getMouse()


if __name__ == '__main__':
    main()
