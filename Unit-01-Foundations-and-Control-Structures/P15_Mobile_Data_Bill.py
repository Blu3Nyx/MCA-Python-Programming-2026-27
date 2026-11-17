# Unit 1 - P15
# Program to calculate mobile data bill according to usage slabs
# Up to 2 GB     -> fixed charge of 200
# Next 3 GB      -> 50 per GB (above 2 GB up to 5 GB)
# Above 5 GB     -> 80 per GB

gb = float(input("Enter data used in GB: "))

if gb <= 2:
    bill = 200
elif gb <= 5:
    bill = 200 + (gb - 2) * 50
else:
    bill = 200 + (3 * 50) + (gb - 5) * 80

print("Data used:", gb, "GB")
print("Total bill: Rs", bill)
