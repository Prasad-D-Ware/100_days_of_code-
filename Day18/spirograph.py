# importing the modules we need 
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

# function for generating random colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# function for performing the task of spirograph
def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.circle(100)
        tim.color(random_color())
        current_heading = tim.heading()
        tim.setheading(current_heading + gap_size)


draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()
