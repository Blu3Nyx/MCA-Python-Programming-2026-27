# Unit 3 - P03
# Program to perform operations on a list of integers

n = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(n):
    x = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(x)

print("Original list:", numbers)

# insert and remove at specified positions
pos = int(input("Enter position to insert at: "))
val = int(input("Enter value to insert: "))
numbers.insert(pos, val)
print("After insert():", numbers)

pos = int(input("Enter position to remove from: "))
removed = numbers.pop(pos)
print("Removed element:", removed)
print("After pop():", numbers)

# sorting
numbers.sort()
print("Ascending order:", numbers)
numbers.sort(reverse=True)
print("Descending order:", numbers)
numbers.reverse()
print("After reverse():", numbers)

# max, min and sum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# append, extend and remove
numbers.append(100)
print("After append(100):", numbers)
numbers.extend([7, 8, 9])
print("After extend([7, 8, 9]):", numbers)
numbers.remove(100)
print("After remove(100):", numbers)

# concatenation, repetition, indexing and membership
a = [1, 2, 3]
b = [4, 5]
print("Concatenation:", a + b)
print("Repetition:", a * 2)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Is 7 in the list?", 7 in numbers)

# list comprehension
print("Even numbers:", [x for x in numbers if x % 2 == 0])
print("Odd numbers:", [x for x in numbers if x % 2 != 0])
print("Squares:", [x * x for x in numbers])
