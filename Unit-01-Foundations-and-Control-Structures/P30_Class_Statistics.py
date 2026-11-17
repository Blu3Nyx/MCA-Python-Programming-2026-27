# Unit 1 - P30
# Program to accept marks of N students and find class average, highest, lowest,
# number of passed, failed and students scoring above 75%
# Marks are out of 100, pass marks = 40

n = int(input("Enter number of students: "))

total = 0
highest = 0
lowest = 100
passed = 0
failed = 0
above75 = 0

for i in range(1, n + 1):
    marks = float(input("Enter marks of student " + str(i) + ": "))

    total = total + marks

    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks

    if marks >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    if marks > 75:
        above75 = above75 + 1

average = total / n

print()
print("Class average:", average)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Number of students passed:", passed)
print("Number of students failed:", failed)
print("Students scoring above 75%:", above75)
