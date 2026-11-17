# Unit 1 - P16
# Program to reverse the digits of a number using while loop

n = int(input("Enter an integer: "))

temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reverse of", n, "is", rev)
