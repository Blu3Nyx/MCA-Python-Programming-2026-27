# Unit 4 - P02
# Program to write, read and append data in a text file named student.txt

# ---------- writing ----------
f = open("student.txt", "w")

n = int(input("How many student records do you want to write? "))
for i in range(n):
    name = input("Enter name of student " + str(i + 1) + ": ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    f.write(roll + "," + name + "," + course + "\n")

f.close()
print("Data written to student.txt")

# ---------- reading the complete file ----------
f = open("student.txt", "r")
print()
print("Complete file contents:")
print(f.read())
f.close()

# ---------- appending ----------
f = open("student.txt", "a")
m = int(input("How many more records do you want to append? "))
for i in range(m):
    name = input("Enter name of student " + str(i + 1) + ": ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    f.write(roll + "," + name + "," + course + "\n")
f.close()
print("Records appended")

# ---------- reading line by line ----------
f = open("student.txt", "r")
print()
print("Reading line by line:")
line = f.readline()
while line != "":
    print(line.strip())
    line = f.readline()
f.close()

# ---------- reading all lines using readlines() ----------
f = open("student.txt", "r")
lines = f.readlines()
print()
print("Total lines in the file:", len(lines))
for l in lines:
    print(l.strip())
f.close()
