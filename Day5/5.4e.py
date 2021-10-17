#Write your code below this row

# create a for loop with range
for number in range(1, 101):
  # use if for first logic
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # use elif for divisiblity by 3
  elif number % 3 == 0 :
    print("Fizz")
  # divisibility by 5
  elif number % 5 == 0 :
    print("Buzz")
  # print rest of the numbers as they r not part of the if conditions
  else:
    print(number)



