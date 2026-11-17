# Unit 1 - P19
# Program to find the number of digits, largest digit and smallest digit

n = int(input("Enter an integer: "))

temp = n
count = 0
largest = 0
smallest = 9

if n == 0:
    count = 1

while temp > 0:
    digit = temp % 10
    count = count + 1
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    temp = temp // 10

print("Number of digits:", count)
print("Largest digit:", largest)
print("Smallest digit:", smallest)
