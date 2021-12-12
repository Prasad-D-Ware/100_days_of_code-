# used this package for extracting colors from an image
# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# print(rgb_colors)

# import modules we need
import turtle as t
import random

# set the colormode as we need rgb
t.colormode(255)

tim = t.Turtle()
# setting turtles starting qualities
tim.penup()
tim.hideturtle()
tim.speed("fastest")

color_list = [
    (202, 164, 109),
    (238, 240, 245),
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (133, 163, 185),
    (198, 91, 71),
    (46, 122, 86),
    (72, 43, 35),
    (145, 178, 148),
    (13, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (105, 74, 77),
    (55, 46, 50),
    (183, 205, 171),
    (36, 60, 74),
    (18, 86, 90),
    (81, 148, 129),
    (148, 17, 20),
    (14, 70, 64),
    (30, 68, 100),
    (107, 127, 153),
    (174, 94, 97),
    (176, 192, 209),
]

# setting the place to strt for our turtle
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# variable to define total dots to be drawn
number_of_dots = 100

# for loop for the final painting work
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.fd(50)
    tim.pendown

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.left(90)
        tim.fd(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
