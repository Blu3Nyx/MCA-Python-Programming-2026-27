# Unit 4 - P04
# Program to demonstrate the math library

import math

n = int(input("Enter a positive integer: "))
x = float(input("Enter a decimal number: "))
p = int(input("Enter power: "))

print("Square root of", n, "is", math.sqrt(n))
print("Factorial of", n, "is", math.factorial(n))
print(n, "raised to the power", p, "is", math.pow(n, p))
print("Ceiling of", x, "is", math.ceil(x))
print("Floor of", x, "is", math.floor(x))
