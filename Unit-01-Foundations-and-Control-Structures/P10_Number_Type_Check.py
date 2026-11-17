# Unit 1 - P10
# Program to check whether a number is positive, negative, zero, even or odd

n = int(input("Enter an integer: "))

if n == 0:
    print("The number is zero")
elif n > 0:
    print("The number is positive")
else:
    print("The number is negative")

# even or odd check (zero is also an even number)
if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
