# Unit 1 - P27
# Program to display multiplication tables from 1 to 10 in table format

print("Multiplication Table (1 to 10)")
print()

# header row
print("   ", end="")
for j in range(1, 11):
    print(j, end="\t")
print()
print("-" * 90)

for i in range(1, 11):
    print(i, end=" |\t")
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
