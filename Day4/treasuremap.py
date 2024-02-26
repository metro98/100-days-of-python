line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
value = []
for i in position:
  value.append(i)

for j in value:
  if j == "A":
    value[0] = 1
  if j == "B":
    value[0] = 2
  if j == "C":
    value[0] = 3

new_value = [value[0],int(value[1])]


map[new_value[1] - 1] [new_value[0] - 1] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")