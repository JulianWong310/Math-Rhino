"""
2026/02/06
https://dmoj.ca/problem/ccc14j1
"""
lst=[int(input())for i in range(3)]
if lst[0] == 60 and lst[1] == 60 and lst[2] == 60:
    print("Equilateral")
elif lst[0] + lst[1] + lst[2] == 180 and (lst[0] == lst[1] or lst[2] == lst[1] or lst[0] == lst[2]):
    print("Isosceles")
elif lst[0] + lst[1] + lst[2] == 180:
    print("Scalene")
else:
    print("Error")