"""
2026/01/10
https://dmoj.ca/problem/ccc07j1
"""

a=int(input())
b=int(input())
c=int(input())

m=a
if a<=b<=c or c<=b<=a:
    m=b
elif a<=c<=b or b<=c<=a:
    m=c
else:
    m=a

print(m)