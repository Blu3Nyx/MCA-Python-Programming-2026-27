# Unit 2 - P03
# Program to find factorial and Fibonacci series using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter a number to find factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of", num, "is", factorial(num))

terms = int(input("Enter number of terms for Fibonacci series: "))
print("Fibonacci series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()
