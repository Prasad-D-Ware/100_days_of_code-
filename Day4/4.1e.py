#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

test_seed = int(input("create seed number: "))
random.seed(test_seed)
# we use the random module to generate a the desired number
head_tail = random.randint(0, 1)

# then we asign them the values using if function we can get our outputs
if head_tail ==0:
  print("Tails")
else:
  print("Heads")









