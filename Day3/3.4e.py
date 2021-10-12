#  Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#  Don't change the code above

#Write your code below this line

# as we dont have a variable for storing bill amount create one
bill =0
# then we use if conditional for size as the main prize is dependent on it
if size == "S":
  bill=15
  # use of second if command as we need to run both the conditions
  if add_pepperoni =="Y":
    bill+=2
 # use of elif to check more then one condition
elif size == "M":
  bill=20
  if add_pepperoni =="Y":
    bill+=3
else:
  bill=25
  if add_pepperoni =="Y":
    bill+=3
    # use of the third condition using if command
if extra_cheese =="Y":
  bill+=1

# at last print the total bill of the customer
print(f"Your total bill is ${bill}")




