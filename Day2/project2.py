#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60



# create an welcome note for ur tip calculator

print("Welcome to the tip calculator!")

# as we need the input abt the bill amount and to work in maths we need to convert it into float for decimal places

bill = float(input("what is the total amount of your bill? $"))

# as we tip in a whole number  or a decimal so we can convert it into integer or float as peer need

tip = int(input("What percentage tip would u like to give ? 10, 12,or 15 "))

# as the number of people will be a whole number this must be in integer

people = int(input("how many people to split the bill? "))

# as to calculate the bill with tip we need to add the percentage of the tip

final_bill = tip/100 * bill + bill

# for the bill to be divided in persons we will divide it

bill_per_person = final_bill/people

# as we want our bill to be rounded off to 2 decimal places we'll use round function

total_bill = round(bill_per_person, 2)

# at last we can print the required output using a f-string function

print(f"Each person should pay {total_bill}$")
