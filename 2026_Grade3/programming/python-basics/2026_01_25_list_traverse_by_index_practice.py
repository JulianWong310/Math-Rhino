"""
2026/01/25
Method 2. Traverse by Index (Modify-safe)
a = [10, 20, 30]
for i in range(len(a)):
    print(a[i])
"""

# Section B — Traverse by Index (for i in range(len(list)))
# ⚠️ Modify-safe — can change the list

# Practice B1 — Print Index and Value
nums = [10, 20, 30]
# Print output like this:
# Index 0: 10
# Index 1: 20
# Index 2: 30
for i in range(len(nums)):
    print(f"Index {i}: {nums[i]}")

# Practice B2 — Add 1 to Each Number
# Modify the list so every number increases by 1.
data = [4, 5, 6]
for i in range(len(data)):
    data[i]=data[i]+1
print(data)

# Practice B3 — Multiply by 2
# Multiply every number by 2 inside the same list. ⚠️ You MUST use index traversal.
b = [2, 4, 6, 8]
for i in range(len(b)):
    b[i]*=2
print(b)

# Practice B4 — Change by Condition
# Change every number greater than 5 to 0.
a = [2, 6, 3, 8, 4]
for i in range(len(a)):
    if a[i]>5:
        a[i]=0
print(a)

# Practice B5 — Replace Value
# Replace all 3s in the list with 9.
lst = [3, 1, 3, 5, 3]
for i in range(len(lst)):
    if lst[i]==3:
        lst[i]=9
print(lst)

# Practice B6 — Sort Value
# given a list a = [1, 2, 3, 4], print all elements from last to first.
# Method 1 — Using reverse()
a = [1, 2, 3, 4]
a.reverse()
for x in a:
    print(x)

"""
reverse() changes the list
If you need the original list later, make a copy first
b = a.copy()
b.reverse()
"""

# Method 2 — Using Index Traversal (No list change)
a = [1, 2, 3, 4]
for i in range(len(a)-1, -1,-1):
    print(a[i])