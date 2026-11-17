# Unit 2 - P05
# Program to use user-defined modules and packages
# Needs arithmetic.py and the student package (folder) in the same folder as this file

# importing the entire module
import arithmetic

# importing selected functions
from arithmetic import add, multiply

# importing the package (selected functions come from __init__.py)
import student
from student import details, results

print("---- Using the whole module ----")
print("Addition:", arithmetic.add(20, 10))
print("Subtraction:", arithmetic.subtract(20, 10))
print("Multiplication:", arithmetic.multiply(20, 10))
print("Division:", arithmetic.divide(20, 10))

print()
print("---- Using selected functions ----")
print("add(5, 3) =", add(5, 3))
print("multiply(5, 3) =", multiply(5, 3))

print()
print("---- Using the student package ----")
student.show_details("Anjali", 101, "MCA")
print(details.get_details("Anjali", 101, "MCA"))

marks = [78, 85, 90, 67, 72]
print("Total marks:", student.calculate_total(marks))
per = results.calculate_percentage(marks)
print("Percentage:", per)
print("Result:", student.get_grade(per))
