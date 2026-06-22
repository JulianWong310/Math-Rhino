"""
2026/01/24
https://dmoj.ca/problem/ccc20j1
"""
s=int(input())
m=int(input())
l=int(input())
x=1*s+2*m+3*l
if x>=10:
    print("happy")
else:
    print("sad")