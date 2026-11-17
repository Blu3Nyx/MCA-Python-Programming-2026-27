# Unit 1 - P09
# Program to check whether a year is a leap year or not

year = int(input("Enter a year: "))

# divisible by 400, OR divisible by 4 but not by 100
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
