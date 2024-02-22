print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
total_bill = 0
bill = [5,7,12]
if height >= 120:
    print("You can take a rollercoaster ride")
    age = int(input("What is your age? "))
    if age < 12:
        total_bill = bill[0]
    elif age <= 18:
        total_bill = bill[1]
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        total_bill = bill[2]
    wants_photo = input("Do you want a photo?(Y or N)")
    if wants_photo == "Y":
        total_bill +=3
    else:
        total_bill = total_bill
    print(f"You final bill is {total_bill}")
else:
    print("Sorry you cannot take a rollercoster ride")