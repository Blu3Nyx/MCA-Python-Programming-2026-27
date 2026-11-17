# Unit 4 - P03
# Program to demonstrate file methods and file related exception handling
# This program reads the file student.txt created in P02

filename = input("Enter the file name to open (for example student.txt): ")

try:
    f = open(filename, "r")

    print("File name:", f.name)
    print("File mode:", f.mode)

    # read()
    print()
    print("Using read():")
    print(f.read())

    # tell() shows the current position of the file pointer
    print("Current position after read():", f.tell())

    # seek() moves the file pointer
    f.seek(0)
    print("Position after seek(0):", f.tell())

    # readline()
    print()
    print("Using readline():")
    print(f.readline())

    # readlines()
    print("Using readlines():")
    rest = f.readlines()
    print(rest)

    f.seek(5)
    print("Position after seek(5):", f.tell())
    print("Reading 10 characters from there:", f.read(10))

except FileNotFoundError:
    print("Error: the file", filename, "was not found")
except PermissionError:
    print("Error: you do not have permission to open this file")
else:
    print()
    print("File operations completed without any error")
    f.close()
finally:
    print("Program finished")
