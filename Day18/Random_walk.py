# importing the required modules
import turtle as t
import random

# creating the turtle
tim = t.Turtle()
# we use colormode function of the module
t.colormode(255)

# create a function for generating a random color from rgb colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


# list for directions for the turtles
directions = [0, 90, 180, 270]

# increasing the thickness of our turtle
tim.pensize(15)

# increasing the speed
tim.speed("fastest")

# creating a loop for our random walk
for _ in range(200):
    # we can call the function for random color
    tim.color(random_color())
    tim.fd(30)
    tim.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
