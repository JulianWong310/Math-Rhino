"""
2026/01/25
https://dmoj.ca/problem/ccc19j1
"""
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
x=a*3+b*2+c*1
y=d*3+e*2+f*1
if x>y:
    print("A")
elif x<y:
    print("B")
else:
    print("T")