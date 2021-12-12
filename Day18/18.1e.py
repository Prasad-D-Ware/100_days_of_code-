from turtle import Turtle, Screen


my_turtle = Turtle()

# my_turtle.color("blue", "red")
# my_turtle.shape("turtle")

# CHALLENGE 1:create a square shape 
# for _ in range(4):
#     my_turtle.fd(100)
#     my_turtle.right(90)

# CHALLENGE 2: create a dashed line
# for _ in range(15): 
#     my_turtle.pendown()
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)

# CHALLENGE 3:create shapes in order triangle,square,pentagon, hexagon, heptagon, octagon, nonagon, decagon
def triangle(): 
    for _ in range(3):
        my_turtle.pencolor("red")
        my_turtle.forward(100)
        my_turtle.right(120)

def square():
    for _ in range(4):
        my_turtle.fd(100)
        my_turtle.right(90)
        my_turtle.pencolor("blue")
  
def pentagon():    
    for _ in range(5):
        my_turtle.forward(100)
        my_turtle.right(72)
        my_turtle.pencolor("green")
        
def hexagon():
    for _ in range(6):
        my_turtle.forward(100)
        my_turtle.right(60)
        my_turtle.pencolor("purple")
    
def heptagon():
    for _ in range(7):
        my_turtle.forward(100)
        my_turtle.right(51.42)
        my_turtle.pencolor("cyan")

def octagon():
    for _ in range(8):
        my_turtle.forward(100)
        my_turtle.right(45)
        my_turtle.pencolor("yellow")

def nonagon():
    for _ in range(9):
        my_turtle.forward(100)
        my_turtle.right(40)
        my_turtle.pencolor("coral")
        
def decagon():
    for _ in range(10):
        my_turtle.forward(100)
        my_turtle.right(36)
        my_turtle.pencolor("orange")

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

screen = Screen()
screen.exitonclick()
