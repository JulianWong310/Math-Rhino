"""
2026/01/25
FINAL RULE SUMMARY (Very Important)
1. for x in list → read only
2. for i in range(len(list)) → can change
3. use i+1 → loop must stop early
"""

# Section 1. Neighbor / i + 1
# Practice C1 — Adjacent Same Check
# If two adjacent numbers are equal, print "YES", otherwise print "NO".
nums = [1, 2, 2, 3]
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        print("YES")
        break
else:
    print("NO")

# Practice 2 — Count Adjacent Matches
# Count how many times two neighboring numbers are the same.
data = [4, 4, 2, 3, 3, 3]
count=0
for i in range(len(data)-1):
    if data[i]==data[i+1]:
        count+=1
print(count)

# Practice C3 — Increasing Neighbor
# Count how many times the next number is bigger than the current number.
lst = [1, 3, 2, 4, 3]
count=0
for i in range(len(lst)-1):
    if lst[i]<lst[i+1]:
        count+=1
print(count)

# Section 2 — Reverse Traversal (Backwards)
#  Practice 1 — Reverse and Print
# Reverse the list, then print all elements.
a = [1, 2, 3]
b=a.copy()
b.reverse()
for x in b :
    print(x)

#  Practice 2 — Print from Last to First (Index Way)
# Print all elements from last to first (Do NOT change the list.)
nums = [5, 6, 7, 8]
for i in range(len(nums)-1,-1,-1):
    print(nums[i])