# Unit 1 - P20
# Program to check whether a number is an Armstrong number
# Example: 153 = 1^3 + 5^3 + 3^3

n = int(input("Enter an integer: "))

# first count the digits
temp = n
count = 0
while temp > 0:
    count = count + 1
    temp = temp // 10

# now add each digit raised to the power of count
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10

if total == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
