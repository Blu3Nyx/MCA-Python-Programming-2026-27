# Unit 1 - P12
# Program to check admission eligibility
# Conditions: at least 50 marks in each subject and at least 60 percent overall

maths = float(input("Enter marks in Mathematics: "))
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))

total = maths + physics + chemistry
percentage = total / 300 * 100

print("Total marks:", total)
print("Percentage:", percentage)

if maths >= 50 and physics >= 50 and chemistry >= 50 and percentage >= 60:
    print("The student is eligible for admission.")
else:
    print("The student is not eligible for admission.")
