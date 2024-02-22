# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#calculate bmi
BMI = weight / (height**2)

status = ["are underweight", "have a normal weight", "are slightly overweight", 
         "are obese", "clinically obese"]

# check for status
if BMI < 18.5:
  status_value = status[0]
elif BMI >= 18.5 and BMI < 25:
  status_value = status[1]
elif BMI >= 25 and BMI < 30:
  status_value = status[2]
elif BMI >= 30 and BMI < 35:
  status_value = status[3]
else:
  status_value = status[4]


print(f"Your BMI is {BMI}, you {status_value}.")