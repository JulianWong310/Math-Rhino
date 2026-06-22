"""
2026/01/18
⚠️ COMMON MISTAKES (VERY IMPORTANT)
1. ❌ Assume remove() removes all values
2. ❌ Modify list while looping with for x in list
3. ❌ Forget list is mutable
4. ❌ a = a.sort()
5. ❌ Index out of range (i+1)
"""

# 1 remove(x) only removes the first x in the list, not all.
a = [1, 2, 3, 2, 4]
a.remove(2) # What does the list become?
print(a)

# 2 When you loop with for x in list:, never modify the list itself inside the loop.
# e.g: remove all the even number from the list
nums = [1, 2, 3, 4, 6, 8]
# wrong
for x in nums:
    print(x)
    if x % 2 == 0:
        nums.remove(x)
        print(nums)

# correct: create a new empty list, instead of remove x , we should append the "non x" to the list
nums = [1, 2, 3, 4, 6, 8]
num1=[]
for x in nums:
    if x % 2 == 1:
        num1.append(x)
print(num1)

# 3 List is mutable
a = [1, 2, 3]
b = a
c = a.copy() # or b = a[:]
a.append(4)
print(b)# result?
print(c)# result?

# 4 sort(), append(x),remove(x) changes the list itself and returns nothing (None).
a = [3, 1, 2, 9]
# Wrong
a = a.sort()
print(a) # None
a=a.append(4)
# print(a) # None
a=a.remove(3)
print(a) # None
a=a.pop(3)
print(a) # 9
a=a.count(3)
print(a) # 1

# 5 Check if out of range
a=[1, 2, 3, 3, 4]
# 1 out of range
a[len(a)]=3

# 2 correct range
for i in range (len(a)):
    print(a[i])

# 3 Check two neighbors i + 1
for i in range(len(a)-1):
    if a[i] == a[i + 1]: # len(a)=5, i<=2: 0,1,2
        print("YES")
# If you use i + 1, your loop MUST be: range(len(list) - 1)

# Practice  — Adjacent Check Using List
nums = [3, 5, 5, 2, 7]
# Check whether the list contains two adjacent numbers that are equal
# If yes, print "YES", Otherwise, print "NO"
# Compare neighboring elements only (nums[i] and nums[i+1])
# Expected Output: YES
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        print("YES")