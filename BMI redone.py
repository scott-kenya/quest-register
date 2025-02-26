# 1st input: Enter your name
name = input("Enter your name: ")
# 2nd input: Enter height in metres.
height = input("Enter your height in metres: ")
# 3rd input: Enter weight in kilograms
weight = input("Enter your weight in kilograms: ")
# 4th input: Enter age in years
age = input("Enter your age in years: ")
# 5th input: your gender M/F
gender = input("Enter your gender M/F: ")
# 6th input: your activity level on a scale of 1-5
Activity = input("Enter your activity level on a scale of 1-5: ")
# 7th input: your goal: lose weight, gain weight, maintain weight
Targetgoal = input("Enter your goal: lose weight, gain weight, maintain weight: ")
# 8th input: your target weight in kilograms
Targetweight = input("Enter your target weight in kilograms: ")

bmi = float(weight) / (float(height)**2)
#print(bmi)
print("Hello", name, "your BMI is", bmi)

# To determine if the person is underweight, normal weight, overweight or obese
if bmi < 18.5:
    print("Wacha kujinyima")
elif 18.5 <= bmi < 24.9:
    print("Uko sawa ")
elif 25 <= bmi < 29.9:
    print("Fanya tizi", name, "umezidi")
