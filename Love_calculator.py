

name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_name = name1 + name2
lower_case_name = combined_name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = int(str(true) + str(love))

print(f"Your love score is {love_score}%")
if love_score < 10 or love_score > 90:
    print("You go together like Coke and Mentos.")
elif 40 <= love_score <= 50:
    print("You are alright together.")
else:
    print(f"Your love score is {love_score}")
