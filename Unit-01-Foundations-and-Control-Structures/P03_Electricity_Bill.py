# Unit 1 - P03: Electricity bill using consumption slabs
# Slabs:  First 100 units  -> Rs 5 per unit
#         Next 100 units   -> Rs 7 per unit   (101 to 200)
#         Next 100 units   -> Rs 10 per unit  (201 to 300)
#         Above 300 units  -> Rs 12 per unit

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
elif units <= 300:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + (units - 300) * 12

print("\n----- Electricity Bill -----")
print("Units consumed :", units)
print("Total bill     : Rs", bill)
