"""
2026/01/18
Traverse a List
"""
# Method 1. Traverse by Value: for x in list → look only, don’t change
a = [10, 20, 30]
for x in a:
    print(x)

# Method 2. Traverse by Index (Modify-safe)
a = [10, 20, 30]
for i in range(len(a)):
    print(a[i])

# Two methods comparison
# Practice 1
# Use x to look
a = [1, 2, 3]
for x in a:
    x = x + 1
print(a)

# Use i to change
a = [1, 2, 3]
for i in range(len(a)):
    a[i] = a[i] + 1
# len(a)=3
# i = 0: a[0] modified from 1 to 2
# i = 1: a[1] modified from 2 to 3
# i = 2: a[2] modified from 3 to 4
print(a)

# Practice — Count Even Numbers (No Modify)
# count how many numbers are even.
nums = [1, 2, 3, 4]
# Method 1 — Direct loop
count=0
for x in nums:
    if x%2==0:
        count=count+1
print(count)

#Method 2 — index loop（OK）
count=0
for i in range(len(nums)):
    if nums[i]%2==0:
        count=count+1
print(count)