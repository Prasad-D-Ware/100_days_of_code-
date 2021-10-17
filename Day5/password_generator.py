#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# use choice function of random module for every step
for char in range(1, nr_letters +1):
  password += random.choice(letters)

# add the input into the password variable so tht it shows the final password in the end
for sym in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for num in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# create a list of the users input
password_list = []

# use append function to add the new letters into the list
for char in range(1, nr_letters +1):
  password_list.append(random.choice(letters))

# used append to add symbols
for sym in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

# used append to add numbers to the list
for num in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

# use random modules shuffle function to shuffle the password characters
random.shuffle(password_list)

# created the variable to store our final string to show our output
password =""
for char in password_list:
  password += char

# print output as needed!
print(f"Your password is {password}")
