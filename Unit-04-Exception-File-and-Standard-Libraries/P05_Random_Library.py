# Unit 4 - P05
# Program to demonstrate the random library

import random

# random integer between two numbers
print("Random integer between 1 and 100:", random.randint(1, 100))

# random element from a list
fruits = ["apple", "banana", "mango", "orange", "grapes"]
print("Random fruit from the list:", random.choice(fruits))

# shuffle the list
print("List before shuffle:", fruits)
random.shuffle(fruits)
print("List after shuffle:", fruits)
