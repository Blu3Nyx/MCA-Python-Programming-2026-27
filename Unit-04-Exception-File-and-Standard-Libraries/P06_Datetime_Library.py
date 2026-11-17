# Unit 4 - P06
# Program to demonstrate the datetime library

from datetime import datetime

now = datetime.now()

print("Current date and time:", now)
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)

# difference between two dates
d1 = input("Enter first date (DD-MM-YYYY): ")
d2 = input("Enter second date (DD-MM-YYYY): ")

date1 = datetime.strptime(d1, "%d-%m-%Y")
date2 = datetime.strptime(d2, "%d-%m-%Y")

difference = date2 - date1
print("Difference between the two dates:", abs(difference.days), "days")
