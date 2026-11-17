# results.py
# Module for student results

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    return sum(marks) / len(marks)

def get_grade(percentage):
    if percentage >= 75:
        return "Distinction"
    elif percentage >= 60:
        return "First Class"
    elif percentage >= 40:
        return "Pass"
    else:
        return "Fail"
