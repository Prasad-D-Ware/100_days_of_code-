# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

#Write your code below this line
# as the formula for bmi we create a variable for it
bmi = round(weight / (height**2), 2)

# now using the if else condictionals we can create our desidered Code
if bmi < 18.5:
  print(f"your bmi is {bmi} , you are underweight.")
    # as we already mentioned the less then 18.5 condition we dont have to mention it again and again and same applies to all the other conditions
    # as we already used if condition we should use elif for making a nested condition
elif bmi< 25:
  print(f"your bmi is {bmi}, you have a normal weight.")
elif bmi<30:
  print (f"your bmi is {bmi}, you are slightly overweight.")
elif bmi <35:
  print(f"your bmi is {bmi}, you are obese.")
else:
  print(f"your bmi is {bmi}, yor are clinically obese")







