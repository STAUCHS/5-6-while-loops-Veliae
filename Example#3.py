# Example 3 - Calculating Average

num_of_students = int(input("Enter the number of students: "))

sum = 0
count = num_of_students
# Ask user for marks and sum all marks
while num_of_students > 0:
  mark = float(input(f"Enter mark {count - 1}: remaining"))
  sum += mark
  count -=1

average = sum/num_of_students

print(f"Your class average is {average}")