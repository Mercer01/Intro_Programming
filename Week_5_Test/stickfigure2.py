from graphics import *


def footballPlayer():
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    arm1 = Line(Point(200, 90), Point(160, 100))
    arm1.draw(win)
    arm2 = Line(Point(200, 90), Point(240, 100))
    arm2.draw(win)
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)

    # setup ground line object
    base_line = Line(Point(0, 170), Point(300, 170)).draw(win)
    # setup goalpost object
    goal_post = Rectangle(Point(60, 170), Point(50, 20)).draw(win)
    goal_post.setFill("black")  # make black
    # setup ball object
    ball = Circle(Point(160, 160), 10).draw(win)
    ball.setFill("blue")  # make object blue

    goal_string = "Goal!"  # setup of string to iterate through
    message = Text(Point(100, 50), "").draw(
        win)  # sets up placeholder location
    for x in range(5):  # loop through 5 times
        win.getMouse()  # get mouse click
        ball.move(-25, 0)  # move by 25 to the left
        message.setText(goal_string[:x + 1])  # update the text on the string


footballPlayer()
