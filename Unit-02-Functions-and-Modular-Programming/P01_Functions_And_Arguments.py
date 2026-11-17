# Unit 2 - P01
# Program to perform arithmetic operations using user-defined functions
# Shows positional arguments, keyword arguments and default arguments

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

# function with a default argument (default operation is addition)
def calculate(a, b, operation="add"):
    if operation == "add":
        return addition(a, b)
    elif operation == "sub":
        return subtraction(a, b)
    elif operation == "mul":
        return multiplication(a, b)
    elif operation == "div":
        return division(a, b)
    else:
        return "Invalid operation"

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# positional arguments
print("Addition:", addition(x, y))
print("Subtraction:", subtraction(x, y))
print("Multiplication:", multiplication(x, y))
print("Division:", division(x, y))

# keyword arguments (order does not matter)
print("Subtraction using keyword arguments:", subtraction(b=y, a=x))

# default argument (operation is not given, so addition happens)
print("Default operation result:", calculate(x, y))
print("Multiplication using calculate():", calculate(x, y, operation="mul"))
