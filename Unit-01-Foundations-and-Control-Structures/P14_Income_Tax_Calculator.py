# Unit 1 - P14
# Program to calculate income tax according to slabs
# Up to 3,00,000      -> no tax
# 3,00,001 - 6,00,000 -> 5% on the amount above 3,00,000
# 6,00,001 - 9,00,000 -> 10% on the amount above 6,00,000 (plus 15000)
# Above 9,00,000      -> 15% on the amount above 9,00,000 (plus 45000)

income = float(input("Enter annual income: "))

if income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 5 / 100
elif income <= 900000:
    tax = 15000 + (income - 600000) * 10 / 100
else:
    tax = 45000 + (income - 900000) * 15 / 100

print("Annual income:", income)
print("Tax payable:", tax)
