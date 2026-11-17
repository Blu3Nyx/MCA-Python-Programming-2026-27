# Unit 3 - P04
# Program to perform operations on tuples and sets

# ---------- Tuple part ----------
rolls = (101, 102, 103, 104, 105, 106)
print("Tuple of roll numbers:", rolls)

print("First element:", rolls[0])
print("Last element:", rolls[-1])
print("Slice [1:4]:", rolls[1:4])

more = (107, 108)
print("After concatenation:", rolls + more)

# ---------- Set part ----------
mca = {101, 102, 103, 104, 105}
mba = {104, 105, 106, 107}

print()
print("MCA students:", mca)
print("MBA students:", mba)

print("Union:", mca | mba)
print("Intersection:", mca & mba)
print("Difference (MCA - MBA):", mca - mba)
print("Symmetric difference:", mca ^ mba)

# subset and superset
small = {101, 102}
print("Is small a subset of MCA?", small.issubset(mca))
print("Is MCA a superset of small?", mca.issuperset(small))

# add and remove
mca.add(110)
print("After adding 110:", mca)
mca.remove(101)
print("After removing 101:", mca)

# set comprehension
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
squares = {x * x for x in range(start, end + 1) if x % 2 == 0}
print("Squares of even numbers:", squares)
