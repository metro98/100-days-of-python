
member = int(input("How many members"))
names = []
for i in range(0, member):
    names_string = input("Enter the names")
    names.append(names_string)
print(names)
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
names_length = len(names)
random_value = random.randint(0,names_length - 1)
print(f"{names[random_value]} is going to buy the meal today!")