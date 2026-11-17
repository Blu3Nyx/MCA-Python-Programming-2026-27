# Unit 1 - P26
# Program to find GCD and LCM of two positive numbers using loops

a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

# GCD: check numbers from 1 up to the smaller number
if a < b:
    smaller = a
else:
    smaller = b

gcd = 1
for i in range(1, smaller + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

# LCM = (a * b) / gcd
lcm = (a * b) // gcd

print("GCD of", a, "and", b, "is", gcd)
print("LCM of", a, "and", b, "is", lcm)
