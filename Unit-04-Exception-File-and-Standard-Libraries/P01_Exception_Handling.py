# Unit 4 - P01
# Program to demonstrate exception handling

# ---------- Part 1: ZeroDivisionError, ValueError, else and finally ----------
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("Error: a number cannot be divided by zero")
except ValueError:
    print("Error: please enter a valid integer")
else:
    print("Result of division:", result)
finally:
    print("This line runs every time (finally block)")

# ---------- Part 2: IndexError ----------
marks = [45, 67, 89, 72, 90]
print()
print("List of marks:", marks)

try:
    index = int(input("Enter index of the element you want to see: "))
    print("Element at index", index, "is", marks[index])
except IndexError:
    print("Error: the index is out of range")
except ValueError:
    print("Error: index must be an integer")
else:
    print("Element was accessed successfully")
finally:
    print("Index check is finished")

# ---------- Part 3: raise ----------
print()
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise Exception("Age is less than 18. You are not eligible.")
    print("You are eligible.")
except ValueError:
    print("Error: age must be a number")
except Exception as e:
    print("Error:", e)
