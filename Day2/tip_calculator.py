print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_split = int(input("How many people to split the bill? "))
tip = bill * (tip_percentage/100)
total_bill = bill + tip
pay_amount = round(total_bill / bill_split, 2)
print(f"Each person should pay {pay_amount}")
