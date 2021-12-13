# import the modules needed
from turtle import Turtle, Screen

# creating the turtle and screen
tim = Turtle()
screen = Screen()

# create the functions for the movement of the turtle
def move_forward():
    tim.fd(20)


def move_backward():
    tim.bk(20)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


# function to clear the screen and return to the centre
def clear():
    tim.clear()
    tim.penup()
    tim.speed("fastest")
    tim.home()
    tim.pendown()


# activating the event listener to hear the keystrokes
screen.listen()

# setting the keys for the specific movements
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
