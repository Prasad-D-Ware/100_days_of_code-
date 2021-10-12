# Don't change the code below
number = int(input("Which number do you want to check? "))
# Don't change the code above

#Write your code below this line

# as we know the all even numbers are divisible by 2 and give remainder 0

# we use modulo as it shows the remainder after dividing and then use if else statement to execute our desired code

if number % 2 == 0:
  print("Its a even number!")

else:
  print("Its an odd number!")


