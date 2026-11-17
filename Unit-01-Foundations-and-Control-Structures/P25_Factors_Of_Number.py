# Unit 1 - P25
# Program to display all factors of a number and count them

n = int(input("Enter an integer: "))

count = 0

print("Factors of", n, "are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        count = count + 1

print()
print("Total number of factors:", count)
