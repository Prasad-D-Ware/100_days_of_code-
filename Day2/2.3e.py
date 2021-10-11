# Don't change the code below
age = input("What is your current age?")
# Don't change the code above

#Write your code below this line

# as we have to convert string into interger format

age1 = int(age)

# do some math and figure how to get the desired outputs and for some strings

years_left = 90 - age1

days_left = years_left * 365

months_left = years_left * 12

weeks_left = years_left * 52

# at final print the statement using f-Strings or u can make this a variable and print it later

print(f"You have {days_left} days,{weeks_left} weeks and {months_left} months left." )
