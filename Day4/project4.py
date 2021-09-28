rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# impot random module for computer chosing the number
import random

# needs an input from the user for there choice and covert it into integer
choice = int(input("What do you want to choose? Type 0 for rock, 1 for Paper, 2 for Scissors. \n "))

# use of if to print choices of user
if choice == 0:
  print(rock + "you chose rock")
elif choice ==1:
  print(paper  + "you chose paper")
else:
  print(scissors  + "you chose scissors")

# use of the random module for computers choice
computer = random.randint(0,2)

# use of if to print computers choices
if computer == 0:
  print(rock + "computer chose rock")
elif computer == 1:
  print(paper + "computer chose paper")
else:
  print(scissors + "computer chose scissors")


# the main logic behind the winning and losing situations
if choice == 0 and computer == 2:
  print("You win!")
elif choice>= 3 or choice <0 :
  print("you entered an invalid choice, You lose.")
elif computer > choice:
  print("You lose")
elif computer == choice:
  print("you had a draw!")
elif choice > computer:
  print("You win!")













