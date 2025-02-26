# 1st input: Enter Height in Metres
height = input("Enter Height in Metres: ")
# 2nd input: Enter Weight in Kilograms  
weight = input("Enter Weight in Kilograms: ")
# Calculate BMI 
bmi = float(weight) / (float(height) ** 2)
# Print BMI
print("Your BMI is: ", bmi)

# Determine weight category
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
