#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
new_letters = []
for letter in range(0, nr_letters):
    new_letters.append(letters[random.randint(0,51)])
# print(new_letters)

new_symbols = []
for letter in range(0, nr_symbols):
    new_symbols.append(symbols[random.randint(0,8)])
# print(new_symbols)

new_numbers = []
for letter in range(0, nr_numbers):
    new_numbers.append(numbers[random.randint(0,9)])
# print(new_numbers)

password_list =  new_letters + new_symbols + new_numbers
# print(password_list)
password = "".join(password_list)
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
new_hard_password_list = []
for i in range(0, len(password_list)):
    new_hard_password_list.append(password_list[random.randint(0, len(password_list) - 1)])
# print(new_hard_password_list)

hard_password = "".join(new_hard_password_list)
print(hard_password)