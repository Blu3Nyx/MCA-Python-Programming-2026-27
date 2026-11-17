# Unit 3 - P01
# Program to perform different string operations and use string methods

sentence = input("Enter a sentence: ")

# length of the string
print("Length of the string:", len(sentence))

# uppercase and lowercase
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

# removing leading and trailing spaces
print("After removing extra spaces:", sentence.strip())

# replacing a word
old = input("Enter the word you want to replace: ")
new = input("Enter the new word: ")
print("After replacing:", sentence.replace(old, new))

# counting a character
ch = input("Enter a character to count: ")
print("The character", ch, "appears", sentence.count(ch), "times")

# starts with and ends with
start = input("Enter a substring to check at the start: ")
end = input("Enter a substring to check at the end: ")
print("Starts with", start, ":", sentence.strip().startswith(start))
print("Ends with", end, ":", sentence.strip().endswith(end))

# concatenation, repetition and membership
s1 = "Hello"
s2 = "Python"
print("Concatenation:", s1 + " " + s2)
print("Repetition:", s1 * 3)
print("Is 'Py' in s2?", "Py" in s2)
print("Is 'java' not in s2?", "java" not in s2)
