target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
for i in range(0,target+1):
  if i % 2 == 0:
    total += i

print(total)
  