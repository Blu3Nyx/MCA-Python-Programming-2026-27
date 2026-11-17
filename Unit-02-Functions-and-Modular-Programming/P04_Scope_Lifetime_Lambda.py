# Unit 2 - P04
# Program to show scope and lifetime of variables and use of lambda functions

x = 10      # global variable (lives until the program ends)

def show_local():
    y = 5   # local variable (created when function starts, destroyed when it ends)
    print("Inside function: local y =", y)
    print("Inside function: global x =", x)

def change_global():
    global x
    x = x + 90
    print("Inside function: global x changed to", x)

def shadow_example():
    x = 1   # this is a new local variable, it does not change the global x
    print("Inside function: local x =", x)

print("Outside: global x =", x)
show_local()
shadow_example()
print("Outside after shadow_example(): global x =", x)
change_global()
print("Outside after change_global(): global x =", x)

# y cannot be used here because it died when show_local() finished
try:
    print(y)
except NameError:
    print("Cannot access y outside the function (its lifetime is over)")

# lambda functions
square = lambda n: n * n
cube = lambda n: n * n * n
maximum = lambda a, b: a if a > b else b
add = lambda a, b: a + b

num = int(input("Enter a number: "))
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))

print("Square of", num, "is", square(num))
print("Cube of", num, "is", cube(num))
print("Maximum of", p, "and", q, "is", maximum(p, q))
print("Addition of", p, "and", q, "is", add(p, q))
