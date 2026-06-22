"""
2026/01/25
Method 1. Traverse by Value: for x in list → look only, don’t change
a = [10, 20, 30]
for x in a:
    print(x)
"""
#  Section A — Traverse by Value (for x in list)
# ⚠️ Read only — do NOT change the list

# 1. Print Values
# Given a list, print every element on a new line (Do NOT use index.)
data = [3, 6, 9, 12]
for x in data:
    print(x)

# Practice A2 — Count Specific Value
# Count how many times the number 5 appears in the list.
nums = [5, 1, 5, 2, 5, 3]
count=0
for x in nums:
    if x==5:
        count+=1
print(count)

# Practice A3 — Check Condition
# If the list contains a number greater than 10, print "YES", otherwise print "NO".
lst = [2, 4, 6, 8, 12]
for x in lst:
    if x > 10:
        print("YES")

# Practice A4 — Sum of Elements
# Find and print the sum of all numbers in the list.
a = [1, 2, 3, 4]
sum=0
for x in a :
    sum+=x
print(sum)

#  Practice A5 — Count Even Numbers
# Count how many even numbers are in the list.
b = [1, 2, 3, 4, 6, 7]
count=0
for x in b:
    if x % 2 ==0:
        count+=1
print(count)
