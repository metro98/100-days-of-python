age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
max_age = 90
alive = max_age - int(age)
alive_in_weeks = alive * 52
print(f"You have {alive_in_weeks} weeks left.")