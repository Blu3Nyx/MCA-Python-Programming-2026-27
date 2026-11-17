# Unit 2 - P02
# Program to calculate total, average and highest marks of a student
# Uses *args for marks and **kwargs for extra student information

def result(*marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    return total, average, highest

def show_info(**details):
    for key in details:
        print(key, ":", details[key])

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

marks_list = []
for i in range(1, n + 1):
    subject = input("Enter name of subject " + str(i) + ": ")
    m = float(input("Enter marks in " + subject + ": "))
    marks_list.append(m)

roll = input("Enter roll number: ")
cls = input("Enter class: ")

total, average, highest = result(*marks_list)

print()
print("========== STUDENT RESULT ==========")
print("Name :", name)
show_info(RollNo=roll, Class=cls)
print("Total marks   :", total)
print("Average marks :", round(average, 2))
print("Highest marks :", highest)
print("====================================")
