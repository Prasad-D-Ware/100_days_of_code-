# Don't change the code below
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above

#Write your code below this row
# make a variable for keeping the values
highest_score = 0

# use for loop to form the desired condition
for score in student_scores:
  # to check if the score is highest use if function
  if score >highest_score:
    highest_score = score

# print the desired output using F-strings
print(f"The highest score in the class is: {highest_score} ")
