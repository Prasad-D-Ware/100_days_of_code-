# CHALLANGE 3 SHORT VERSION :

from turtle import Turtle, Screen, shape
import random

my_turtle = Turtle()

colors = [
    "medium sea green",
    "medium blue",
    "dark red",
    "pale violet red",
    "indigo",
    "deep pink",
    "dark slate blue",
]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        my_turtle.fd(100)
        my_turtle.right(angle)


for shape_sides in range(3, 11):
    my_turtle.color(random.choice(colors))
    draw_shape(shape_sides)


screen = Screen()
screen.exitonclick()
