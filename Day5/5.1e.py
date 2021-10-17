# Don't change the code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above


#Write your code below this row

# make a variable for using for loop
total_height = 0
# use for loop to add all the input values
for height in student_heights:
  add_height = total_height = total_height + height

# create a variable to store number of students
number_of_students = 0

# use for loop to find the number of students
for student in student_heights:
  add_students = number_of_students =number_of_students + 1

# print the final output which is rounded as we needed
print(round(add_height / add_students))



