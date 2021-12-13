# import the required modules
from turtle import Turtle, Screen, turtles
import random

# set a variable for the while loop
is_race_on = False

# creating a screen for our turtle race
screen = Screen()

screen.setup(width=500, height=400)

# using textinput method creating the prompt for users guess
user_bet = screen.textinput(
    title="Make Your Bet", prompt="Which turtle will win the race? Enter a color : "
)

# lists for the data to be stored and used
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = [100, 60, 20, -20, -60, -100]
all_turtles = []

# for loop for creating new turtle object
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cord[turtle_index])
    all_turtles.append(new_turtle)

# setting the while loop switch on
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # switching off the variable for stoping the while loop after one turtle wins
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You have won! The {winning_turtle} turtle is the winner! ")
            else:
                print(f"You have lose! The {winning_turtle} turtle is the winner! ")

        # creating random numbers for random distance to be travelled by the turtle
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# using method so tht the screen wont go off after finishing the race
screen.exitonclick()
