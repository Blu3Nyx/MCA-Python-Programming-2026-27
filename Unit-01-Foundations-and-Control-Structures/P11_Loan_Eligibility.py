# Unit 1 - P11
# Program to check loan eligibility
# Conditions: age 21 to 60, monthly income at least 25000, credit score at least 700

age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
score = int(input("Enter credit score: "))

if age >= 21 and age <= 60 and income >= 25000 and score >= 700:
    print("Congratulations! You are eligible for the loan.")
else:
    print("Sorry, you are not eligible for the loan.")
    if age < 21 or age > 60:
        print("Reason: age should be between 21 and 60")
    if income < 25000:
        print("Reason: monthly income should be at least 25000")
    if score < 700:
        print("Reason: credit score should be at least 700")
