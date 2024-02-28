# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
count = 0
sum = 0
for height in student_heights:
  count += 1
  sum += height
print(f"total_height = {sum}")
print(f"number of students = {count}")
average_height = round(sum/count)
print(f"average height = {average_height}")