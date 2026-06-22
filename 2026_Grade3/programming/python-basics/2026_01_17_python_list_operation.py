""""
2026/01/17
# Python List — All Common Operations
# Operation    Modify List?    Use
# ----------   ------------    ----------
# append()     YES             build
# pop()        YES             simulate
# remove()     YES             delete
# count()      NO              frequency
# sort()       YES             ranking
# reverse()    YES             order
# len()        NO              loops
# in           NO              check
"""

# 1 Create a List
a = [1, 2, 3, 4, 1, 5]
b = []
c = list("ABC")     # ['A', 'B', 'C']
print(a,b,c)

# ️2 Length of a List
num=len(a)
print(num)

# 3 Access Elements (Indexing)
a = [10, 20, 30]
print(a[0])
print(a[1])
print(a[-1])
print(a[len(a)-1]) # len(a)-1 is the index of the last element
# print(a[len(a)]) # out of range
# ⚠️ Index starts at 0, the last index is len(a)-1,not len(a)

# 4 Modify Elements by Index
a = [5, 6, 7]
a[0] = 100
print(a) # [100, 6,7]
a[2] = 0
print(a) # [100, 6, 0]

# 5 append(x): adds an element to the end of the list.
a = []
a.append(1)
print(a)
a.append(2)
print(a)
a.append(3)
print(a) # Result:[1, 2, 3]

# 6 pop()
# 6.1 pop() — remove last element
a = [10, 20, 30]
x = a.pop()
print(x)
print(a)
# Result: x = 30, a = [10, 20]

# 6.2 pop(i) — remove by index
a = [5, 6, 7, 8]
a.pop(1)
print(a)
# Result: [5, 7, 8]

# 7 remove(x): removes the first x.
a = [1, 2, 3, 2, 4]
a.remove(2)
print(a)
a.remove(2)
print(a)
# Result:[1, 3, 2, 4]
a.remove(0)
print(a)
# ⚠️ If x does not exist → error

️# 8 count(x): counts how many times x appears.
a = [1, 2, 2, 3, 2]
num=a.count(2)
print(num)

# 9 sort(): sorts list in ascending order (in-place).
a = [4, 1, 3, 2]
a.sort()
print(a) # Result: [1, 2, 3, 4]
# a = a.sort()  # ❌ WRONG

# 10 reverse(): reverses list in place.
a = [1, 2, 3]
a.reverse()
print(a)
# Result: [3, 2, 1]

# 11 Clear a List
a = [1, 2, 3]
a.clear()
print(a)
# Result:[]

# 12 Copy a List
a = [1, 2, 3]
b = a.copy()
print(b)
# or
c = a[:]
print(c)
# ❌ Wrong (same reference) b = a
a = [1, 2, 3]
b = a
c = a.copy() # or c = a[:]
b.append(4)
print(a)# result:[1, 2, 3, 4]
print(c)# result:[1, 2, 3]

# 13 Combine Lists
a = [1, 2]
b = [3, 4]
c = a + b
print(c)
# Result:[1, 2, 3, 4]

# 14 Convert List ↔ String
# List → String
a = ['A', 'B', 'C']
s = "".join(a)

# String → List
s = "ABC"
a = list(s)

# 15 Membership Test (in)
a = [1, 2, 3]
2 in a     # True
5 in a     # False

