import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code

answer = int(input("What do you want to choose Type 0 for rock , 1 for paper  and 2 for scissors\n"))
comp_answer = random.randint(0,2)
compare_list = []
compare_list.append(answer)
compare_list.append(comp_answer)
new_compare = [rock, paper, scissors]
if answer == 0:
    print(new_compare[0])
if answer == 1:
    print(new_compare[1])
if answer == 2:
    print(new_compare[2])


if comp_answer == 0:
    print(new_compare[0])
if comp_answer == 1:
    print(new_compare[1])
if comp_answer == 2:
    print(new_compare[2])


print(compare_list)
if compare_list[0] == compare_list[1]:
    print("Draw")
elif compare_list[0] == 0 and compare_list[1] == 1:
    print("Computer Wins")
elif compare_list[0] == 1 and compare_list [1] == 2:
    print("Computer Wins")
elif compare_list[1] == 2 and compare_list[0] == 0:
    print("Computer Wins")
else:
    print("You Win")