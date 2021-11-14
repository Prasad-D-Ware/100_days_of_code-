# import the modules required
import random
from art import logo

# Global variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.


def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining.  """
  if guess < answer:
    print("Too low.")
    return turns - 1
  elif guess > answer:
    print("Too high")
    return turns - 1
  else:
    print(f"You got it right. The answer is {answer}.")

# Make function to set difficulty.


def set_difficulty():
  difficulty = input("Choose a dificulty, type 'easy' or 'hard' : ")
  if difficulty == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print(logo)

  print("Welcome to the number guessing game! ")

  print("I am thinking of a number between 1-100")

  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

  # Choosing a random number between 1 and 100.
  answer = random.choice(numbers)

  turns = set_difficulty()
  # Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} turns to guess the number. ")

    # Let the user guess a number.
    guess = int(input("Make your guess : "))

    # Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You have run out of guesses, You lose.")
      return


game()
