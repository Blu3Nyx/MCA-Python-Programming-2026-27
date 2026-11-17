# Unit 1 - P02: Employee salary calculator
# Accept basic salary and calculate DA, HRA, gross salary, tax and net salary

# Rates used in this program (you can change them)
DA_RATE = 20      # Dearness Allowance = 20% of basic
HRA_RATE = 10     # House Rent Allowance = 10% of basic
TAX_RATE = 10     # Tax = 10% of gross salary

basic = float(input("Enter basic salary: "))

da = basic * DA_RATE / 100
hra = basic * HRA_RATE / 100
gross = basic + da + hra
tax = gross * TAX_RATE / 100
net = gross - tax

print("\n----- Salary Slip -----")
print(f"Basic Salary : {basic:.2f}")
print(f"DA (20%)     : {da:.2f}")
print(f"HRA (10%)    : {hra:.2f}")
print(f"Gross Salary : {gross:.2f}")
print(f"Tax (10%)    : {tax:.2f}")
print(f"Net Salary   : {net:.2f}")
