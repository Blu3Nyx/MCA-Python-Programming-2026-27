# Unit 1 - P17
# Program to check whether a number is a palindrome using while loop

n = int(input("Enter an integer: "))

temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if rev == n:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")
