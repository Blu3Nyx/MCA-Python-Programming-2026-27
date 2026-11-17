# Unit 1 - P22
# Program to check whether a number is prime using for loop

n = int(input("Enter an integer: "))

is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
