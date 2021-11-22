# import the turtle module to use in our code
# import turtle

# # create an object and tap inside the class
# jimmy = turtle.Turtle()
# print(jimmy)

# # we can use this and access the methods/functions
# jimmy.shape("turtle")
# jimmy.color("cyan1")
# jimmy.forward(100)

# # using this we can also access the attributes of the object
# my_screen = turtle.Screen()

# print(my_screen.canvheight)

# # we used this to make the window stay on after the code is completed
# my_screen.exitonclick()


# import and edit packages from the pypi.org
from prettytable import PrettyTable

# making and object
table = PrettyTable()

# add column is an attribute in prettytable
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Evolves into", ["Raichu", "Wartortle", "Charmeleon"])
table.align = "l"


print(table)
