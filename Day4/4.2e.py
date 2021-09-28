import random
test_seed = int(input("create seed number: "))
random.seed(test_seed)


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above

#Write your code below this line

# as we need to get total no of items in the list
num_items = len(names)

# using the random no generator we can make it pick a number
random_choice = random.randint(0, num_items -1)

# as we need a specific name out of the list
person = names[random_choice]

# print our output as we need
print( person + " is gonna pay for the meal today!")






