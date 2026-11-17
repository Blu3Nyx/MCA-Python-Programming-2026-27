# Unit 1 - P23
# Program to display all prime numbers in a given range and count them

start = int(input("Enter starting number of range: "))
end = int(input("Enter ending number of range: "))

count = 0

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num, end=" ")
            count = count + 1

print()
print("Total prime numbers found:", count)
