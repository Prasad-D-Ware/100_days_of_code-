# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

#Write your code below this line
# as we have to count instead of doing it several times we combine there names
combined_name = name1 + name2

# as the user can enter data in any case for code to work right we convert it into lower case
lowercase_string = combined_name.lower()

# use of variables and using count() function
t =lowercase_string.count("t")
r =lowercase_string.count("r")
u =lowercase_string.count("u")
e =lowercase_string.count("e")

# as the vairables are in int form we can add them
true = t + r + u + e

l =lowercase_string.count("l")
o =lowercase_string.count("o")
v =lowercase_string.count("v")
e =lowercase_string.count("e")

love = l + o + v + e

# for using the string concactanation for our final score we convert it into string first

true_love = int(str(true) + str(love))

# as we need our variable to be used for comparison we need to convert it in int

# use of logical operator "or".
if (true_love <10) or (true_love >90):
  print(f"your score is {true_love},you go together like coke and mentos.")
elif true_love <50 or true_love >40:
  print(f"your score is {true_love}, you are alright together.")

else:
  print(f"your score is {true_love}.")
