"""
2026/02/05
https://dmoj.ca/problem/ccc24j3
"""

n=int(input())
largest=float("-inf")
second=float("-inf")
third=float("-inf")
lst=[int(input()) for i in range(n)]
for x in lst:
    if largest<x:
        third=second
        second=largest
        largest=x
    elif x<largest and x>second:
        third=second
        second=x
    elif x<second and x>third:
        third=x
nums=lst.count(third)
print(third,nums)