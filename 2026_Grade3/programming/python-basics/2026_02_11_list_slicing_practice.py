"""
2026/01/14
Slicing does NOT change the original list but creates a NEW list
"""
# Level 1 — Basic Slicing (Must Know)
# a[start : end: step]   # start included, end NOT included
a = [10, 20, 30, 40]
a[1:3]    # [20, 30]
a[:2]     # [10, 20]
a[2:]     # [30, 40]
a[: :2]   # [10,30]
a[::-1]   # reverse the list [40,30,20,10]
a[-2:]    # [30,40]

# Practice 1.1 — Middle Slice
a = [10, 20, 30, 40, 50] # Print a new list containing 20, 30, 40 using slicing.
b=a[1:4]
print(b)
print(a)

# Practice 1.2 — First Part
a = [5, 6, 7, 8] # Print the first two elements using slicing.
print(a[:2])

# Practice 1.3 — Last Part
#Print a new list containing the last three elements.
a = [1, 2, 3, 4, 5]
print(a[-3:])

# Practice 1.4
# Print a new list containing the last three elements in a reverse order: a[-1:-len(a)-1:-1]
print(a[-1:-4:-1])
print(a[4:1:-1])

# Level 2 — Using : Correctly
# Practice 2.1 — From Start
a = [100, 200, 300, 400] # Use slicing to get all elements before index 2.
print(a[:2])

# Practice 2.2 — To the End
a = [9, 8, 7, 6, 5] # Use slicing to get all elements from index 2 to the end.
print(a[2:])

# Practice 2.3 — Full Copy
a = [1, 3, 5, 7] # Make a copy of the list using slicing and print both lists.
b=a[:]
print(a,b)

# Level 3 — Concept Checks (VERY IMPORTANT)
# Practice 3.1 — Does slicing Change the List? No
a = [2, 4, 6, 8]
b = a[1:3]
print (b)
print(a)

# Practice 3.2 — Modify the Slice
a = [10, 20, 30, 40]
b = a[:2]
b[0] = 99
print (b)
print (a)

# Level 4 — Combine Slicing + Traversal
# Practice 4.1 — Traverse a Slice
a = [1, 2, 3, 4, 5, 6] # Use slicing to take [3, 4, 5], then print each number on a new line.
b=a[2:5]
for x in b:
    print(x)

# Practice 4.2 — Modify a Slice
a = [2, 4, 6, 8] #Try to multiply only the middle two numbers by 2 using slicing.
b=a[1:3]
for i in range(len(b)):
    b[i]=b[i]*2 # b[0]=4*2, b[1]=8*2
print(b)

# Level 5 — CCCJ Trap Questions (Exam Favorite)
# Practice 5.1 — Predict the Output
a = [1, 2, 3, 4]
b = a[1:]
b.append(5)
print(a)
print(b) # [2,3,4,5]

# Practice 5.2 — True or False
# Write True or False
# a[:] creates a new list  YES
# Changing a slice will change the original list NO
# Slicing can cause index out of range YES
a = [1, 2, 3]
print(a[0:10])   # [1,2,3]
# print(a[10])   # wrong


