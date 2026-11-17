# details.py
# Module for student details

def get_details(name, roll_no, course):
    return "Name: " + name + ", Roll No: " + str(roll_no) + ", Course: " + course

def show_details(name, roll_no, course):
    print("----- Student Details -----")
    print("Name   :", name)
    print("Roll No:", roll_no)
    print("Course :", course)
