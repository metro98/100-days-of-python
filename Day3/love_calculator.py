print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇



full_name = name1.upper() + name2.upper()
full_name_list = []
for i in full_name:
  full_name_list.append(i)
first_calc = ["T","R","U","E"]
second_calc = ["L","O","V","E"]
count = 0
true_occurence = []
love_occurence = []

for i in first_calc:
  for j in full_name_list:
    if i == j:
      count += 1
  true_occurence.append(count)
  count = 0


for x in second_calc:
  for y in full_name_list:
    if x == y:
      count += 1
  love_occurence.append(count)
  count = 0


sum_true = 0
for a in true_occurence:
  sum_true += a

    
sum_love = 0
for b in love_occurence:
  sum_love += b


total_score = str(sum_true) + str(sum_love)
total_score_int = int(total_score)

if total_score_int < 10 or total_score_int > 90:
  print(f"Your score is {total_score_int}, you go together like coke and mentos.")
elif 40 <= total_score_int <= 50:
  print(f"Your score is {total_score_int}, you are alright together.")
else:
  print(f"Your score is {total_score_int}.")
  
