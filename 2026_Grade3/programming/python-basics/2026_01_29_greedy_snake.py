"""
2026/01/29
max_val = float('-inf')
min_val = float('inf')
for each value v:
    if max_val< v:
        max_val = v
    if min_val > v:
        min_val = v
"""
# Practice 1
nums = [5, 3, 9, 1, 7] # find biggest and smallest numbers in the list
max_=float("-inf")
for x in nums:
    if max_<x:
        max_=x
min_=float("inf")
for x in nums:
    if min_>x:
        min_=x
print(max_)
print(min_)

# Practice 2
nums = [8, 10, 10, 6] # find second largest number
largest = float('-inf')
second = float('-inf')
for x in nums:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x < largest:
        second = x
print(second)
print(largest)

# Practice 3
listA = [7, 2, 10, 5, 8]
listB = [3, 4, 6, 9, 1]
#  the maximum difference between the two list of the same position
max_=float("-inf")
for i in range(len(listA)):
    diff=listA[i]-listB[i]
    if max_< diff:
        max_=diff
print(max_)

# Practice 4
nums = [7, 1, 5, 3, 6, 4]  # Find the maximum difference between two numbers i+1-i
max_diff = float("-inf")
for i in range(len(nums)-1):
    diff = nums[i+1]-nums[i]
    if max_diff<diff:
        max_diff=diff
print(max_diff)

"""
Practice 5
The Fence Designer Problem
Description:Julian wants to build a rectangular fence for his garden.
The area of the garden must be exactly 1200 square units.
To save money on materials, Julian wants the perimeter (the distance around the garden) to be as short as possible.
The Length and Width of the garden must be integers (whole numbers)           
Write a Python program to find the Length and Width that result in the smallest perimeter.
What is the value of the minimum perimeter?
"""
# Method 1
min_p=float("inf")
for i in range(1,1201):
    if 1200% i ==0:
        j=1200//i
        p=i+j
        if min_p>p:
            min_p=p
            w=i
            l=j
print(p*2)
print(min_p*2)
print(w,l)

# Method 2
min_diff=float("inf")
for i in range(1,1201):
    if 1200% i ==0:
        j=1200//i
        x=j-i
        if x<min_diff and x >=0:
            min_diff=x
            w=i
            l=j
print(min_diff)
print((w+l)*2)