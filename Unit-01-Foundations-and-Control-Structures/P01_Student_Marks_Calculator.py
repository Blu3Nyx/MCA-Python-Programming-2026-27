# Unit 1 - P01: Accept marks of five subjects and calculate
# total marks, average marks and percentage

# Step 1: Take marks of five subjects (each subject is out of 100)
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Step 2: Calculations
total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = (total / 500) * 100

# Step 3: Display the result
print("\n----- Result -----")
print("Total Marks   :", total, "/ 500")
print("Average Marks :", average)
print("Percentage    :", f"{percentage:.2f}%")
