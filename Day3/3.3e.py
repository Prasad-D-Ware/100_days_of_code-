# Don't change the code below
year = int(input("Which year do you want to check? "))
# Don't change the code above

#Write your code below this line

# as the logic behind the leap years is like:
# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

# as per finding the logic behind the leap years we can write this code and for refrence use this flowchart for better understanding :https://bit.ly/36BjS2D

if year % 4 ==0:
  if year % 100 ==0:
    if year % 4 ==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
