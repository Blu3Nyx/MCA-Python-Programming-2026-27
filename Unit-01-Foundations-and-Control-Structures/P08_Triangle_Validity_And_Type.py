# Unit 1 - P08
# Program to check whether three sides form a triangle
# and to find its type (Equilateral, Isosceles or Scalene)

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# a triangle is valid only if the sum of any two sides is greater than the third side
if a + b > c and b + c > a and a + c > b:
    print("The sides form a valid triangle.")

    if a == b and b == c:
        print("Type: Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Type: Isosceles triangle")
    else:
        print("Type: Scalene triangle")
else:
    print("The sides do not form a valid triangle.")
