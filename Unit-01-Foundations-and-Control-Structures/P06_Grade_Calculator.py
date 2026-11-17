# Unit 1 - P06
# Program to find the grade of a student using if-elif-else

per = float(input("Enter percentage: "))

if per < 0 or per > 100:
    print("Invalid percentage! It should be between 0 and 100.")
elif per >= 90:
    print("Grade: A+")
elif per >= 80:
    print("Grade: A")
elif per >= 70:
    print("Grade: B")
elif per >= 60:
    print("Grade: C")
elif per >= 40:
    print("Grade: D")
else:
    print("Grade: F (Fail)")
