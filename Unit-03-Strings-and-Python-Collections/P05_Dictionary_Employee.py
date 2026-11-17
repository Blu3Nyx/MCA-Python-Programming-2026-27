# Unit 3 - P05
# Program to maintain employee information using dictionaries

employees = {
    101: {"name": "Amit", "department": "IT", "salary": 50000},
    102: {"name": "Sneha", "department": "HR", "salary": 40000},
    103: {"name": "Rahul", "department": "Finance", "salary": 60000}
}

print("Employee data:", employees)

# add a new employee
employees[104] = {"name": "Priya", "department": "IT", "salary": 55000}
print("After adding employee 104:", employees[104])

# update an employee
employees[102]["salary"] = 45000
print("After updating salary of 102:", employees[102])

# delete an employee
del employees[103]
print("After deleting employee 103, IDs are:", list(employees.keys()))

# keys, values and items
print()
print("Keys:", employees.keys())
print("Values:", employees.values())
print("Items:")
for emp_id, info in employees.items():
    print(emp_id, "->", info)

# search an employee by id
search_id = int(input("Enter employee ID to search: "))
if search_id in employees:
    info = employees[search_id]
    print("Employee found")
    print("Name:", info["name"])
    print("Department:", info["department"])
    print("Salary:", info["salary"])
else:
    print("Employee not found")

# dictionary comprehension
limit = int(input("Enter salary limit: "))
high = {i: info for i, info in employees.items() if info["salary"] > limit}
print("Employees earning above", limit, ":")
for i in high:
    print(i, "->", high[i]["name"], high[i]["salary"])
