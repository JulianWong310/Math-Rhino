"""
2026/01/17
LIST PRACTICE
list is mutable which means it is changeable.
A list can be changed.
Numbers and strings cannot.
"""

# 1. Create a List
# For each variable below, write YES if it is a list, NO if it is not.
a = [1, 2, 3] # YES
b = "123" # NO
c = [] # YES
d = list("ABC") # YES
e = 10 # YES

# Create a list called nums containing numbers from 1 to 5
nums=[1,2,3,4,5]
# Create an empty list called data
data=[]
# Convert the string "HELLO" into a list of characters
lst=list("HELLO")

# Given a = [10, 20, 30, 40]  Answer the following without running code:
# What is a[0]  10
# What is a[2] 30
# What is a[len(a) - 1]  40

# 2 Modifying by Index
a = [5, 6, 7, 8]
# Change the first element to 100
a[0]=100
# Change the last element to 0
a[3]=0

#3 Index Error Check
#Which of the following lines cause an index error?
a = [1, 2, 3]
# a[3] = 10 # Wrong
a[-1] # Correct
# a[len(a)] # Wrong, out of range

# 4 append()
# Start with an empty list. Add numbers 1, 2, 3, 4 one by one using append().
a=[]
a.append(1)
a.append(2)
a.append(3)
a.append(4)

# 5 Build a New List
nums = [1, 2, 3, 4, 5]
# Create a new list containing only even numbers.
nums1=[]
for x in nums:
    if x%2==0:
        nums1.append(x)

# 6. pop()
# pop() Without Index
a = [10, 20, 30]
# Remove the last element,and print the list after removal
a.pop()

#  pop(i)
a = [5, 6, 7, 8]
# Remove the element at index 1.
a.pop(1)
# Keep removing the last element of a list until the list is empty.
# Count how many elements were removed.
a = [5, 7, 8]
# wrong ❌
# count=0
# for x in a:
#     a.pop()
#     count=count+1
#     print(a)
# print(count)

# right ✅
count=0
while len(a)>0:
    a.pop()
    count=count+1
print(count)

# 7 remove(x)
a = [1, 2, 3, 2, 4]
a.remove(2) # What does the list become?
# a=[1,3,2,4]

# 8 remove vs pop (Explain)
# Explain in your own words: difference between remove(x) and pop(i)
# Which one uses value, which one uses index
# Remove uses value, pop uses index

# 9 Mistake Detection
# What is wrong with this code if we need to remove all the even numbers.
nums = [1, 2, 3, 4]
for x in nums:
    if x % 2 == 0:
        nums.remove(x)
# it will skip the number after the number has been deleted

# correction
nums = [1, 2, 3, 4]
num1=[]
for x in nums:
    if x%2==1:
        num1.append(x)

# 10 count(x): counting Elements
a = [1, 2, 2, 3, 2, 4] # Write code to print how many times 2 appears.
num=a.count(2)
print(num)

# 11 sort(): sorting Numbers from small to big (ascending)
a = [4, 1, 3, 2] # Write code to sort the list in ascending order.
# Given a list of scores, find the largest score after sorting.
a.sort()
print(a)

# 12 reverse: reverse a List
a = [1, 2, 3, 4] # reverse the list in place. ( modify the same list without creating new)
a.reverse()
print(a)

# 13 List Copy vs Reference
a = [1, 2, 3]
b = a
c = a.copy()  # or c = a[:]
# Modify the original list
a.append(4)
# Predict what b and c will contain after the modification
# b = [ ? ]
print(b)
# c = [ ? ]
print(c)

# 14 Combined
# Remove All Zeros (VERY IMPORTANT)
nums = [0, 1, 0, 2, 3, 0] # remove all zeros from the list.
#⚠️ Do NOT remove while traversing the same list.
num1=[]
for x in nums:
    if x!=0:
        num1.append(x)
print(num1)

# 15 String → List → String (Modify Characters)
s = "ABRAKADABRA"
# Convert the strings into a list of characters
#  Change all 'A' characters to 'B'
# Convert the list back into a string
# Print the final string
# Expected Output: BBRBKBDBBRB
a=list(s)
print(a)
for i in range (len(a)):
   if  a[i]=="A":
       a[i]="B"
b="".join(a)
print(b)

# 16 Membership Test (in)
nums = [0, 3, 5, 0, 7, 2]
# Check whether the number 0 appears more than once in the list
# If it appears at least once, print: YES
# Otherwise, print: NO
# Expected Output: YES
if 0 in nums:
    print("YES")
else:
    print("NO")