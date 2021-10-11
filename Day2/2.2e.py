#  Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#  Don't change the code above

# Write your code below this line

#convert string data type into interger data type
weight1 = int(weight)
height1 = float(height)

# as we only need the interger part of our result and not the decimals it should be in interger
# data type so we convert it using function in function method

result = print(int((weight1)/(height1*height1)))
