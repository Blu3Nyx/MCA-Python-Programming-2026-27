# Unit 1 - P18
# Program to find the sum and product of digits of a number using while loop

n = int(input("Enter an integer: "))

temp = n
total = 0
product = 1

while temp > 0:
    digit = temp % 10
    total = total + digit
    product = product * digit
    temp = temp // 10

print("Sum of digits:", total)
print("Product of digits:", product)
